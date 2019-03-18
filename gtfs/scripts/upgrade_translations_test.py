import os
import os.path
import shutil
import tempfile
import unittest

from upgrade_translations import TranslationsConverter


def get_file_contents(filename):
    with open(filename, 'rt') as f:
        return f.read()
    

class TestTranslationsConverter(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_convert_translations(self):
        testdata_dir = os.path.join(os.path.dirname(__file__), 'testdata')
        output_dir = os.path.join(self.test_dir, 'new-feed')
        want_feed_dir = os.path.join(testdata_dir, 'new-feed')
        converter = TranslationsConverter(os.path.join(testdata_dir, 'old-feed'))
        converter.convert_translations(output_dir)
        for filename in sorted(os.listdir(want_feed_dir)):
            if not filename.endswith('.txt'):
                continue
            got_filename = os.path.join(output_dir, filename)
            want_filename = os.path.join(want_feed_dir, filename)            
            self.assertTrue(os.path.exists(got_filename))
            self.assertEqual(get_file_contents(want_filename),
                             get_file_contents(got_filename))
