import os
import sys
sys.path.append('/var')
sys.path.append('/var/me2echelon')
os.environ['DJANGO_SETTINGS_MODULE'] = 'me2echelon.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
