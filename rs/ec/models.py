# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RequestRecord(models.Model):
    global_id = models.CharField(max_length=32)
    parnet_id = models.CharField(max_length=32, blank=True, null=True)
    current_id = models.CharField(max_length=32)
    deep_num = models.IntegerField()
    index_num = models.IntegerField()
    http_status = models.IntegerField()
    nscloud_status = models.IntegerField()
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=128)
    module = models.CharField(max_length=45)
    remote_ip = models.CharField(max_length=64)
    request_data = models.TextField()
    response_data = models.TextField()
    taking = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'request_record'
