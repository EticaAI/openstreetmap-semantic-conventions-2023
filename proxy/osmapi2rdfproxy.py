#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmapi2rdfproxy.py
#
#         USAGE:  hug -f ./osmapi2rdfproxy.py --help
#                 # Expose http://localhost:8000/ as API endpoint:
#                     hug --port 8000 -f ./osmapi2rdfproxy.py
#                 # Disable cache of de facto API calls
#                     RDFPROXY_TTL="-1" hug -f ./osmapi2rdfproxy.py
#
#   DESCRIPTION:  Proxy over de facto public OpenStreetMap v0.6 API that adds
#                 turtle format as additional output intented to be used for
#                 local testing and/or feedback on the conventions.
#                 This is not intended for production or near-production use,
#                 however it implements python Hug (https://www.hug.rest/)
#                 (great at benchmarks, yet less code) and requests-cache
#                 (https://requests-cache.readthedocs.io/) so it is out of the
#                 box a great starting point, even if you don't know python.
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - hug (pip install hug -U)
#                   - requests-cache (pip install requests-cache)
#                 - osmrdf2022.py (Python library)
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.2.0
#       CREATED:  2022-11-25 15:53:00Z v0.1.0 started
#      REVISION:  2022-11-26 20:47:00Z v0.2.0 node, way, relation basic turtle,
#                                      only attached tags (no <nd> <member> yet)
# ==============================================================================

from osmrdf2022 import (
    osmrdf_node_xml2ttl,
    osmrdf_relation_xml2ttl,
    osmrdf_way_xml2ttl
)
import json
import os
import requests
import requests_cache
import hug

# user configuration ________________________________________________________

# TIP: enviroment variable DE_FACTO_API_BASE="" can be customized!
DE_FACTO_API_BASE = os.getenv(
    'DE_FACTO_API', 'https://www.openstreetmap.org/api/0.6')

# @see https://requests-cache.readthedocs.io/en/stable/
# File osmapi_cache.sqlite will cache backend calls
requests_cache.install_cache(
    'osmapi_cache',
    # https://requests-cache.readthedocs.io/en/stable/user_guide/backends.html
    backend=os.getenv('RDFPROXY_CACHE', 'sqlite'),
    # https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
    expire_after=os.getenv('RDFPROXY_TTL', '604800'),  # 7 days
)

# ### Hug overrides ____________________________________________________________


@hug.format.content_type('application/xml')
def format_as_xml(data, request=None, response=None):
    """format_as_xml
    @FIXME make Hug return XML formating instead of text
    """
    return str(data).encode('utf8')


@hug.format.content_type('text/turtle')
def format_as_turtle(data, request=None, response=None):
    """format_as_turtle custom Turtle output format for Hug
    """
    return str(data).encode('utf8')


# ### Tell Hug suffix can be used to infer output strategy _____________________
suffix_output = hug.output_format.suffix({
    '.json': hug.output_format.json,
    '.xml': format_as_xml,
    '.ttl': hug.output_format.text,
    '': hug.output_format.text,  # @FIXME use format_as_xml()
})

# ### Logic for API endpoints __________________________________________________
# @NOTE: This section mostly:
#        - Request+cache openstreetmap.org/api/0.6/ API calls and serve as it is
#        - If user ask .ttl, uses osmrdf2022.py to generate
# @BUG   While osmapi2rdfproxy.py is intented to only generate Turtle for
#        discussed types of data, the actuall OpenStreetMap API have more
#        endpoints than the ones here.

@hug.get('/changeset/{changeset_uid}', output=suffix_output)
def api_changeset(changeset_uid):
    """api_changeset /api/0.6/changeset/ (no changes, just proxy + cache)

    @example http://localhost:8000/changeset/1.json
    """
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
    # print(DE_FACTO_API_BASE + '/node/' + node_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/node/' + node_uid)

    if node_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result


# http://localhost:8000/node/1.ttl
# rdfpipe --input-format='ttl' --output-format=longturtle http://localhost:8000/node/2.ttl
@hug.get('/node/{node_uid}.ttl', output=format_as_turtle)
def api_node_ttl(node_uid):
    content = requests.get(
        DE_FACTO_API_BASE + '/node/' + node_uid + '.xml')

    result = osmrdf_node_xml2ttl(content.text)
    return result

# @see https://wiki.openstreetmap.org/wiki/Relation
# @see https://wiki.openstreetmap.org/wiki/Category:Relations
# http://localhost:8000/relation/10000.json
@hug.get('/relation/{relation_uid}', output=suffix_output)
def api_relation(relation_uid):
    # print(DE_FACTO_API_BASE + '/relation/' + relation_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/relation/' + relation_uid)

    if relation_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result

# http://localhost:8000/relation/10000.ttl
# rdfpipe --input-format='ttl' --output-format=longturtle http://localhost:8000/relation/10000.ttl


@hug.get('/relation/{relation_uid}.ttl', output=format_as_turtle)
def api_relation_ttl(relation_uid):
    content = requests.get(
        DE_FACTO_API_BASE + '/relation/' + relation_uid + '.xml')

    result = osmrdf_relation_xml2ttl(content.text)
    return result

# http://localhost:8000/way/100.json


@hug.get('/way/{way_uid}', output=suffix_output)
def api_way(way_uid):
    # print(DE_FACTO_API_BASE + '/way/' + way_uid)
    content = requests.get(
        DE_FACTO_API_BASE + '/way/' + way_uid)

    if way_uid.endswith('.json'):
        result = json.loads(content.text)
    else:
        result = content.text
    return result

# http://localhost:8000/way/100.ttl
# rdfpipe --input-format='ttl' --output-format=longturtle http://localhost:8000/way/100.ttl


@hug.get('/way/{way_id}.ttl', output=format_as_turtle)
def api_node_ttl(way_id):
    content = requests.get(
        DE_FACTO_API_BASE + '/way/' + way_id + '.xml')

    result = osmrdf_way_xml2ttl(content.text)
    return result
