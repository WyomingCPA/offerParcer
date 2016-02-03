# coding: utf-8

from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=128, blank=True)
    category = models.CharField(max_length=128, blank=True)
    payout = models.IntegerField(null=True, blank=True)
    countries = models.CharField(max_length=128, blank=True)
    linkOffer = models.CharField(max_length=128, blank=True)
    link = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return self.title








