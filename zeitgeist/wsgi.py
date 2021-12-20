"""
WSGI config for zeitgeist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from dotenv import load_dotenv
ENV_PATH = '../../../virtualenv/Z22/.env'
load_dotenv(ENV_PATH)

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home3/zeitgeist/Z22/Zeitgeist22')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zeitgeist.settings')

application = get_wsgi_application()
