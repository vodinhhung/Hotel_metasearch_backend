from django.db.models.expressions import F
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q

from hotel.models import Province, Root, Url, Quality, Info
from hotel.serializers import RootSerializer
from hotel.templates import render_hotel_detail_template, render_hotel_list_template, render_hotel_list_template_like, render_hotel_list_template_view, render_search_list_template
from hotel.tools.tools import hotel_list_filter_facility
from hotel.tools.login_tools import call_facebook_api, save_user_database, check_token_user
from hotel.tools.user_tools import save_like, save_view

def hotel_list(request):
    if request.method == 'GET':
        #filter with params (destination, page, wifi, ...)    
        province_name = request.GET.get('destination', None)
        if province_name is not None:
            province = Province.objects.filter(name=province_name)
        province_id = province[0].id
        root = Root.objects.filter(province_id = province_id)
        star = request.GET.get('star', None)
        if star is not None:
            root = root.filter(star=int(star))
        min_price = request.GET.get('PriceFrom', None)
        max_price = request.GET.get('PriceTo', None)
        if min_price is not None:
            root = root.filter(min_price_domain__gte = min_price)
        if max_price is not None:
            root = root.filter(min_price_domain__lte = max_price)
        facility = request.GET.get('facility', None)
        root = hotel_list_filter_facility(root,facility)
        sort = request.GET.get('sort', None)
        if sort is not None:
            root = root.filter(~Q(min_price_domain = -1))
            if str(sort) == 'asc':
                root = root.order_by('min_price_domain')
            else:
                root = root.order_by('-min_price_domain')
        total = root.count()
        page = request.GET.get('page', None)
        if page is not None:
            num_p = (int(page)-1)*5
        else:
            num_p = 0
        
        # Render Json response
        root = root[num_p:(num_p+5)]
        hotel_list_dict = render_hotel_list_template(root, total)
        hotel_list_json = json.dumps(hotel_list_dict)
        return HttpResponse(hotel_list_json, content_type="application/json")

def hotel_search(request):
    if request.method == 'GET':
        #filter with params search    
        text = request.GET.get('text', None)
        province_items = []
        hotel_items = []
        if text is not None:
            search_list_dict = render_search_list_template(text)
        else:
            search_list_dict = {"province_items":  [{ "id": 11, "name": "Hà Nội" },
                                                    { "id": 33, "name": "Hồ Chí Minh" },
                                                    { "id": 1, "name": "Thừa Thiên - Huế" },
                                                    { "id": 50, "name": "Đà Nẵng" },
                                                    { "id": 16, "name": "Thanh Hóa" }],
                                "hotel_items": []}
        search_list_json = json.dumps(search_list_dict)
        return HttpResponse(search_list_json, content_type="application/json")

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

@csrf_exempt
def login_user(request):
    response = {}
    if request.method == 'POST':
        request_body = json.loads(request.body)
        token = request_body['access_token']
        facebook_response = call_facebook_api(token)
        if not facebook_response[0]:
            response = {
                'status': False,
                'user': {},
                'access_token': "",
            }
        else:
            access_token = save_user_database(facebook_response[1], 1)
            response = {
                'status': True,
                'user': facebook_response[1],
                'access_token': access_token,
            }

    return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt
def hotel_like(request):
    response = {}
    if request.method == "POST":
        user_id, is_valid = check_token_user(request.headers.get('Authorization'))
        request_body = json.loads(request.body)
        hotel_id = request_body['hotel_id']

        if is_valid:
            save_success, action = save_like(hotel_id, user_id)
            response = {
                'status': save_success,
                'action': ['Unlike', 'Like'][action == 1]
            }
        else:
            response = {
                'status': False,
            }
    elif request.method == "GET":
        user_id, is_valid = check_token_user(request.headers.get('Authorization'))
        if is_valid:
            response = render_hotel_list_template_like(user_id)
        else:
            response = {
                'status': False,
            }
    
    return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt
def hotel_view(request):
    response = {}
    if request.method == "POST":
        user_id, is_valid = check_token_user(request.headers.get('Authorization'))
        request_body = json.loads(request.body)
        hotel_id = request_body['hotel_id']

        if is_valid:
            save_view_status = save_view(hotel_id, user_id)
            response = {
                'status': save_view_status,
            }
        else:
            response = {
                'status': False,
            }
    else:
        user_id, is_valid = check_token_user(request.headers.get('Authorization'))
        if is_valid:
            response = render_hotel_list_template_view(user_id)
        else:
            response = {
                'status': False
            } 
    
    return HttpResponse(json.dumps(response), content_type='application/json')