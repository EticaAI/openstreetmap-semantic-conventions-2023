#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmapi2rdfproxy.py
#
#         USAGE:  ./proxy/osmapi2rdfproxy.py
#                 ./proxy/osmapi2rdfproxy.py --help
#                 hug -f ./proxy/osmapi2rdfproxy.py
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
# /opt/Protege-5.5.0/run.sh
import hug
import requests

# @hug.get('/cve', versions=1) 
# def cve(cve_number):
#     get_cve = requests.get('http://cve.mitre.org/cgi-bin/cvename.cgi?name='+cve_number)
#     return get_cve

"""A simple example of a hug API call with versioning"""
import hug


@hug.get('/echo', versions=1)
def echo(text):
    return text


@hug.get('/echo', versions=range(2, 5))
def echo(text):
    return 'Echo: {text}'.format(**locals())


@hug.get('/unversioned')
def hello():
    return 'Hello world!'
