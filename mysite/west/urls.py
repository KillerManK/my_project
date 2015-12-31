# coding=utf-8

from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
                       url(r'^$', 'west.views.first_page'),
                       )
