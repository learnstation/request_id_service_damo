# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.shortcuts import render
from rest_framework.decorators import api_view
from .views import record_view
from .views import get_record_view
from .views import get_request_view
from .views import get_response_view


@api_view(['GET'])
def index_view(request):
    return render(request, 'index.html')


urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^record$', record_view, name='record_view'),
    url(r'^data$', get_record_view, name='get_record_view'),
    url(r'^request_data$', get_request_view, name='get_request_view'),
    url(r'^response_data$', get_response_view, name='get_response_view')
]
