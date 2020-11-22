from datetime import date
import unidecode
import threading
from time import sleep

from hotel.models import Domain, Like, Url, Quality, Root, User, View, Province, Rank
from hotel.tools.tools import get_price, get_min_price_hotel, get_min_price_hotel_database, update_min_price_domain, update_ranking

today = date.today() 
date = str(today.year)+str(today.month)+str(today.day)

def render_hotel_detail_template(hotel, services, urls, quality, reviews, checkday):
    hotel_detail_dic = {
        'id': hotel.id,
        'name': hotel.name,
        'assets': [hotel.logo],
        'address': hotel.address,
        'description': hotel.description,
        'star': hotel.star,
        'position': {
            'lat': hotel.lat,
            'long': hotel.long,
        },
        'linking': render_url_hotel_detail(urls, checkday),
        'services': render_service_hotel_detail(services),
        'prices': render_price_list_database_hotel_detail(urls),
        # 'prices': render_price_list_hotel_detail(urls),
        'review': render_review_hotel_detail(reviews),
        'facilities': render_facilities_hotel_detail(quality),
    }

    return hotel_detail_dic

def render_url_hotel_detail(urls, checkday):
    lists = []

    for url in urls:
        domain_id = url.domain_id
        domain_name = Domain.objects.get(id=domain_id).name

        if url.url == "-1":
            hotel_id = url.domain_hotel_id
            params = '?chkin={' + checkday[0] + "}&chkout={"+checkday[1]+"}"
            hotel_url = "https://expedia.com.vn/h" + hotel_id + ".Thong-tin-khach-san" + params
            lists.append({
                'type': "Expedia",
                'url': hotel_url,
            })
            continue
        
        if domain_name == "Agoda":
            params = "?Ios=1&checkIn={" + checkday[0] + "}&checkOut={" + checkday[1] +"}"
            hotel_url = "https://agoda.com" + url.url + params
            lists.append({
                'type': "Agoda",
                'url': hotel_url,
            })
            continue
        
        params = "?checkin={" + checkday[0] + "}&checkout={" + checkday[1] + "}"
        hotel_url = url.url + params
        lists.append({
            'type': domain_name,
            'url': hotel_url,
        })
    
    return lists

def render_service_hotel_detail(services):
    lists = []
    
    if services.have_breakfast == 1:
        lists.append({
            'name': 'breakfast',
        })

    if services.is_free_wifi == 1:
        lists.append({
            'name': 'wifi',
        })
    
    if services.have_car_park == 1:
        lists.append({
            'name': 'car_park',
        })
    
    if services.have_airport_transport == 1:
        lists.append({
            'name': 'airport',
        })
    
    if services.have_restaurant == 1:
        lists.append({
            'name': 'restaurant',
        })
    
    if services.have_deposit == 1:
        lists.append({
            'name': 'deposit',
        })
    
    if services.have_baby_service == 1:
        lists.append({
            'name': 'baby_service',
        })
    
    if services.have_bar == 1:
        lists.append({
            'name': 'bar',
        })
    
    if services.have_laundry == 1:
        lists.append({
            'name': 'laundry',
        })
    
    if services.have_tour == 1:
        lists.append({
            'name': 'tour',
        })

    if services.have_spa == 1:
        lists.append({
            'name': 'spa',
        })

    if services.have_pool == 1:
        lists.append({
            'name': 'pool',
        })


    return lists

def render_price_list_hotel_detail(urls):
    price_list = []

    for url in urls:
        domain_id = str(url.domain_id)
        domain_hotel_id = str(url.domain_hotel_id)
        params = domain_id+ "_" +domain_hotel_id+ "_" + date
        payload =  '{"hotel_ids": '+'"'+params+'"'+'}'

        current_price = get_price(payload)
        domain = Domain.objects.get(id=url.domain_id)
        if current_price != float('inf'):
            price_list.append({
                'platform': domain.name,
                'value': current_price
            })
    
    return price_list

def render_price_list_database_hotel_detail(urls):
    price_list = []

    for url in urls:
        domain_id = str(url.domain_id)
        domain = Domain.objects.get(id=url.domain_id)
        if url.min_price != -1:
            price_list.append({
                'platform': domain.name,
                'value': url.min_price
            })
    
    return price_list

def render_facilities_hotel_detail(quality):
    lists = []
    quality_field_list = [
        'cleanliness',
        'meal',
        'location',
        'sleep',
        'room',
        'service',
        'facility',
        'overall'
    ]
    index = 0
    score = 0

    while index < 8:
        if index == 0:
            score = quality.cleanliness_scores
        elif index == 1:
            score = quality.meal_score
        elif index == 2:
            score = quality.location_score
        elif index == 3:
            score = quality.sleep_quality_score
        elif index == 4:
            score = quality.room_score
        elif index == 5:
            score = quality.service_score
        elif index == 6:
            score = quality.facility_score
        elif index == 7:
            score = quality.overall_score

        lists.append({
            'type': quality_field_list[index],
            'score': score,
        })
        
        index += 1
    
    return lists

