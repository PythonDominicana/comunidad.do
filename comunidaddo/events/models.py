from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Event(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from='title', blank=True)
    created = models.DateTimeField(
        auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(
        auto_now=True, editable=False)
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(
        upload_to="events", null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='events',
        on_delete=models.CASCADE)
    region = models.ForeignKey(
        "region", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return f"/events/{self.slug}"


    def get_update_url(self):
        return f"/events/update/{self.slug}"


class Region(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('events_region_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('events_region_update', args=(self.slug,))


