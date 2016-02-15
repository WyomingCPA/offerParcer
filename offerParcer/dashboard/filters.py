import django_filters
from offers.models import Offer


class OfferFilter(django_filters.FilterSet):
       
    payout = django_filters.RangeFilter()

    class Meta:
        model = Offer
        fields = ['payout', ]