#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmapiproxy.py
#
#         USAGE:  ./proxy/osmapiproxy.py
#                 ./proxy/osmapiproxy.py --help
#                 hug --port 8000 -f ./proxy/osmapiproxy.py
#                 # curl http://localhost:8000/
#
#   DESCRIPTION:  See http://www.hug.rest/
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - hug (pip install hug -U)
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

"""A simple example of a hug API call with versioning"""
import json
import os
import requests
import hug

DE_FACTO_API_BASE = os.getenv(
    'DE_FACTO_API', 'https://www.openstreetmap.org/api/0.6')


@hug.format.content_type('application/xml')
def format_as_xml(data, request=None, response=None):
    return str(data).encode('utf8')


suffix_output = hug.output_format.suffix({
    # '.xml': format_as_xml,
    '.json': hug.output_format.json,
    # '.xml': hug.output_format.html,
    # '.html': hug.output_format.html,
    '.xml': hug.output_format.text,
    '': hug.output_format.text,
})


@hug.get('/echo', versions=1)
def echo(text):
    return text


# http://localhost:8000/changeset/1.json

@hug.get('/changeset/{changeset_and_format}', output=suffix_output)
def api_changeset_xml(changeset_and_format):
    print(DE_FACTO_API_BASE + '/changeset/' + changeset_and_format)
    content = requests.get(
        DE_FACTO_API_BASE + '/changeset/' + changeset_and_format)

    if changeset_and_format.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result


# @hug.get('/changeset/{changeset_id}.{format}', output=suffix_output)
# def api_changeset_anyformat(changeset_id, format):
#     print(DE_FACTO_API_BASE + '/changeset/' + changeset_id + '.' + format)
#     content = requests.get(
#         DE_FACTO_API_BASE + '/changeset/' + changeset_id + '.' + format)
#     return content
# https://www.openstreetmap.org/api/0.6/changeset/129373852

# @hug.get('/echo', versions=range(2, 5))
# def echo(text):
#     return 'Echo: {text}'.format(**locals())


@hug.get('/unversioned')
def hello():
    return 'Hello world!'
