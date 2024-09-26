import requests
import pandas as pd
from tqdm import tqdm

proxy_list=pd.read_csv('proxies.csv')['ip'].tolist()
url="https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4"
# url='https://www.google.com/'
all_htmls=[]
all_status=[]
usefull_proxy=[]
for proxy in tqdm(proxy_list):
    proxies = {
    'http': proxy,
    'https': proxy,
    }
    try:
        r = requests.get(url,proxies=proxies)
        all_htmls.append(r.text)
        all_status.append(r.status_code)
        usefull_proxy.append(proxy)
        pd.DataFrame({'proxy':usefull_proxy,'status':all_status,'html':all_htmls}).to_csv('responses.csv')
        # if len(html)>1000:
        #     break
    except:
        pass
