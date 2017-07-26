# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from ec.views import test1_view
from ec.views import test2_view
from ec.views import test3_view
from ec.views import test4_view


urlpatterns = [
    url(r'^test1/$', test1_view, name='test1_view'),
    url(r'^test2/$', test2_view, name='test2_view'),
    url(r'^test3/$', test3_view, name='test3_view'),
    url(r'^test4/$', test4_view, name='test4_view')
]
