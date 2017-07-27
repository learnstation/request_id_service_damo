# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def field_names(cls):
    _fields = cls._meta.fields
    names = []
    for f in _fields:
        names.append(f.name)
    return names


class RequestRecord(models.Model):
    global_id = models.CharField(max_length=32)
    parent_id = models.CharField(max_length=32, blank=True, null=True)
    current_id = models.CharField(max_length=32)
    deep_num = models.IntegerField()
    index_num = models.IntegerField()
    http_status = models.IntegerField()
    nscloud_status = models.IntegerField()
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=128)
    module = models.CharField(max_length=45)
    api_type = models.CharField(max_length=16)
    remote_ip = models.CharField(max_length=64)
    request_data = models.TextField()
    response_data = models.TextField()
    taking = models.IntegerField()
    child_num = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'request_record'

    @classmethod
    def create_obj(cls, **kwargs):
        """
            添加服务对象
        :return:
        """
        fields = field_names(cls)
        cs_dict = {}
        for key in fields:
            cs_dict[key] = kwargs.get(key, None)

        obj = RequestRecord(**cs_dict)
        try:
            obj.save()
            return obj.id
        except Exception, err:
            print err, "save err"
