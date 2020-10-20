from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
import json
from hotel.models import Province, Root, Url

def hotel_list(request):
    a = Province.objects.all()
    b = serializers.serialize('json', a)
    return HttpResponse(b, content_type='application/json')

def hotel_detail(request, pk):
    if request.method == 'GET':
        a = Root.objects.filter(province_id = pk)[:5]
        b = serializers.serialize('json', a)
        return HttpResponse(b, content_type='application/json')

def province_list(request):
    if request.method == 'GET':
        province = Province.objects.all()    
        name = request.GET.get('name', None)
        if name is not None:
            province = province.filter(name=name)
        
        b = serializers.serialize('json', province)
        return HttpResponse(b, content_type='application/json')