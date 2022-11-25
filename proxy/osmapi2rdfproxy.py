#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmapi2rdfproxy.py
#
#         USAGE:  ./proxy/osmapi2rdfproxy.py
#                 hug --port 8000 -f ./proxy/osmapi2rdfproxy.py
#                 # curl http://localhost:8000/
#
#   DESCRIPTION:  RUN /999999999/0/999999999_54872.py --help
#                 - Q54872, https://www.wikidata.org/wiki/Q54872
#                   - Resource Description Framework
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
#       CREATED:  2022-11-25 15:53 UTC v0.1.0 started
#      REVISION:  ---
# ==============================================================================

import json
import os
import requests
import hug

DE_FACTO_API_BASE = os.getenv(
    'DE_FACTO_API', 'https://www.openstreetmap.org/api/0.6')


@hug.format.content_type('application/xml')
def format_as_xml(data, request=None, response=None):
    # @FIXME temporary, needs be fixed
    return str(data).encode('utf8')


suffix_output = hug.output_format.suffix({
    '.json': hug.output_format.json,
    '.xml': hug.output_format.text,
    '': hug.output_format.text,
})


@hug.get('/echo', versions=1)
def echo(text):
    return text


# http://localhost:8000/changeset/1.json
@hug.get('/changeset/{changeset_uid}', output=suffix_output)
def api_changeset(changeset_uid):
    print(DE_FACTO_API_BASE + '/changeset/' + changeset_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/changeset/' + changeset_uid)

    if changeset_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result


# http://localhost:8000/node/1.json
@hug.get('/node/{node_uid}', output=suffix_output)
def api_node(node_uid):
    print(DE_FACTO_API_BASE + '/node/' + node_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/node/' + node_uid)

    if node_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result


# http://localhost:8000/relation/10000.json
@hug.get('/relation/{relation_uid}', output=suffix_output)
def api_relation(relation_uid):
    print(DE_FACTO_API_BASE + '/relation/' + relation_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/relation/' + relation_uid)

    if relation_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result

# http://localhost:8000/way/100.json


@hug.get('/way/{way_uid}', output=suffix_output)
def api_way(way_uid):
    print(DE_FACTO_API_BASE + '/way/' + way_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/way/' + way_uid)

    if way_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result
