from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
def data(request):
    emp_data = {
        'eno':10,
        'ename':'ss',
        'esal' :124562,
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type = 'application/json')



# class basd view

from django.views.generic import View

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
            'eno':100,
            'ename':'ss',
            'esal':1000,
        }
        return JsonRespose(rem_data)