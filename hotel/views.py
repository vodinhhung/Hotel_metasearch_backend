from django.db.models.expressions import F
from django.http import HttpResponse
from django.core import serializers
import json
from hotel.models import Province, Root, Url, Quality, Info
from hotel.serializers import RootSerializer
from hotel.templates import render_hotel_detail_template, render_hotel_list_template
from hotel.tools import get_price, get_min_price_domain

def hotel_list(request):
    if request.method == 'GET':
        #get params (destination, page)    
        province_name = request.GET.get('destination', None)
        if province_name is not None:
            province = Province.objects.filter(name=province_name)
        province_id = province[0].id
        page = request.GET.get('page', None)
        if page is not None:
            num_p = (int(page)-1)*5
        else:
            num_p = 0
        
        # Render Json response
        total = len(Root.objects.filter(province_id = province_id))
        root = Root.objects.filter(province_id = province_id)[num_p:(num_p+5)]
        hotel_list_dict = render_hotel_list_template(root, total)
        hotel_list_json = json.dumps(hotel_list_dict)
        
        return HttpResponse(hotel_list_json, content_type="application/json")

def hotel_detail(request, id):
    if request.method == "GET":
        # Get hotel information from databse
        hotel = Root.objects.get(id=id)
        info = Info.objects.get(root_id=id)
        urls = Url.objects.filter(root_id=id)
        quality = Quality.objects.get(root_id=id)

        # Customise Json response
        hotel_detail = render_hotel_detail_template(hotel, info, urls, quality)
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
