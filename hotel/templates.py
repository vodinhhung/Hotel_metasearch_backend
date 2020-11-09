from datetime import date

from hotel.models import Domain, Like, Url, Quality, Root, User, View
from hotel.tools.tools import get_price, get_min_price_hotel

today = date.today() 
date = str(today.year)+str(today.month)+str(today.day)

def render_hotel_detail_template(hotel, services, urls, quality):
    hotel_detail_dic = {
        'id': hotel.id,
        'name': hotel.name,
        'assets': [hotel.logo],
        'address': hotel.address,
        'description': hotel.description,
        'rating': {
            'value': hotel.star,
        },
        'position': {
            'lat': hotel.lat,
            'long': hotel.long,
        },
        'linking': render_url_hotel_detail(urls),
        'services': render_service_hotel_detail(services),
        'prices': render_price_list_hotel_detail(urls),
        'review': {
            'score': 7,
            'number_review': 234548,
        },
        'facilities': render_facilities_hotel_detail(quality),
    }

    return hotel_detail_dic

def render_url_hotel_detail(urls):
    lists = []

    for url in urls:
        domain_id = url.domain_id
        domain_name = Domain.objects.get(id=domain_id).name

        if url.url == "-1":
            hotel_id = url.domain_hotel_id
            hotel_url = "https://expedia.com.vn/h" + hotel_id + ".Thong-tin-khach-san"
            lists.append({
                'type': "Expedia",
                'url': hotel_url,
            })
            continue
        
        if domain_name == "Agoda":
            hotel_url = "https://agoda.com" + url.url
            lists.append({
                'type': "Agoda",
                'url': hotel_url,
            })
            continue
        
        lists.append({
            'type': domain_name,
            'url': url.url,
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
    [min_price, domain_id] = get_min_price_hotel(urls)
    item = {}

    if (domain_id != -1):
        if domain_id == '2' :
            domain = 'Traveloka'
        elif domain_id == '3' :
            domain = 'Agoda'
        elif domain_id == '5' :
            domain = 'Booking'
        else:
            domain = 'None'

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

def render_hotel_list_template_view(user_id):
    user = User.objects.get(social_id = user_id)
    views = View.objects.filter(user_id = user.index)
    items = []

    for view in views:
        root_id = view.root_id
        hotel = Root.objects.get(id = root_id)
        hotel_template = render_hotel_template_hotel_list(hotel)
        if hotel_template != {}:
            items.append(hotel_template)
    
    hotel_list_dic = {
        'status': True,
        'items': items[::-1],
        'total_item': len(items),
    }

    return hotel_list_dic