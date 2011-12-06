import os
import sys

sys.path.append("/var/django/Iris/")
sys.path.append("/var/django/Iris/irisserver")
os.environ['DJANGO_SETTINGS_MODULE'] = 'irisserver.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

