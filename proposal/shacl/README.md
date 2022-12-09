# proposal/shacl/README.md
- @see https://www.w3.org/TR/shacl/

```bash
shacl validate --shapes BR_highways.shacl.ttl --data tests/BR_highways.tdata.ttl
shacl validate --shapes XZ_tags_wikidata.shacl.ttl --data tests/XZ_tags_wikidata-invalid.tdata.ttl
shacl validate --shapes XZ_tags_wikidata.shacl.ttl --data tests/XZ_tags_wikidata-valid.tdata.ttl
```


```bash
cd ../../
shacl validate --shapes proposal/shacl/BR_highways.shacl.ttl --data poc/tmp/STP~test.osm.ttl
shacl validate --shapes proposal/shacl/XZ_tags_wikidata.shacl.ttl --data poc/tmp/STP~test.osm.ttl
shacl validate --shapes proposal/shacl/XZ_relation_empty.shacl.ttl --data proposal/shacl/tests/XZ_relation_empty.tdata.ttl
```

<!--
- Max speed

- https://www.openstreetmap.org/way/251689884/history
-->
