py webApp/manage.py makemigrations
py webApp/manage.py sync_cassandra
py webApp/manage.py migrate --database default
py webApp/manage.py runserver
