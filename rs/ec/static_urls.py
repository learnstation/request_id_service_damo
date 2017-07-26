# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['GET'])
def index_view(request):
    return render(request, 'index.html')


urlpatterns = [
    url(r'^$', index_view, name='index_view')
]
