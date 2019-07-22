@echo off

IF %1 == terminal (
    docker-compose run --rm web /bin/bash
)

IF %1 == start (
    docker-compose up
)

IF %1 == stop (
    docker-compose stop
)

IF %1 == build (
    docker-compose build
)

IF %1 == make-migrations (
    docker-compose run --rm web ./manage.py makemigrations
)

IF %1 == migrate (
    docker-compose run --rm web ./manage.py migrate
)

IF %1 == create-superuser (
    docker-compose run --rm web ./manage.py createsuperuser
)

IF %1 == refresh-db (
    docker-compose run --rm web bash refresh-db.sh
)

if %1 == save-superuser (
    docker-compose run --rm web ./manage.py dumpdata --indent 4 auth.User  -o common/fixtures/superuser.json
)

if %1 == load-superuser (
    docker-compose run --rm web ./manage.py loaddata superuser
)

if %1 == load-test-data (
    docker-compose run --rm web ./manage.py load_test_data
)