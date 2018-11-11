# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:53:56 2018

@author: kim
"""
import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def door(request):
    return render(request,"dhtG.html")

def parser(request):
    global hum,tem
    if request.method=="POST":
        data=json.loads(request.body)
        hum=data['hum']
        tem=data['tem']
    return HttpResponse("Done")

def browser(request):
    global hum,tem
    data={'hum':hum,'tem':tem}
    return JsonResponse(data)