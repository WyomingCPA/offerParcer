import django_tables2 as tables
from offers.models import Offer
from django.forms import ModelForm

class OfferTable(tables.Table):

    title = tables.Column(attrs={'class': 'gradeA even'})
    category = tables.Column()
    payout = tables.Column()
    countries = tables.Column()
    linkOffer = tables.Column()
    link = tables.Column()
   

    class Meta:
        model = Offer
        attrs = {'class': 'table table-striped table-bordered table-hover dataTables-example dataTable'}      
        exclude = () 