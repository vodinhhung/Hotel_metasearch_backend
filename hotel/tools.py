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