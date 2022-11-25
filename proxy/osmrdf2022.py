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


RDF_TURTLE_PREFIXES = [
    'PREFIX osmnode: <https://www.openstreetmap.org/node/>',
    'PREFIX osmway: <https://www.openstreetmap.org/way/>',
]


def osmrdf_node_xml2ttl(data_xml: str):
    output = []
    output.extend(RDF_TURTLE_PREFIXES)
    output.append('')

    output.append('# TODO turtle here')

    output.append('')
    comment = "# " + "\n# ".join(data_xml.split("\n"))
    output.append(comment)

    return "\n".join(output)
