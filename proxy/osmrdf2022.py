#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmrdf2022.py
#
#         USAGE:  # this is a library. Import into your code:
#                     from osmrdf2022 import *
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.1.0
#       CREATED:  2022-11-25 19:22 UTC v1.0.0 started
#      REVISION:  ---
# ==============================================================================

import xml.etree.ElementTree as XMLElementTree

RDF_TURTLE_PREFIXES = [
    'PREFIX osmnode: <https://www.openstreetmap.org/node/>',
    'PREFIX osmway: <https://www.openstreetmap.org/way/>',
]


class OSMApiv06Xml:
    """OSMApiv06Xml

    Not so optimized quick parser for XML files that can fit into memory
    """

    iterator: None
    xmlroot: None  # xml.etree.ElementTree.Element
    root_tag: str  # Example: osm
    root_attrib: dict
    child_1_tag: str
    child_1_attr: dict
    # @TODO for full dumps, will have 1-n child items

    def __init__(self, file_or_string: str) -> None:

        # @TODO maybe eventually implement from file (the large ones)
        # self.iterator = XMLElementTree.iterparse(
        #     source=file_or_string,
        #     events=('start', 'end')
        # )

        # self.iterator = XMLElementTree.fromstring(
        #     file_or_string,
        #     events=('start', 'end')
        # )
        root = XMLElementTree.fromstring(file_or_string)
        self.xmlroot = root
        self.root_tag = root.tag
        self.root_attrib = root.attrib
        print(root)
        print(root.tag)
        print(root.attrib)
        print(type(root.attrib))
        print(type(root))

        for child in root:
            print('>>>>> ', child.tag, child.attrib)

        # print(root.findall("."))
        # print(root.findall(".[0]"))

        # child_1 = next(root)
        # self.child_1_tag = child_1.tag
        # self.child_1_attr: child_1.attrib

        # print(self.child_1_tag, self.child_1_attr)
        # pass


def osmrdf_node_xml2ttl(data_xml: str):

    osmx = OSMApiv06Xml(data_xml)

    output = []
    output.extend(RDF_TURTLE_PREFIXES)
    output.append('')

    output.append('# TODO turtle here')

    output.append('')
    comment = "# " + "\n# ".join(data_xml.split("\n"))
    output.append(comment)

    return "\n".join(output)
