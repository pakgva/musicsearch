# musicsearch

Python + GraphQL + Postgres

Featuring:

- Docker v1.12.5
- Docker Compose v1.8.1
- Python 2.7

### Instructions for Linux 

1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Load fixtures - `docker-compose run web /usr/local/bin/python manage.py loaddata tracks`
1. Go to http://localhost:8000/graphql 
