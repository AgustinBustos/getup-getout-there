import threading
import queue
import requests
import pandas as pd
q=queue.Queue()

url="https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4"
url='http://ipinfo.io/json'

all_proxies=pd.read_csv('proxies.csv')['ip'].tolist()
for p in all_proxies:
    q.put(p)

valid_proxies=[]
all_html=[]
def check_proxies():

    global q
    while not q.empty():
        proxy=q.get()
        try:
            res=requests.get(url,proxies={'http':proxy,'https':proxy})
        except:
            continue
        if res.status_code==200:
            print(proxy)
            # valid_proxies.append(proxy)
            # all_html.append(res.text)
for _ in range(4):
    threading.Thread(target=check_proxies).start()