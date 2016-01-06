
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls.static import static
import  openstage.interviews.views as views

urlpatterns = [
    url(r'^$', views.InterviewListView.as_view(), name="home"),
    url(r'^interview/(?P<pk>[\d]+)$', views.InterviewView.as_view(), name="inteview_detail"),
]
