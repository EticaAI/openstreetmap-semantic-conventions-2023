## [EARLY DRAFT] Request for Feedback: OpenStreetMap RDF Schema 2023
[early draft][proof of concept] RDF/OWL samples from/to other OpenStreetMap data formats. See https://www.openstreetmap.org/user/fititnt/diary/400329

## Reference vs RFC

- [reference/changeset-1.xml](reference/changeset-1.xml)
  - (...)
- [reference/node-1.xml](reference/node-1.xml)
  - [proposal/node-1.ttl](proposal/node-1.ttl)
- [reference/relation-10000.xml](reference/relation-10000.xml)
  - (...)
  - source: https://www.openstreetmap.org/api/0.6/relation/10000
    - source full: https://www.openstreetmap.org/api/0.6/relation/10000/full
- [reference/way-100.xml](reference/way-100.xml)
  - [proposal/way-100.ttl](proposal/way-100.ttl)

**Public domain code**
- [poc/osmapi2rdfproxy.py](poc/osmapi2rdfproxy.py): early proof of concept to generate the RFC data; not intented for production use, but for test viability. Is a proxy
  - [poc/osmrdf2022.py](poc/osmrdf2022.py): logic of the proof of concept proxy


<!--

./poc/osmdump2rdfcli.py reference/zzz-region-1.xml
./poc/osmdump2rdfcli.py reference/zzz-region-1.xml > poc/tmp/zzz-region-1.ttl
./poc/osmdump2rdfcli.py reference/zzz-region-1.xml > reference/zzz-region-1.ttl
riot --validate poc/tmp/zzz-region-1.ttl

# Turtle to JSON-LD
rdfpipe --output-format=json-ld proposal/zzz-region-1.ttl

# Queries example
arq --query=proposal/query/owl-classes.rq --data=poc/tmp/zzz-region-1.ttl
arq --query=proposal/query/by-name.rq --data=poc/tmp/zzz-region-1.ttl
arq --query=proposal/query/geosparq-example.rq --data=poc/tmp/zzz-region-1.ttl
arq --query=proposal/query/is-admin.rq --data=poc/tmp/zzz-region-1.ttl

# @see https://jena.apache.org/documentation/fuseki2/fuseki-quick-start.html
/opt/apache-jena-fuseki/fuseki-server --file poc/tmp/zzz-region-1.ttl /osm
# http://localhost:3030/#/

curl --output poc/tmp/geosparql_test.rdf https://raw.githubusercontent.com/apache/jena/main/jena-fuseki2/jena-fuseki-geosparql/geosparql_test.rdf

rdfpipe poc/tmp/geosparql_test.rdf > poc/tmp/geosparql_test.rdf.ttl

/opt/apache-jena-fuseki/fuseki-server --file poc/tmp/geosparql_test.rdf /geotest

arq --query=proposal/query/geosparq-example.rq --data=poc/tmp/geosparql_test.rdf

curl --output poc/tmp/geosparql_vocab_all.rdf http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf


# @TODO make tests with https://dbpedia.org/sparql
-->


## Acknowledgments

- Minh Nguyen ([wiki](https://wiki.openstreetmap.org/wiki/User:Minh_Nguyen))
  - [User:Minh Nguyen/Wikidata discussions](https://wiki.openstreetmap.org/wiki/User:Minh_Nguyen/Wikidata_discussions)
- Yuri Astrakhan ([wiki](https://wiki.openstreetmap.org/wiki/User:Yurik))
  - [Sophox](https://wiki.openstreetmap.org/wiki/Sophox)
  - https://wiki.openstreetmap.org/wiki/Sophox#How_OSM_data_is_stored
- (names?)
  - [LinkedGeoData](https://wiki.openstreetmap.org/wiki/LinkedGeoData)

## Disclaimers
<!--
TODO see https://wiki.osmfoundation.org/wiki/Trademark_Policy
-->

OpenStreetMap™ is a trademark of the OpenStreetMap Foundation, and is used with their permission.
This project is not endorsed by or affiliated with the OpenStreetMap Foundation.
