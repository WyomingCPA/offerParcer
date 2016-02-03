from django.contrib import admin
from .models import Offer

# Register your models here
class OffersAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'payout', 'countries', 'linkOffer', 'link', )

admin.site.register(Offer, OffersAdmin)

