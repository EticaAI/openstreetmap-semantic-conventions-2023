# Semantic Conventions for OpenStreetMap™ 2023
**[Request for Feedback] Semantic Conventions for OpenStreetMap™ 2023. Mappings from common file formats to RDF, and other considerations**

> This initial draft was based on discussions from [Emerson Rocha 400329 Diary](https://www.openstreetmap.org/user/fititnt/diary/400329).

## The conventions

Please visit <https://eticaai.github.io/openstreetmap-semantic-conventions-2023/> for the lastest editor draft.

The structure for the directory is:
- [reference/](reference/): reference files
- [proposal/](proposal/): Proposal files in RDF with  [Turtle serialization](https://www.w3.org/TR/turtle/).
  - [proposal/shacl](proposal/shacl/): proof of convept of [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) usable with the proposed RDF encoding.
  - [proposal/query](proposal/query/): proof of convept of [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) usable with the proposed RDF encoding.
- [poc/](poc/): public domain scripts to convert between the formats

### SHACL Tutorial <sup>new!</sup>

Please visit <https://eticaai.github.io/openstreetmap-semantic-conventions-2023/shacl-tutorial/>.

## Become an editor

1. The hard requeriment is know the basics of <https://respec.org/docs/> to edit the [index.html](index.html) file without help.
2. Either solid experience with OpenStreetMap (preferable tagging **or** with files used to exchange data) **or** solid experience with [Semantic Web](https://www.w3.org/standards/semanticweb/) (does **not** need to be both) is expected.
3. Be open to receive feedback from suggestions. Being an editor does not mean being an author.
4. Get in contact and ask.

<!--
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
-->

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

curl --output poc/tmp/tagfinder_thesaurus.rdf http://tagfinder.herokuapp.com/tagfinder_thesaurus.rdf
rdfpipe --output-format=longturtle poc/tmp/tagfinder_thesaurus.rdf > poc/tmp/tagfinder_thesaurus.rdf.ttl

# @TODO make tests with https://dbpedia.org/sparql
# @TODO maybe use as example (because of implies)
#  - https://wiki.openstreetmap.org/wiki/Item:Q4980
#  - https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway

/opt/Protege-5.5.0/run.sh
-->


## Acknowledgments

- Minh Nguyen ([wiki](https://wiki.openstreetmap.org/wiki/User:Minh_Nguyen))
  - [User:Minh Nguyen/Wikidata discussions](https://wiki.openstreetmap.org/wiki/User:Minh_Nguyen/Wikidata_discussions)
- Yuri Astrakhan ([wiki](https://wiki.openstreetmap.org/wiki/User:Yurik))
  - [Sophox](https://wiki.openstreetmap.org/wiki/Sophox)
  - https://wiki.openstreetmap.org/wiki/Sophox#How_OSM_data_is_stored
- (names?)
  - [LinkedGeoData](https://wiki.openstreetmap.org/wiki/LinkedGeoData)
- (names?)
  - <http://tagfinder.herokuapp.com/tagfinder_thesaurus.rdf>

## Disclaimers
<!--
TODO see https://wiki.osmfoundation.org/wiki/Trademark_Policy
-->

OpenStreetMap™ is a trademark of the OpenStreetMap Foundation, and is used with their permission.
This project is not endorsed by or affiliated with the OpenStreetMap Foundation.

## License

Public domain
