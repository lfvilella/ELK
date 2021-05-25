# Curator

Elasticsearch Curator helps you curate or manage your indices.

## Usage

If you want to include the Curator extension, run Docker Compose from the root of the repository with an additional
command line argument referencing the `curator-compose.yml` file:

```bash
$ docker-compose -f docker-compose.yml -f extensions/curator/curator-compose.yml up
```

All configuration files are available in the `config/` directory.

## Documentation

[Curator Reference](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/index.html)
