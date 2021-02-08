import requests
import os
from pprint import pprint

# token = os.environ['token']
token = '1646026624:AAFl-4-09PT5AM5T1RewNdGSo52jnLMLNv4'
# 1258594598

def getUpdates():
    
    url_Updates = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.get(url_Updates)
    updates = res.json()['result']
    
    return updates
getUpdates()

def Count(data):
    n_like = 0
    n_dLike = 0
    for x in data:
        msg_text = x['message'].get('text')

        if msg_text != None:
            if msg_text == '👍':
                n_like += 1
            elif msg_text == '👎':
                n_dLike += 1
    
    return n_like, n_dLike

m0 = 0
while True:
    m1 = len(getUpdates())
    if m0 != m1:
        n_1, n_2 = Count(getUpdates())
        f = open('data.json', 'w')
        f.write(f'like = {n_1}\ndislike = {n_2}')
        f.close()
        print(n_1, n_2)
        m0 = m1
