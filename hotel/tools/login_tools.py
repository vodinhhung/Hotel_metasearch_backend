import requests
from datetime import date

from hotel.models import User

today = date.today() 
date = str(today.year)+str(today.month)+str(today.day)

def call_facebook_api(token):
    url = "https://graph.facebook.com/v8.0/me"
    parameters = {
        "access_token": token,
        "field": "id, name"
    }
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        return [True, response.json()]
    else:
        return [False, {}]

# Save information of user from response after calling api of domain
# to local database 
def save_user_database(info, domain):
    name = info['name']
    social_id = info['id']

    if not User.objects.filter(social_id=social_id, social_domain=domain).exists():
        user = User(
            social_id = social_id,
            name = name,
            social_domain = domain
        )
        user.save()
    else:
        user = User.objects.get(social_id=social_id, social_domain=domain)
        new_user = User(
            index = user.index,
            social_id = social_id,
            name = name,
            social_domain = domain,
        )
        new_user.save()

    access_token = social_id + "@@@" + date
    return access_token