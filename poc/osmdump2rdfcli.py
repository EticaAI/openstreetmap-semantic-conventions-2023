#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmdump2rdfcli.py
#
#         USAGE:  ./osmdump2rdfcli.py --help
#
#   DESCRIPTION:  ---
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.2.0
#       CREATED:  2022-11-27 03:14 UTC v0.2.0 started
#      REVISION:  ---
# ==============================================================================

from osmrdf2022 import (
    osmrdf_xmldump2_ttl
)
import json
import os
import requests
import requests_cache
import hug

# https://download.geofabrik.de/africa/sao-tome-and-principe.html

# curl --output ./tmp/sao-tome-and-principe-latest.osm.bz2 https://download.geofabrik.de/africa/sao-tome-and-principe-latest.osm.bz2
# bunzip2 ./tmp/sao-tome-and-principe-latest.osm.bz2


osmrdf_xmldump2_ttl('./tmp/sao-tome-and-principe-latest.osm')


# ./osmdump2rdfcli.py --help
# ./osmdump2rdfcli.py > ./tmp/sao-tome-and-principe-latest.osm.ttl

# rdfpipe --input-format='ttl' --output-format=longturtle ./tmp/sao-tome-and-principe-latest.osm.ttl > ./tmp/sao-tome-and-principe-latest~longturtle.osm.ttl