def render_review_hotel_detail(reviews):
    items = []
    for review in reviews:
        items.append({
            'title': review.title,
            'text': review.text,
            'score': review.score,
        })
    
    return items

def render_search_list_template(text):
    province_items = []
    hotel_items = []
    text = unidecode.unidecode(text).lower().rstrip(' ').lstrip(' ')
    provinces = Province.objects.filter(name_no_accent__contains=text)[0:10]
    roots = Root.objects.filter(name_no_accent__contains=text)[0:10]
    for province in provinces:
        province_items.append({
            'id': province.id,
            'name': province.name
        })

    for root in roots:
        hotel_items.append({
            'id': root.id,
            'name': root.name
        })
    
    search_list_dict = {"province_items": province_items,
                        "hotel_items": hotel_items }
    return search_list_dict

def render_hotel_list_template(root, total):
    items = []
    for i in range(0,root.count()):
        item = render_hotel_template_hotel_list(root[i])
        if item != {}:
            items.append(item)
            
    hotel_list_dict = { "items": items,
                        "total_item": total }
    return hotel_list_dict

def render_hotel_template_hotel_list(root):
    urls = Url.objects.filter(root_id = root.id)
    quality = Quality.objects.filter(root_id = root.id)
    #[min_price, domain_id] = get_min_price_hotel(urls)
    [min_price, domain_id] = get_min_price_hotel_database(urls)
    k = threading.Thread(target=update_ranking, args=[root])
    k.setDaemon(False)
    k.start()
    item = {}

    if (domain_id != -1):
        if str(domain_id) == '2' :
            domain = 'Traveloka'
        elif str(domain_id) == '3' :
            domain = 'Agoda'
        elif str(domain_id) == '5' :
            domain = 'Booking'
        else:
            domain = 'Expedia'

        item = {
            'id': root.id,
            'name': root.name,
            'address': root.address,
            'star': root.star, 
            'logo': root.logo,
            'overall_score': quality[0].overall_score, 
            'price': {
                'domain': domain, 
                'value': min_price
            }
        }

    return item

def render_hotel_list_template_like(user_id):
    user = User.objects.get(social_id = user_id)
    likes = Like.objects.filter(user_id = user.index, status = 1)
    items = []

    for like in likes:
        root_id = like.root_id
        hotel = Root.objects.get(id = root_id)
        hotel_template = render_hotel_template_hotel_list(hotel)
        if hotel_template != {}:
            items.append(hotel_template)
    
    hotel_list_dic = {
        'status': True,
        'items': items,
        'total_item': len(items),
    }

    return hotel_list_dic

# def render_hotel_list_template_view(user_id):
#     user = User.objects.get(social_id = user_id)
#     views = View.objects.filter(user_id = user.index)
#     items = []
#     hotel_list = []

#     for view in views:
#         root_id = view.root_id
#         hotel = Root.objects.get(id = root_id)
#         hotel_template = render_hotel_template_hotel_list(hotel)
#         if hotel_template != {}:
#             items.append(hotel_template)
    
#     if len(items) > 10:
#         hotel_list = items[::-1][:10]
#     else:
#         hotel_list = items[::-1]
    
#     hotel_list_dic = {
#         'status': True,
#         'items': hotel_list,
#         'total_item': len(items),
#     }

#     return hotel_list_dic

def render_hotel_list_template_view(user_id):
    user = User.objects.get(social_id = user_id)
    views = View.objects.filter(user_id = user.index)
    store = {}
    items = []

    for view in views[::-1]:
        if len(items) > 10:
            break
        
        root_id = view.root_id
        if root_id not in store:
            store[root_id] = True
            hotel = Root.objects.get(id = root_id)
            hotel_template = render_hotel_template_hotel_list(hotel)
            if hotel_template != {}:
                items.append(hotel_template)
    
    hotel_list_dic = {
        'status': True,
        'items': items,
        'total_item': len(items),
    }

    return hotel_list_dic

def render_search_recommend():
    root = Root.objects.all().order_by('-rank__rank_score')[0:10]
    hotel = []
    for i in range(0,len(root)):
        t = {"id": root[i].id, "name": root[i].name}
        hotel.append(t)
    search_list_dict = {"province_items":  [{ "id": 11, "name": "Hà Nội" },
                                        { "id": 33, "name": "Hồ Chí Minh" },
                                        { "id": 1, "name": "Thừa Thiên - Huế" },
                                        { "id": 50, "name": "Đà Nẵng" },
                                        { "id": 16, "name": "Thanh Hóa" }],
                    "hotel_items": hotel}
    return search_list_dict