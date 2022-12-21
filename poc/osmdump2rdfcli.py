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
#       VERSION:  v0.3.0
#       CREATED:  2022-11-27 03:14 UTC v0.2.0 started
#      REVISION:  2022-12-21 01:46:00Z v0.3.0 osmrdf2022.py -> osmrdf2023.py
# ==============================================================================

import argparse
import sys
# from poc.osmrdf2023 import (
from osmrdf2023 import (
    # osmrdf_xmldump2_ttl,
    osmrdf_xmldump2_ttl_v2,
    OSMElementFilter
)

STDIN = sys.stdin.buffer

NOMEN = 'osmdump2rdfcli'
PROGRAM_EXE = __file__

DESCRIPTION = f"""
{PROGRAM_EXE} Proof of concept for OSM RDF 2022, CLI alternative \
(intended to run on dumps) to the proxy version.
"""

__EPILOGUM__ = f"""
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
Read from file on disk . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {PROGRAM_EXE} tmp/STP.osm
    {PROGRAM_EXE} tmp/STP.osm > tmp/STP.osm.ttl
    {PROGRAM_EXE} --filter-xml-tag='way' tmp/STP.osm > tmp/STP~ways.osm.ttl

Pipe from other commands . . . . . . . . . . . . . . . . . . . . . . . . . . .
    cat tmp/STP.osm | {PROGRAM_EXE}
    bzcat tmp/BRA-north.osm.bz2 | {PROGRAM_EXE}
    bzcat tmp/BRA-north.osm.bz2 | {PROGRAM_EXE} --filter-xml-tag='relation'

Re-tag (without full inference) . . . . . . . . . . . . . . . . . . . . . . .
    {PROGRAM_EXE} --retagger-file=tmp/tagger.rdfstxt.tsv tmp/STP.osm 

Download external data examples ______________________________________________

Geofabrik download + decompress  . . . . . . . . . . . . . . . . . . . . . . .
    curl --output tmp/STP.osm.bz2 \
https://download.geofabrik.de/africa/sao-tome-and-principe-latest.osm.bz2
    bunzip2 tmp/STP.osm.bz2

Geofabrik download (but not decompress)  . . . . . . . . . . . . . . . . . . .
    curl --output tmp/BRA-north.osm.bz2 \
https://download.geofabrik.de/south-america/brazil/norte-latest.osm.bz2

Overpass download examples . . . . . . . . . . . . . . . . . . . . . . . . . .
(See http://overpass-api.de/command_line.html)
    curl --output tmp/target.osm --silent --globoff \
"https://overpass-api.de/api/interpreter?data=node[name=\"Gielgen\"];out;"
    curl --output tmp/speed-200.osm --silent --globoff \
"https://overpass-api.de/api/interpreter?data=way[maxspeed=\"200\"];out;"

Other ________________________________________________________________________

Create not-so-smart-inference (hardcoded auto tagger) . . . . . . . . . . . . .
    echo "-<TAB>*<TAB>*<TAB>created_by=*<NEWLINE>\
+<TAB><way>|<relation><TAB>*<TAB>ISO3166-1:alpha3=BRA<TAB>" \
> tmp/tagger.rdfstxt.tsv

Mapping  . . . . . . . . . . . . . . . . . . . . . . . .
    echo "-<TAB>*<TAB>*<TAB>created_by=*<NEWLINE>\
+<TAB><way>|<relation><TAB>*<TAB>ISO3166-1:alpha3=BRA<TAB>" \
> tmp/tagger.rdfstxt.tsv

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

# https://overpass-turbo.eu/s/1ohl
# way({{bbox}})[highway=residential]
#   [maxspeed](if:t["maxspeed"]>120);
# out geom;

# @see also https://gis.stackexchange.com/questions/127315/filtering-overpass-api-by-country

# https://overpass-turbo.eu/s/1ohm
# area["ISO3166-1:alpha3"="BRA"]->.boundaryarea;
# (
# way(area.boundaryarea)[maxspeed](if:t["maxspeed"]>120);
# );
# out meta;


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    venandum_insectum: bool = False  # noqa: E701

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def make_args(self, hxl_output=True):
        parser = argparse.ArgumentParser(
            prog=NOMEN,
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Input file',
            # required=False,
            nargs='?'
        )

        parser.add_argument(
            '--real-infile-path',
            help='(Quick workaround for edge cases) in case infile becomes'
            'ambigous on shell scripting, use this to force real source path',
            dest='real_infile',
            nargs='?',
            default=None,
            required=False,
        )

        parser.add_argument(
            '--retagger-file',
            help='(Poors man\'s inference) sPath to a TSV file to apply OSM '
            'Tags before output RDF',
            dest='retagger_file',
            nargs='?',
            default=None,
            required=False,
        )

        parser.add_argument(
            '--filter-xml-tag',
            help='Filter XML tags',
            dest='xml_tags',
            nargs='?',
            type=lambda x: x.split(','),
            default=None
        )

        parser.add_argument(
            '--filter-xml-tag-not',
            help='Filter XML tags (not)',
            dest='xml_tags_not',
            nargs='?',
            type=lambda x: x.split(','),
            default=None
        )

        return parser.parse_args()

    def execute_cli(
            self, pyargs, stdin=STDIN, stdout=sys.stdout,
            stderr=sys.stderr):
        """execute_cli"""

        if pyargs.real_infile is not None:
            _infile = pyargs.real_infile
            _stdin = False
        else:
            if stdin.isatty():
                _infile = pyargs.infile
                _stdin = False
            else:
                _infile = None
                _stdin = True

        filter = OSMElementFilter()

        if pyargs.xml_tags:
            filter.set_filter_xml_tags(pyargs.xml_tags)

        if pyargs.xml_tags_not:
            filter.set_filter_xml_tags_not(pyargs.xml_tags_not)

        retagger = None
        if pyargs.retagger_file:
            _file = open(pyargs.retagger_file,mode='r')
            retagger = _file.read()
            _file.close()

        if _stdin:
            osmrdf_xmldump2_ttl_v2(stdin, filter)
        else:
            osmrdf_xmldump2_ttl_v2(_infile, filter, retagger)
        # print('todo')


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()
    # print('  >>>>  args', args)
    # raise ValueError(args)

    est_cli.execute_cli(args)

# osmrdf_xmldump2_ttl('./tmp/sao-tome-and-principe-latest.osm')


# ./osmdump2rdfcli.py --help
# ./osmdump2rdfcli.py > ./tmp/sao-tome-and-principe-latest.osm.ttl

# rdfpipe --input-format='ttl' --output-format=longturtle ./tmp/sao-tome-and-principe-latest.osm.ttl > ./tmp/sao-tome-and-principe-latest~longturtle.osm.ttl
