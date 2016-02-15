# coding: utf-8

from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    payout = models.IntegerField(null=True, blank=True)
    countries = models.CharField(max_length=128, blank=True, null=True)
    linkOffer = models.CharField(max_length=128, blank=True, null=True)
    link = models.CharField(max_length=128, blank=True, null=True, default = '')

    def __unicode__(self):
        return self.title








