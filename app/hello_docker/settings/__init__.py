"""
this is a django-split-settings main file.

default environment is 'devlopment'.

To change settings file:
'DJANGO_ENV=production python manage.py runserver'
"""

from split_settings.tools import optional, include
from os import environ
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = environ.get("DJANGO_ENV") or "development"

base_settings = [
    "components/base.py",
    "components/database.py",
    "components/rq.py",
    "components/emails.py",
    "environments/%s.py" % ENV,
    optional("environments/local.py"),
]

# include settings
include(*base_settings)
