#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Generates a GraphViz DOT file that Visualizes pathway graph for a given GTFS feed.

Graph vertices are stations, platforms, entrances, generic nodes and boarding areas.
Graph edges are pathways.

Legend for vertices:
* platform: light sky blue
* station: light yellow
* entrance: light coral
* generic_node: light grey
* boarding_area: springgreen

Usage:

  $ visualize_pathways.py my-feed-dir my-feed.dot
  $ dot -T png -o my-feed.png my-feed.dot
"""

from enum import Enum
import csv
import re
import os
import sys


class LocationType(Enum):
    """Types of locations in stops.txt (field location_type).
    """
    platform = 0
    station = 1
    entrance = 2
    generic_node = 3
    boarding_area = 4


class PathwayMode(Enum):
    """Modes of pathways in pathways.txt (field pathway_mode).
    """
    unknown = 0
    walkway = 1
    stairs = 2
    moving_sidewalk = 3
    escalator = 4
    elevator = 5
    fare_gate = 6
    exit_gate = 7


class GtfsLocation(object):
    """GTFS location of any type: station, entrance etc defined in stops.txt.
    """
    def __init__(self, row, gtfs_reader):
        self._row = row
        self._reader = gtfs_reader
        self.gtfs_id = row['stop_id'].strip()
        self.location_type = LocationType(
            int(row.get('location_type', 0) or 0))
        self.name = row['stop_name'].strip()
        self.platform_code = row.get('platform_code', '').strip() or None
        self.signposted_as = row.get('signposted_as', '').strip() or None
        self.parent_id = row.get('parent_station', '').strip() or None
        self.children = []
        self.outgoing_pathways = []
        self.incoming_pathways = []

    @property
    def parent(self):
        if self.parent_id:
            return self._reader.get_location(self.parent_id)
        return None

    def station(self):
        result = self
        while result.parent_id:
            result = result.parent
        return result

    def add_to_parent(self):
        if self.parent_id:
            self.parent.children.append(self.gtfs_id)

    def has_children(self):
        return len(self.children) > 0

    def add_outgoing_pathway(self, pathway_id):
        self.outgoing_pathways.append(pathway_id)

    def add_incoming_pathway(self, pathway_id):
        self.incoming_pathways.append(pathway_id)

    def has_pathways(self):
        return (len(self.incoming_pathways) > 0 or
                len(self.outgoing_pathways) > 0)

    def self_or_children_have_pathways(self):
        if self.has_pathways():
            return True
        for child_id in self.children:
            if self._reader.get_location(
                    child_id).self_or_children_have_pathways():
                return True
        return False


class GtfsPathway(object):
    """GTFS pathway defined in pathways.txt.
    """
    def __init__(self, row, gtfs_reader):
        self._row = row
        self._reader = gtfs_reader
        self.gtfs_id = row['pathway_id'].strip()
        self.from_id = row['from_stop_id'].strip()
        self.to_id = row['to_stop_id'].strip()
        self.mode = PathwayMode(int(row.get('pathway_mode', 0) or 0))
        self.is_bidirectional = int(row.get('is_bidirectional', 0) or 0)
        self.signposted_as = row.get('signposted_as', '').strip() or None
        self.reversed_signposted_as = row.get(
            'reversed_signposted_as', '').strip() or None

    @property
    def from_location(self):
        return self._reader.get_location(self.from_id)

    @property
    def to_location(self):
        return self._reader.get_location(self.to_id)

    def add_to_endpoints(self):
        self.from_location.add_outgoing_pathway(self.gtfs_id)
        self.to_location.add_incoming_pathway(self.gtfs_id)


class GtfsReader(object):
    """Reads GTFS data relevant for pathway visualization: stops.txt and
    pathways.txt.

    """
    def __init__(self, gtfs_dir):
        self.gtfs_dir = gtfs_dir
        self._read_locations()
        self._read_pathways()

    def get_location(self, stop_id):
        return self._locations_map[stop_id]

    @property
    def locations(self):
        return self._locations_map.values()

    def get_pathway(self, stop_id):
        return self._pathways_map[stop_id]

    @property
    def pathways(self):
        return self._pathways_map.values()

    def _read_locations(self):
        self._locations_map = self._read_table('stops', GtfsLocation)
        for location in self.locations:
            location.add_to_parent()

    def _read_pathways(self):
        self._pathways_map = self._read_table('pathways', GtfsPathway)
        for pathway in self.pathways:
            pathway.add_to_endpoints()

    def _read_table(self, table, entity_type):
        entities = {}
        with open(os.path.join(self.gtfs_dir, '%s.txt' % table)) as f:
            reader = csv.DictReader(f)
            for row in reader:
                entity = entity_type(row, self)
                entities[entity.gtfs_id] = entity
        return entities


_VALID_GRAPHVIZ_ID = re.compile(r'^[A-Za-z_][A-Za-z0-9_]+$')


def escape_graphviz_id(gtfs_id):
    if _VALID_GRAPHVIZ_ID.match(gtfs_id):
        return gtfs_id
    return '"%s"' % gtfs_id.replace('"', r'\"')


def truncate_string(s, max_length=20):
    if max_length <= 0 or len(s) < max_length:
        return s
    return '%s..%s' % (s[:max_length - 4], s[-2:])


class Attributes(object):
    """Helper for pretty-printing attributes:

      label="Platform 2" color=springgreen shape=oval

    """
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def __str__(self):
        return ' '.join(
            '%s=%s' % (k, escape_graphviz_id(v))
            for k, v in self.attributes.items()
            if v is not None)


class GraphViz(object):
    """Keeps all data for a GraphViz DOT file: nodes, clustes and edges.

    """
    def __init__(self):
        self.nodes = []
        self.clusters = {}
        self.edges = []

    def __str__(self):
        result = 'digraph D {\n  node [ %s ]\n' % Attributes(style='filled')
        for cluster in self.clusters.values():
            result += '\n  %s\n' % cluster.indent(1)
        for node in self.nodes:
            result += '  %s\n' % node
        result += '\n'
        for edge in self.edges:
            result += '\n  %s\n' % edge
        result += '}\n'
        return result

    def add_cluster(self, cluster):
        self.clusters[cluster.id] = cluster

    def get_cluster(self, id):
        return self.clusters[id]


class GraphCluster(object):
    """A GraphViz cluster that groups several nodes.
    """
    def __init__(self, id, label, color):
        self.id = id
        self.label = label
        self.color = color
        self.nodes = []
        self.clusters = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_cluster(self, cluster):
        self.clusters[cluster.id] = cluster

    def get_cluster(self, id):
        return self.clusters[id]

    def __str__(self):
        return self.indent(0)

    def indent(self, level):
        indent_str = '  ' * level
        result = 'subgraph %s {\n' % (
            escape_graphviz_id('cluster_%s' % self.id))
        result += '%s  graph [ %s ]\n' % (
            indent_str,
            Attributes(
                style='filled',
                color=self.color,
                label=self.label))
        for cluster in self.clusters.values():
            result += '\n%s  %s\n' % (indent_str, cluster.indent(level + 1))
        for node in self.nodes:
            result += '\n%s  %s\n' % (indent_str, node)
        result += '%s}' % indent_str
        return result


class GraphNode(object):
    """A GraphViz node.

    """
    def __init__(self, id, label, color, shape):
        self.id = id
        self.label = label
        self.color = color
        self.shape = shape

    def __str__(self):
        return '%s [ %s ]' % (
            escape_graphviz_id(self.id), Attributes(
                label=self.label,
                color=self.color,
                shape=self.shape))


class GraphEdge(object):
    """A GraphViz edge.

    """
    def __init__(self, source, destination, direction, label):
        self.source = source
        self.destination = destination
        self.direction = direction
        self.label = label

    def __str__(self):
        return 'edge [ %s ]\n  %s -> %s [ %s ]' % (
            Attributes(dir=self.direction),
            escape_graphviz_id(self.source),
            escape_graphviz_id(self.destination),
            Attributes(label=self.label))


def location_color(location_type):
    colors = {
        LocationType.platform: "lightskyblue",
        LocationType.station: "lightyellow",
        LocationType.entrance: "lightcoral",
        LocationType.generic_node: "lightgrey",
        LocationType.boarding_area: "springgreen",
    }
    return colors.get(location_type, "blue")


def location_shape(location_type):
    shapes = {
        LocationType.platform: "box",
        LocationType.station: "polygon",
        LocationType.entrance: "triangle",
        LocationType.generic_node: "diamond",
        LocationType.boarding_area: "oval",
    }
    return shapes.get(location_type, "blue")


def location_label(location, max_length=20):
    label = location.gtfs_id
    if location.platform_code:
        label += '\\nPlatform %s' % location.platform_code
    elif location.signposted_as:
        label += '\\n%s' % location.signposted_as
    elif location.name:
        label += '\\n%s' % truncate_string(location.name, max_length)
    return label


def pathway_label(pathway):
    label = pathway.mode.name
    if pathway.signposted_as:
        label += '\\n%s' % truncate_string(pathway.signposted_as)
    if pathway.reversed_signposted_as:
        label += '\\n%s' % truncate_string(pathway.reversed_signposted_as)
    return label


def requires_platform_cluster(location):
    return (location.location_type == LocationType.platform and
            location.has_children())


def gtfs_to_graphviz(gtfs):
    """Reads GTFS data and returns GraphViz DOT file content as string.

    """
    graph = GraphViz()

    # Skip locations that are not involved in pathway graph.
    locations = [location
                 for location in gtfs.locations
                 if location.station().self_or_children_have_pathways()]

    for location in locations:
        if not location.parent_id:
            graph.add_cluster(GraphCluster(
                location.gtfs_id,
                location_label(location, max_length=-1),
                location_color(location.location_type)))

    for location in locations:
        if location.parent_id and requires_platform_cluster(location):
            graph.get_cluster(location.parent_id).add_cluster(GraphCluster(
                location.gtfs_id,
                location_label(location),
                location_color(location.location_type)))

    for location in locations:
        if not location.parent_id or requires_platform_cluster(location):
            continue
        node = GraphNode(
            location.gtfs_id,
            location_label(location, max_length=25),
            location_color(location.location_type),
            location_shape(location.location_type))
        cluster = graph.get_cluster(location.station().gtfs_id)
        if location.location_type == LocationType.boarding_area:
            cluster = cluster.get_cluster(location.parent_id)
        cluster.nodes.append(node)

    for pathway in gtfs.pathways:
        graph.edges.append(GraphEdge(
            pathway.from_id, pathway.to_id,
            'both' if pathway.is_bidirectional else 'forward',
            pathway_label(pathway)))

    return graph


def main():
    if len(sys.argv) < 2:
        print('usage: visualize_pathways.py [GTFS DIR] [OUTPUT DIR]',
              file=sys.stderr)
        sys.exit(1)
    graph = gtfs_to_graphviz(GtfsReader(sys.argv[1]))
    with open(sys.argv[2], 'w+') as dot_f:
        dot_f.write(str(graph))


if __name__ == '__main__':
    main()
