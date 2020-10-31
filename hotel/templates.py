import json

from hotel.models import Domain

def render_hotel_detail_template(hotel, services, urls):
    hotel_detail_dic = {
        'id': hotel.index,
        'name': hotel.name,
        'assets': [hotel.logo],
        'address': hotel.address,
        'description': hotel.description,
        'rating': {
            'value': hotel.star,
        },
        'linking': render_url_hotel_detail(urls),
        'services': render_service_hotel_detail(services),
        'review': {
            'score': 7,
            'number_review': 234548,
        }
    }

    return hotel_detail_dic

def render_url_hotel_detail(urls):
    lists = []

    for url in urls:
        # If there is no url for this domain, continue loop
        if url.url == "-1":
            continue
    
        domain_id = url.domain_id
        domain_name = Domain.objects.get(id=domain_id).name
        lists.append({
            'type': domain_name,
            'url': url.url,
        })
    
    return lists

def render_service_hotel_detail(services):
    lists = []
    
    print(services.is_free_wifi)
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