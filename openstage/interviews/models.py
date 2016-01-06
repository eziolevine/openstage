import datetime

from django.db import models
from django.conf import settings
from django.contrib import admin

from embed_video.fields import EmbedVideoField
from publisher.models import PublisherModel
from publisher.admin import PublisherAdmin


class DateMixin(models.Model):
    date_added = models.DateTimeField(default=datetime.datetime.now)
    date_modified = models.DateTimeField(default=datetime.datetime.now)

    def save(self):
        self.date_modified = datetime.datetime.now()
        super(DateMixin, self).save()

    class Meta:
        abstract = True


class Inerview(PublisherModel, DateMixin):
    slug = models.SlugField(blank=False)
    video = EmbedVideoField()  
    title = models.CharField(max_length=500, blank=False)
    interviewer =  models.ForeignKey(settings.AUTH_USER_MODEL)
    interviewee = models.CharField(max_length=500, blank=False)
    body = models.TextField(blank=False)
    is_active = models.BooleanField(default=True)

    @models.permalink
    def get_absolute_url(self):
        '''
        return the object absloute url
        '''
        return ('inteview_detail', (), {'pk': self.pk})


class InerviewAdmin(PublisherAdmin):
    pass


admin.site.register(Inerview, InerviewAdmin)

    
