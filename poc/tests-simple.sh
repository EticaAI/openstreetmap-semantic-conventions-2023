#!/bin/bash
#===============================================================================
#
#          FILE:  tests-simple.sh
#
#         USAGE:  ./scripts/tests-simple.sh
#                 DUMP_LOG=dump.log.tsv ./scripts/wikibase-wiki-dump-items.sh
#                 DELAY=10 ./scripts/wikibase-wiki-dump-items.sh
#                 Q_START=1 Q_END=2 ./scripts/wikibase-wiki-dump-items.sh
#                 OPERATION=merge_p ./scripts/wikibase-wiki-dump-items.sh
#
#   DESCRIPTION:  This shell script will download Wikibase Ps and Qs in
#                 less efficient way, one by one. Cache individual results
#                 in disk (including errors). At the end it will merge
#                 the output into single files, already well formated
#                 in a preditable way (e.g. to allow diffs).
#                 The merging mecanism may
#
#       OPTIONS:  env WIKI_URL_ENTITYDATA=
#                     http://example.org/wiki/Special:EntityData/
#                 env DELAY
#                 env P_START
#                 env P_END
#                 env Q_START
#                 env Q_END
#                 env CACHE_ITEMS
#                 env CACHE_ITEMS_404
#                 env CACHE_ITEMS
#                 env CACHE_ITEMS_404
#                 env DUMP_LOG
#
#  REQUIREMENTS:  - curl
#                 - rdfpipe (pip install rdflib)
#                   - Used to merge results. Tested with rdflib 6.1.1. Feel
#                     free to use other tools to concatenate.
#
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-11-19 20:16 UTC
#      REVISION:  ---
#===============================================================================
set -e

ROOTDIR="$(pwd)"

#### internal variables ________________________________________________________
#### Fancy colors constants - - - - - - - - - - - - - - - - - - - - - - - - - -
tty_blue=$(tput setaf 4)
tty_green=$(tput setaf 2)
tty_red=$(tput setaf 1)
tty_normal=$(tput sgr0)

## Example
# printf "\n\t%40s\n" "${tty_blue}${FUNCNAME[0]} STARTED ${tty_normal}"
# printf "\t%40s\n" "${tty_green}${FUNCNAME[0]} FINISHED OKAY ${tty_normal}"
# printf "\t%40s\n" "${tty_blue} INFO: [] ${tty_normal}"
# printf "\t%40s\n" "${tty_red} ERROR: [] ${tty_normal}"
#### Fancy colors constants - - - - - - - - - - - - - - - - - - - - - - - - - -

#### functions _________________________________________________________________

#######################################
# Main loop. The output to screen will be a valid .tsv format. Example:
#   item<tab>result
#   Q1<tab>error cached
#   Q2<tab>cached
#   Q3<tab>downloaded
#
# Globals:
#    CACHE_ITEMS
#    CACHE_ITEMS_404
#    DUMP_LOG
#
# Arguments:
#
# Outputs:
#
#######################################
main_loop_items() {
  printf "\n\t%40s\n" "${tty_blue}${FUNCNAME[0]} STARTED ${tty_normal}"

  if [ ! -d "$CACHE_ITEMS" ]; then
    printf "%s\n" "${tty_red} ERROR: env CACHE_ITEMS \
[$CACHE_ITEMS]? ${tty_normal}"
    exit 1
  fi

  if [ ! -d "$CACHE_ITEMS_404" ]; then
    printf "%s\n" "${tty_red} ERROR: env CACHE_ITEMS_404 \
[$CACHE_ITEMS_404]? ${tty_normal}"
    exit 1
  fi

  # tab-separated output, START
  printf "\n%s\t%s" "item" "result"
  if [ -n "$DUMP_LOG" ]; then
    printf "%s\t%s\n" "item" "result" >"$DUMP_LOG"
  fi

  for ((c = P_START; c <= P_END; c++)); do
    download_wiki_item "P${c}" ""
  done
  for ((c = Q_START; c <= Q_END; c++)); do
    download_wiki_item "Q${c}" "?flavor=dump"
  done
  echo ""
  # tab-separated output, END

  printf "\t%40s\n" "${tty_green}${FUNCNAME[0]} FINISHED OKAY ${tty_normal}"
}

#### main ______________________________________________________________________

# if [ -z "${OPERATION}" ] || [ "${OPERATION}" = "download" ]; then
#   main_loop_items
# fi

set +e
set -x
xmllint --noout --schema temp-schema/osm-wiki-api-capabilities-v06.xsd tests/data/C0002.xml
echo ""
echo ""

xmllint --noout --schema temp-schema/osm-wiki-api-capabilities-v06.xsd tests/data/C0002.xml
echo ""
echo ""

xmllint --noout --schema temp-schema/osm-wiki-api-capabilities-v06.xsd tests/data/C0001.xml
echo ""
echo ""

xmllint --noout --schema temp-schema/OSMSchema.xsd tests/data/C0001.xml
set -x
echo ""
echo ""

jsonschema --instance tests/data/C0003.json temp-schema/osm.schema.json
set -x


# @TODO - http://tagfinder.herokuapp.com/apidoc
#         - http://tagfinder.herokuapp.com/tagfinder_thesaurus.rdf
