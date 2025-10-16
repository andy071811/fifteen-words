#!/bin/bash

python manage.py migrate
python -m gunicorn --bind 0.0.0.0:8000 fifteen_words_project.wsgi:application