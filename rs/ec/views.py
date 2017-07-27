#! /usr/bin/env python
# coding=utf-8
# author: jack-zh

import requests
import random
import json

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import RequestRecord


def response_func(result=None, status=2000, message="", module="aera"):
    return Response({
        "status": status,
        "module": module,
        "message": message,
        "result": result
    })


@api_view(['POST'])
@renderer_classes((JSONRenderer, ))
def record_view(request):
    req_data = request.data
    print req_data
    obj_data = req_data
    obj_id = RequestRecord.create_obj(**obj_data)
    return response_func(result={"id": obj_id})


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test1_view(request):
    req_data = request.query_params.dict()
    a("test2", req_data)
    a("test3", req_data)
    a("test4", req_data)
    return response_func(result=req_data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test2_view(request):
    req_data = request.query_params.dict()
    a("test3", req_data)
    a("test4", req_data)
    return response_func(result=req_data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test3_view(request):
    req_data = request.query_params.dict()
    a("test4", req_data)
    return response_func(result=req_data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test4_view(request):
    req_data = request.query_params.dict()
    return response_func(result=req_data)


def a(path, data):
    url = "http://127.0.0.1:8000/api/nuri/aere/" + path + "/"
    data.update({
        'path': path,
        'random': random.randint(0, 99)
    })
    requests.get(url, params=data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def get_record_view(request):
    parent_id = None
    parent_record_id = request.query_params.dict().get("parent_record_id")
    if parent_record_id:
        record_db = RequestRecord.objects.filter(id=parent_record_id).first()
        parent_id = record_db.current_id
    back_dbs = RequestRecord.objects.filter(parent_id=parent_id).order_by("index_num").all()
    result = []
    for o in back_dbs:
        obj = model_to_dict(o)
        result.append(obj)
    return response_func(result=result)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def get_request_view(request):
    record_id = request.query_params.dict().get("id")
    record_db = RequestRecord.objects.filter(id=record_id).first()
    request_data = record_db.request_data
    result = ""
    if request_data:
        print request_data
        print json.loads(request_data)
        result = json.dumps(json.loads(request_data), indent=2)
    return response_func(result=result)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def get_response_view(request):
    record_id = request.query_params.dict().get("id")
    record_db = RequestRecord.objects.filter(id=record_id).first()
    response_data = record_db.response_data
    result = ""
    if response_data:
        result = json.dumps(json.loads(response_data), indent=2)
    return response_func(result=result)
