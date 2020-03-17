#!/bin/bash

source venv/bin/activate

python -m pip install pytest

pip3 install Flask

pip3 install flask_mysqldb

pip3 install flask-bootstrap

pip3 install flask-ckeditor

pip3 install Werkzeug

pip3 install Flask-WTF

pip3 install urllib3

python3 -m pip install coverage

source ~/.bashrc

python3 /var/lib/jenkins/workspace/SFIA/app.py

#gunicorn --workers=4 --bind=0.0.0.0:5000 app:app
