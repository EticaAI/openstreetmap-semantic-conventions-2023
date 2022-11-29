# proposal/shacl/README.md
- @see https://www.w3.org/TR/shacl/

```bash
shacl validate --shapes BR_highways.shacl.ttl --data tests/BR_highways.tdata.ttl
shacl validate --shapes XZ_tags_wikidata.shacl.ttl --data tests/XZ_tags_wikidata-invalid.tdata.ttl
shacl validate --shapes XZ_tags_wikidata.shacl.ttl --data tests/XZ_tags_wikidata-valid.tdata.ttl
```

<!--
- Max speed

- https://www.openstreetmap.org/way/251689884/history
-->
