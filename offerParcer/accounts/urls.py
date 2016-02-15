"""
Definition of urls for offerParcer.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm
from accounts.forms import AuthenticationFormCustom
from offers.models import Offer


urlpatterns = patterns('',

    url(r'^(?P<username>(?!(signout|signup|signin)/)[\@\.\w-]+)/$', 'userena.views.profile_detail',
               {
                   'extra_context': { 'Table': Offer.objects.values('title', 'category', 'payout', 'countries', 'linkOffer').order_by().distinct(), }
               }, name='userena_profile_detail'),

    url(r'^', include('userena.urls')),
)
