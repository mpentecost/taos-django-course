#!/usr/bin/env bash

case $1 in
	start)
		docker-compose up
		;;
    stop)
        docker-compose down
        ;;
    build)
        docker-compose build
        ;;
    terminal)
        docker-compose run --rm web bash
        ;;
    migrate)
        docker-compose run --rm web ./manage.py makemigrations
        docker-compose run --rm web ./manage.py migrate
        ;;
    create-superuser)
		docker-compose run --rm web ./manage.py createsuperuser
		;;
    refresh-db)
        docker-compose run --rm web bash refresh-db.sh
        ;;
    save-superuser)
        docker-compose run --rm web ./manage.py dumpdata --indent 4 auth.User  -o common/fixtures/superuser.json
        ;;
    load-superuser)
        docker-compose run --rm web ./manage.py loaddata superuser
        ;;
    load-test-data)
        docker-compose run --rm web ./manage.py load_test_data
        ;;
esac