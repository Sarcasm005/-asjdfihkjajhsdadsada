import requests
import json
import config

def track(token, uid, message, name='Message'):
    try:
        r = requests.post(
            config.TRACK_URL,
            params={
                  "token": token,
                    "uid": uid,
                   "name": name
                   }, data=json.dumps(message),
            headers={'Content-type': 'application/json'},
        )
        return r.json()
    except: 
        return False



def shorten_url(url, botan_token, user_id):

    try:
        return requests.get(config.SHORTENER_URL, params={
            'token': botan_token,
            'url': url,
            'user_ids': str(user_id),
        }).text
    except:
        return url
