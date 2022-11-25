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
import hug


@hug.get('/echo', versions=1)
def echo(text):
    return text

@hug.get('/changeset')
def echo(changeset_number):
    return changeset_number
# https://www.openstreetmap.org/api/0.6/changeset/129373852

# @hug.get('/echo', versions=range(2, 5))
# def echo(text):
#     return 'Echo: {text}'.format(**locals())


@hug.get('/unversioned')
def hello():
    return 'Hello world!'
