#! /bin/bash

rm -rf concertainly/migrations
rm db.sqlite3
python manage.py makmigrations concertainly
python manage.py migrate