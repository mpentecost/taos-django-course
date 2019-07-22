psql -h db -U postgres -d postgres -c 'drop database fotogram'
psql -h db -U postgres -d postgres -c 'create database fotogram'
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata superuser
