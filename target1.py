# import json
import json

import pandas as pd
import requests
# import json
url ='https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&keyword=samsung+galaxy&offset=0&page=%2Fs%2Fsamsung+galaxy&platform=desktop&pricing_store_id=921&store_ids=921%2C1030%2C1907%2C682%2C2474&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F96.0.4664.110+Safari%2F537.36&visitor_id=017E2A42695C0201A434D1FCA85B69BD'
head={
    'Accept': 'application/json',
    'Referer': 'https://www.target.com/s?searchTerm=samsung+galaxy',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
response=requests.request("GET",url=url,headers=head)
x = response.text
y=json.loads(x)
lst1=[]
print(y['data']['search']['products'])
for i in y['data']['search']['products']:
    anwer=dict()
    anwer['url']= i['item']['enrichment']['buy_url']
    anwer['title'] = i['item']['product_description']['title']
    anwer['price']=i['price']['current_retail']
    anwer['brand']=i['item']['primary_brand']['name']
    try:
        if i['sponsored_ad']:
            anwer['sponsered']='yes'
        else:
            anwer['sponsered'] = 'no'
    except:
        anwer['sponsered'] = 'no'
    lst1.append(anwer)

print(lst1)
r = json.dumps(lst1)
print(r)

df = pd.lst1
print(df)



print('***********')
