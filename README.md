# Publications API

A Django REST API to serve publication data, for both papers and data sets.

## Setup

After cloning this repo, you should be able to get a local copy of this up and
running with:

```bash
docker-compose run api python manage.py migrate
docker-compose run api python manage.py createsuperuser
docker-compose up
```

Visit `http://localhost:8000/admin/` to log into Django's built in CMS.

You can browse the API by just visiting `http://localhost:8000/`.

## API Documentation

* `/` - returns links to available resource types.
* `/publications/` - returns all publications.
* `/publications/?type=paper` - returns only papers.
* `/publications/?type=data` - returns on data sets.
