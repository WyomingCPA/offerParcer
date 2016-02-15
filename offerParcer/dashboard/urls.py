from django.conf.urls import patterns, url, include
from offers.models import Offer


urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.table_pagin', name='index'),
    #url(r'^$', 'django_filters.views.object_filter', {'model': Offer, 'template_name' : 'dashboard/index.html'}),
) 
 