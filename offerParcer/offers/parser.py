import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append(r'../offerParcer/settings.py')

import django
django.setup()