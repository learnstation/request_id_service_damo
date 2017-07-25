# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from api.views import AddLogViews


urlpatterns = patterns(
    'ec.views',
    url(r'^add/$', AddLogViews.as_view()),
)
