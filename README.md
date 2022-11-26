## [EARLY DRAFT] Request for Feedback: OpenStreetMap RDF Schema 2022
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
- [proxy/osmapi2rdfproxy.py](proxy/osmapi2rdfproxy.py): early proof of concept to generate the RFC data; not intented for production use, but for test viability. Is a proxy
  - [proxy/osmrdf2022.py](proxy/osmrdf2022.py): logic of the proof of concept proxy

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
