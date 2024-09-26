import requests
import pandas as pd

proxy_list=pd.read_csv('proxies.csv')['ip'].tolist()
url="https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4"
# url='https://www.google.com/'
for proxy in proxy_list:
    proxies = {
    'http': proxy,
    'https': proxy,
    }
    try:
        r = requests.get(url,proxies=proxies)
        html=r.text
        if len(html)>1000:
            break
    except:
        pass
print(html)