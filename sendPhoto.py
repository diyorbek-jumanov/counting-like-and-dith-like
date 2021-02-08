import requests
import os
from pprint import pprint

# token = os.environ['token']
token = '1646026624:AAFl-4-09PT5AM5T1RewNdGSo52jnLMLNv4'
# 1258594598

def sendPhoto():
    
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload = {
        'chat_id': 1258594598,
        'photo': 'https://images.app.goo.gl/Dw9GVsbafCDKoaXN7',
        'caption': 'masjid rasmi'
    }
    respons = requests.get(url=url, params=payload)
    

sendPhoto()
