import requests
from datetime import date

from hotel.models import User

today = date.today() 
date = str(today.year)+str(today.month)+str(today.day)

def call_facebook_api(token):
    url = "https://graph.facebook.com/v8.0/me"
    parameters = {
        "access_token": token,
        "fields": "id, name, picture"
    }
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        return [True, response.json()]
    else:
        return [False, {}]

def call_google_api(token):
    url = "https://www.googleapis.com/oauth2/v2/userinfo"
    parameters = {
        "access_token": token,
        "alt": "json"
    }
    response = requests.get(url, params=parameters)
    return 0

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

def check_token_user(token):
    if token is None or token == "":
        return ["", False]
    
    token = token[7:]
    current_date = ""
    user_id = ""
    index = 0
    for i in range(len(token)-2):
        if token[i] == '@' and token[i+1] == '@' and token[i+2] == '@':
            user_id = token[:i]
            current_date = token[(i+3):]
            index += 1
            break
    
    if index == len(token)-3 or current_date != date or not User.objects.filter(social_id = user_id).exists():
        return ["", False]

    return [user_id, True]