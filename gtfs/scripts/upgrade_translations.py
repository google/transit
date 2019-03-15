#!/usr/bin/python3
"""
Upgrades GTFS data from Google translations extension [1] to GTFS-Translations [2].

[1] http://developers.google.com/transit/gtfs/reference/gtfs-extensions#translationstxt
[2] http://bit.ly/gtfs-translations
"""
import csv
import os
import os.path
import shutil
import sys

RECORD_ID_MAP = {
    # Record ids defined in GTFS-Translations spec.
    'agency': ('agency_id', None),
    'stops': ('stop_id', None),
    'routes': ('route_id', None),
    'trips': ('trip_id', None),
    'stop_times': ('trip_id', 'stop_sequence'),
    'feed_info': (None, None),
    'calendar': ('service_id', None),
    'calendar_dates': ('service_id', 'date'),
    'fare_attributes': ('fare_id', None),
    'fare_rules': ('fare_id', 'route_id'),
    'shapes': ('shape_id', 'shape_pt_sequence'),
    'frequencies': ('trip_id', 'start_time'),
    'transfers': ('from_stop_id', 'to_stop_id'),
    # Additional record ids supported by Google.
    'pathways': ('pathway_id', None),
    'levels': ('level_id', None),
    'properties': ('property_id', None),
    'vehicle_carriages': ('carriage_id', None),
    'vehicles': ('vehicle_id', None),
}

NEW_TRANSLATIONS_FIELDS = [
    'table_name', 'field_name', 'language', 'translation',
    'record_id', 'record_sub_id', 'field_value',
]


def get_record_id(table_name, row, id_index=0):
  field_name = RECORD_ID_MAP.get(table_name, (None, None))[id_index]
  if field_name:
    return row.get(field_name)
  return ''


def get_record_sub_id(table_name, row):
  return get_record_id(table_name, row, 1)


def read_first_available_value(filename, field_name):
  if not os.path.exists(filename):
    return None
  with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      value = row.get(field_name)
      if value:
        return value
  return None


def is_translatable_field(gtfs_file, field):
  for suffix in '_name', '_desc', '_headsign', '_url':
    if field.endswith(suffix):
      return True
  return False


