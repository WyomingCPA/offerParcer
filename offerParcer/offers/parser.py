import os
import sys


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append(r'C:\Users\montanaPython\Documents\Visual Studio 2013\Projects\offerParcer\offerParcer\offerParcer\settings.py')

import django
from models import Offer
django.setup()

test = Offer.objects.get(pk=1)