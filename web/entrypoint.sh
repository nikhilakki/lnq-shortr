# Copyright (c) 2022 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

python manage.py migrate --no-input
python manage.py collectsatic --no-input
gunicorn django_project.wsgi:application --bind 0.0.0.0:8000