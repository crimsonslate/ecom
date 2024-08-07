#!/usr/bin/bash

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py tailwind install
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
