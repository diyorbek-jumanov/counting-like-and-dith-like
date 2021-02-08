import requests
import os
from pprint import pprint

# token = os.environ['token']
token = '1646026624:AAFl-4-09PT5AM5T1RewNdGSo52jnLMLNv4'
# 1258594598
# AgACAgQAAxkBAAMOYCC-dNtXi3ZzJ8xHlMVXSVycWOsAAuyqMRtxmGxQW71jzwkrdqeImgABI10AAwEAAwIAA20AAz-IAAIeBA

def sendPhoto():
    
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload = {
        'chat_id': 1258594598,
        'photo': 'AgACAgQAAxkBAAMOYCC-dNtXi3ZzJ8xHlMVXSVycWOsAAuyqMRtxmGxQW71jzwkrdqeImgABI10AAwEAAwIAA20AAz-IAAIeBA',
        'caption': 'masjid rasmi'
    }
    respons = requests.get(url=url, params=payload)
    

sendPhoto()
