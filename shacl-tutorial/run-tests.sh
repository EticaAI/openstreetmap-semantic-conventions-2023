#!/bin/bash
#  Run with:
#    ./run-tests.sh

# "shacl" Requires Apache Jena CLI installed,
# @see https://jena.apache.org/documentation/shacl/index.html

set -x

shacl validate --shapes=shapes/R001_wikidata.shacl.ttl --data=data/R001_wikidata-invalid.tdata.ttl

shacl validate --shapes=shapes/R001_wikidata.shacl.ttl --data=data/R001_wikidata-valid.tdata.ttl

set +x
