
import requests
from config import busername, bpassword
import pandas as pd


#!/usr/bin/env python
proxy = f"http://{busername}:{bpassword}@brd.superproxy.io:22225"
url="https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/"#0?from=SB&di=4 'https://geo.brdtest.com/welcome.txt'

# url='https://httpbin.org/ip'

import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
if sys.version_info[0]==2:
    import six
    from six.moves.urllib import request
    opener = request.build_opener(
        request.ProxyHandler(
            {'http': proxy,
            'https': proxy}))
    print(opener.open(url).read())
if sys.version_info[0]==3:
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {'http': proxy,
            'https': proxy}))
    print(opener.open(url).read())





# result = requests.get(url, proxies = {
#     'http': proxy,
#     'https': proxy
# })
# pd.DataFrame({'proxy':['none'],'status':[result.status_code],'html':[result.text]}).to_csv('responses_bright.csv')