class TranslationsConverter(object):

  def __init__(self, src_dir):
    self.src_dir = src_dir
    self.find_feed_language()
    self.read_translations()
    self.find_context_dependent_names()

  def find_feed_language(self):
    self.feed_language = (read_first_available_value(
            os.path.join(self.src_dir, 'feed_info.txt'), 'feed_lang') or
      read_first_available_value(
            os.path.join(self.src_dir, 'agency.txt'), 'agency_lang'))
    if not self.feed_language:
       raise Exception('Cannot find default feed language in feed_info.txt and agency.txt')
    print ('\tfeed language: %s' % self.feed_language)

  def read_translations(self):
    print('Reading original translations')
    self.translations_map = {}
    n_translations = 0
    with open(
        os.path.join(self.src_dir, 'translations.txt'), newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        self.translations_map.setdefault(
            row['trans_id'], {})[row['lang']] = row['translation']
        n_translations += 1
    print('\ttotal original translations: %s' % n_translations)

  def find_context_dependent_names(self):
    n_occurences_of_original = {}
    for trans_id, translations in self.translations_map.items():
      try:
        original_name = translations[self.feed_language]
      except KeyError:
        raise Exception(
            'No translation in default feed language for %s, available: %s' %
            (trans_id, translations))
      n_occurences_of_original[original_name] = 1 + n_occurences_of_original.get(
          original_name, 0)

    self.context_dependent_names = set(
        name
        for name, occur in n_occurences_of_original.items()
        if occur > 1)
    print ('Total context-dependent translations: %d' %
           len(self.context_dependent_names))

  def convert_translations(self, dest_dir):
    """
    Converts translations to the new format and stores at dest_dir.
    """
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    total_translation_rows = 0
    with open(os.path.join(dest_dir, 'translations.txt'), 'w+t', newline='') as out_file:
      writer = csv.DictWriter(out_file, fieldnames=NEW_TRANSLATIONS_FIELDS)
      writer.writeheader()
      for filename in os.listdir(self.src_dir):
        if not (filename.endswith('.txt') and
                os.path.isfile(os.path.join(self.src_dir, filename))):
          print ('Skipping %s' % filename)
          continue
        table_name = filename[:-len('.txt')]
        if table_name == 'translations':
          continue
        if table_name not in RECORD_ID_MAP:
          print ('Copying %s' % filename)
          shutil.copyfile(os.path.join(self.src_dir, filename),
                          os.path.join(dest_dir, filename))
        else:
          total_translation_rows += self.translate_table(dest_dir, table_name, writer)
    print ('Total translation rows: %s' % total_translation_rows)

  def translate_table(self, dest_dir, table_name, translations_writer):
    """
    Converts translations to the new format for a single table.
    """
    in_filename = os.path.join(self.src_dir, '%s.txt' % table_name)
    if not os.path.exists(in_filename):
      raise Exception('No %s' % table_name)

    out_filename = os.path.join(dest_dir, '%s.txt' % table_name)

    # stop_times.txt and trips.txt usually have a lot of repeated headsigns, so
    # it is better to use field_value than record_id and record_sub_id.
    # However, we will fallback to record_id+sub_id if the translation is
    # context-dependent, e.g., the same trip_headsign is translated differently
    # for different trips.
    table_uses_record_id = table_name not in ('stop_times', 'trips')
    translations_for_values = {}

    print('Translating %s by %s' %
          (table_name, 'record_id' if table_uses_record_id else 'field_name'))
    total_translation_rows = 0

    with open(in_filename, newline='') as in_file:
      with open(out_filename, 'w+t', newline='') as out_file:
        reader = csv.DictReader(in_file)
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
          out_row = row
          for field_name, field_value in row.items():
            if not is_translatable_field(table_name, field_name):
              continue
            field_translations = self.translations_map.get(field_value)
            if not field_translations:
              continue
            out_row[field_name] = field_translations.get(
                self.feed_language, field_value)
            value_in_feed_lang = field_translations[self.feed_language]
            # If translation depends on the context, then always use record_id.
            row_uses_record_id = (
                table_uses_record_id or
                value_in_feed_lang in self.context_dependent_names)
            for language, translation in field_translations.items():
              if language == self.feed_language:
                continue
              if row_uses_record_id:
                translations_writer.writerow({
                    'table_name': table_name,
                    'field_name': field_name,
                    'language': language,
                    'translation': translation,
                    'record_id': get_record_id(table_name, row),
                    'record_sub_id': get_record_sub_id(table_name, row)
                })
                total_translation_rows += 1
              else:
                translations_for_values[(field_name, language,
                                         value_in_feed_lang)] = translation

          writer.writerow(out_row)

    for ((field_name, language, field_value),
         translation) in translations_for_values.items():
      translations_writer.writerow({
          'table_name': table_name,
          'field_name': field_name,
          'language': language,
          'translation': translation,
          'field_value': field_value,
      })
      total_translation_rows += 1

    print('\ttranslation rows: %s' % total_translation_rows)
    return total_translation_rows


def main():
  if len(sys.argv) < 2:
    print ('usage: upgrade_translations.py [SRC GTFS DIR] [DEST GTFS DIR]',
           file=sys.stderr)
    sys.exit(1)

  src_dir = os.path.normpath(sys.argv[1])
  if len(sys.argv) >= 3:
    dest_dir = sys.argv[2]
  else:
    dest_dir = '%s_upgraded' % src_dir

  print ('Upgrading translations')
  print ('\tsource directory: %s' % src_dir)
  print ('\tdestination directory: %s' % dest_dir)

  TranslationsConverter(src_dir).convert_translations(dest_dir)
  print ('Done!')

if __name__ == '__main__':
  main()
