# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    calibre = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    power reserve = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    jewels = models.CharField(max_length=255, null=True, blank=True)
    certifications = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Brand(models.Model):

    #__Brand_FIELDS__
    brand = models.CharField(max_length=255, null=True, blank=True)
    collection = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    model reference = models.CharField(max_length=255, null=True, blank=True)
    bracelet = models.CharField(max_length=255, null=True, blank=True)
    calibre = models.CharField(max_length=255, null=True, blank=True)
    calibre reference = models.CharField(max_length=255, null=True, blank=True)

    #__Brand_FIELDS__END

    class Meta:
        verbose_name        = _("Brand")
        verbose_name_plural = _("Brand")


class Case Features(models.Model):

    #__Case Features_FIELDS__
    case reference = models.CharField(max_length=255, null=True, blank=True)
    case size = models.IntegerField(null=True, blank=True)
    material = models.CharField(max_length=255, null=True, blank=True)
    bezel = models.CharField(max_length=255, null=True, blank=True)
    bezel material = models.CharField(max_length=255, null=True, blank=True)
    crystal = models.CharField(max_length=255, null=True, blank=True)
    dial = models.CharField(max_length=255, null=True, blank=True)
    hour markers = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Case Features_FIELDS__END

    class Meta:
        verbose_name        = _("Case Features")
        verbose_name_plural = _("Case Features")


class Bracelet(models.Model):

    #__Bracelet_FIELDS__
    bracelet reference = models.CharField(max_length=255, null=True, blank=True)
    material = models.CharField(max_length=255, null=True, blank=True)
    total links = models.CharField(max_length=255, null=True, blank=True)
    clasp = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Bracelet_FIELDS__END

    class Meta:
        verbose_name        = _("Bracelet")
        verbose_name_plural = _("Bracelet")



#__MODELS__END
