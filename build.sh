#!/usr/bin/env bash
set -o errexit

py -m pip install --upgrade pip
pip install -r requirements.txt

py manage.py collectstatic --no-input
py manage.py migrate