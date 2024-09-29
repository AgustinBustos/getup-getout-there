import requests
from config import username, password
import pandas as pd



url="https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4"

proxy = f"http://{username}:{password}@ar.smartproxy.com:10001"
result = requests.get(url, proxies = {
    'http': proxy,
    'https': proxy
})
pd.DataFrame({'proxy':['none'],'status':[result.status_code],'html':[result.text]}).to_csv('responses.csv')