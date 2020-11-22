import requests
import base64
from datetime import date
from hotel.models import Domain, Url, Quality, Root, Info, Rank
import threading
from time import sleep
today = date.today() 
date = str(today.year)+str(today.month)+str(today.day)
price_weight = 1.1594202897206469e-10

def update_min_price(urls):
    #chạy sau khi trả response 60s
    for url in urls:
        domain_id = str(url.domain_id)
        domain_hotel_id = str(url.domain_hotel_id)
        params = domain_id+ "_" +domain_hotel_id+ "_" + date
        payload =  '{"hotel_ids": '+'"'+params+'"'+'}'
        current_price = get_price(payload)
        if (current_price != float('inf')) and ((int(current_price) - int(url.min_price)) != 0):
            url.min_price = int(current_price)
            url.save()
            print("Updated min price with domain_hotel_id: ",url.domain_hotel_id)

def update_min_price_domain(root):
    #chạy sau khi trả response 120s, phải update min_price trước
    urls = Url.objects.filter(root_id = root.id)
    [min_price, min_domain_id] = get_min_price_hotel_database(urls)
    if (min_price != -1) and (int(min_price) != int(root.min_price_domain)):
        root.min_price_domain = int(min_price)
        root.save()
        print("Updated min price domain with root_id:  ",root.id)

def update_ranking(root):
    #tích hợp update min price domain và ranking
    sleep(60)
    urls = Url.objects.filter(root_id = root.id)
    [min_price, min_domain_id] = get_min_price_hotel_database(urls)
    if (min_price != -1) and (int(min_price) != int(root.min_price_domain)):
        list_price = list(Root.objects.values_list('min_price_domain', flat=True))
        sum_price_old = sum(list(filter(lambda a: a != -1, list_price)))
        # update price
        t = root.min_price_domain
        root.min_price_domain = int(min_price)
        root.save()
        print("Updated min price domain with root_id:  ",root.id)
        # update ranking
        sum_price_new = sum_price_old - t + min_price
        rank = Rank.objects.get(root_id = root.id)
        score = rank.rank_score - price_weight*(sum_price_old/t) + price_weight*(sum_price_new/min_price)
        rank.rank_score = float(score)
        rank.save()
       
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
        return float('inf')
    else:
        min = float('inf')
        for i in range(0,len(a[0])):
            t = float(a[0][i].get("final_amount"))
            if t<min:
                min = t
        return min

def get_min_price_domain(urls):
    min_price = float('inf')
    min_domain_id = -1

    for url in urls:
        domain_id = str(url.domain_id)
        domain_hotel_id = str(url.domain_hotel_id)
        params = domain_id+ "_" +domain_hotel_id+ "_" + date
        payload =  '{"hotel_ids": '+'"'+params+'"'+'}'

        current_price = get_price(payload)
        if float(current_price) < min_price :
            min_price = current_price
            min_domain_id = domain_id 
    
    if min_price == float('inf'):
        min_price = 100000
    
    return [min_price, min_domain_id]

def get_min_price_hotel(urls):
    params = ''
    for url in urls:
        domain_id = str(url.domain_id)
        domain_hotel_id = str(url.domain_hotel_id)
        param = domain_id+ "_" +domain_hotel_id+ "_" + date
        params += param+","

    params = params.rstrip(",")
    payload =  '{"hotel_ids": '+'"'+params+'"'+'}'
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
    min_price = float('inf')
    min_domain_id = -1

    for i in range(0,len(a)):
        if (a[i] == []) or (a[i] == [[]]):
            continue
        else:
            for j in range(0,len(a[i])):
                t = float(a[i][j].get("final_amount"))
                if t<min_price:
                    min_price = t
                    min_domain_id = str(a[i][j].get("domain_id"))

    if min_price == float('inf'):
        min_price = 100000
    
    return [min_price, min_domain_id]

def get_min_price_hotel_database(urls):
    t = threading.Thread(target=update_min_price, args=[urls])
    t.setDaemon(False)
    t.start()
    min_price = float('inf')
    min_domain_id = -1
    for url in urls:
        t = url.min_price
        if (t > 0) and (t < min_price):
            min_price = t
            min_domain_id = url.domain_id
        
    if min_price == float('inf'):
        min_price = -1
    
    return [min_price, min_domain_id]

def hotel_list_filter_facility(root, facility):
    info_query_10 = Info.objects.filter(is_free_wifi = 1)
    info_query_11 = Info.objects.filter(have_car_park = 1)
    info_query_12 = Info.objects.filter(have_airport_transport = 1)
    info_query_13 = Info.objects.filter(have_restaurant = 1)
    info_query_14 = Info.objects.filter(have_baby_service = 1)
    info_query_15 = Info.objects.filter(have_bar = 1)
    info_query_16 = Info.objects.filter(have_laundry = 1)
    info_query_17 = Info.objects.filter(have_tour = 1)
    info_query_18 = Info.objects.filter(have_spa = 1)
    info_query_19 = Info.objects.filter(have_pool = 1)
    if facility is not None:
        if str(facility).find('10') > -1:
            root = root.filter(id__in=info_query_10)
        if str(facility).find('11') > -1:
            root = root.filter(id__in=info_query_11)
        if str(facility).find('12') > -1:
            root = root.filter(id__in=info_query_12)
        if str(facility).find('13') > -1:
            root = root.filter(id__in=info_query_13)
        if str(facility).find('14') > -1:
            root = root.filter(id__in=info_query_14)
        if str(facility).find('15') > -1:
            root = root.filter(id__in=info_query_15)
        if str(facility).find('16') > -1:
            root = root.filter(id__in=info_query_16)
        if str(facility).find('17') > -1:
            root = root.filter(id__in=info_query_17)
        if str(facility).find('18') > -1:
            root = root.filter(id__in=info_query_18)
        if str(facility).find('19') > -1:
            root = root.filter(id__in=info_query_19)
    return root
