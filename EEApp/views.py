# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json

@api_view(["POST"])
def uploadLogs(request):
    try:
        if request.method == 'POST' and request.FILES['logFile']:
            logFile = request.FILES['logFile']
            fs = FileSystemStorage("/home/Documents/")
            logfilename = fs.save(logFile.name, logFile)
            uploaded_file_url = fs.url(logfilename)
            return JsonResponse("File Uploaded Successfully "+uploaded_file_url,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
# Create your views here.
