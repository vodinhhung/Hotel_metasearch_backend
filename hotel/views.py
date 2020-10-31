from django.db.models.expressions import F
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json

from hotel.models import Province, Root, Url, Quality, Info
from hotel.serializers import RootSerializer
from hotel.templates import render_hotel_detail_template

import requests
import base64
from datetime import date

today = date.today() 
date = str(today.year)+str(today.month)+str(today.day)

def get_price(payload):
    USERNAME = 'CFF'
    PASSWORD = 'Q3bohJmeuQcItP9vmhVE'
    msg = f"{USERNAME}:{PASSWORD}"
    t = "Basic " + base64.b64encode(msg.encode('ascii')).decode('ascii')
    url = "https://tripgle.data.tripi.vn/get_price"
    headers = {
    'Authorization': t,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    a = response.json()
    if (a == []) or (a == [[]]):
        return 100000
    else:
        min = 1000000000
        for i in range(0,len(a[0])):
            t = float(a[0][i].get("final_amount"))
            if t<min:
                min = t
        return min

def hotel_list(request):
    if request.method == 'GET':
        a = []
        b = []
        province = Province.objects.all()    
        province_name = request.GET.get('name', None)
        if province_name is not None:
            province = province.filter(name=province_name)
        province_id = province[0].id
        root = Root.objects.filter(province_id = province_id)[:5]
        for i in range(len(root)):
            url = Url.objects.filter(root_id = root[i].id)
            quality = Quality.objects.filter(root_id = root[i].id)
            min_price = 100000000
            d_id = 0
            for j in range(0,len(url)):
                domain_id = str(url[j].domain_id)
                domain_hotel_id = str(url[j].domain_hotel_id)
                params = domain_id+"_"+domain_hotel_id+"_"+date
                payload =  '{"hotel_ids": '+'"'+params+'"'+'}'
                min_price = 100000000
                price = get_price(payload)
                if float(price) < min_price :
                    min_price = price
                    d_id = domain_id 
            a = {
                'id': root[i].id,
                'name': root[i].name,
                'address': root[i].address,
                'star': root[i].star, 
                'logo': root[i].logo,
                'overall_score': quality[0].overall_score, 
                'price': {'domain': d_id, 'value': min_price},
                'review': {
                    "score": 7,
                    "number_of_review": 2529465,
                }
            },
            b.append(a)
        hotel_list_dict = { "items": b,
                            "total_item": len(root) }
        hotel_list_json = json.dumps(hotel_list_dict)
        return HttpResponse(hotel_list_json, content_type="application/json")

def hotel_detail(request, id):
    if request.method == "GET":
        # Get hotel information from databse
        hotel = Root.objects.get(index=id)
        info = Info.objects.get(index=id)
        urls = Url.objects.filter(root_id=id)

        # Customise Json response
        hotel_detail = render_hotel_detail_template(hotel, info, urls)
        hotel_detail_json = json.dumps(hotel_detail)
        return HttpResponse(hotel_detail_json, content_type="application/json")

def province_list(request):
    if request.method == 'GET':
        province = Province.objects.all()    
        name = request.GET.get('name', None)
        if name is not None:
            province = province.filter(name=name)
        
        b = serializers.serialize('json', province)
        return HttpResponse(b, content_type='application/json')
