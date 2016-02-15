from django.shortcuts import render, render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django_tables2   import RequestConfig
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from offers.models import Offer
from .filters import OfferFilter

@login_required(login_url='/accounts/login/')
def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'dashboard/index.html',
        context_instance = RequestContext(request,
        {
            'Table': Offer.objects.values('title', 'category', 'payout', 'countries', 'linkOffer').order_by().distinct(),
        })
    ) 


@login_required(login_url='/accounts/login/')
def table_pagin(request):
    filter = OfferFilter(request.GET, queryset=Offer.objects.values('title', 'category', 'payout', 'countries', 'linkOffer').order_by().distinct())
    table_value_list = filter 

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    paginator = Paginator(table_value_list, 100, request = request) # Show 25 contacts per page

    try:
        page_offer = paginator.page(page)
    except PageNotAnInteger:
        page_offer = paginator.page(1)
    except EmptyPage:
        page_offer = paginator.page(paginator.num_pages)

    return render_to_response('dashboard/index.html', {"Table": page_offer, 'filter' : filter,})




