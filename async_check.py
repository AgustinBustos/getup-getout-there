import asyncio
from time import perf_counter
import aiohttp
import pandas as pd

proxy_list=pd.read_csv('proxies.csv')['ip'].tolist()

url = "https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4"
# url ='https://www.google.com/'
# url='http://ipinfo.io/json'

async def fetch(s, url, proxy):
    try:
        async with s.get(url, proxy=proxy) as r:
            if r.status != 200:
                r.raise_for_status()
            return await r.text()
    except Exception as e:
        print(f"Failed to fetch via {proxy}: {e}")
        return None


async def fetch_all(s, url, proxies):
    tasks = []
    for proxy in proxies:
        task = asyncio.create_task(fetch(s, url, proxy))
        tasks.append(task)

    # Wait for all tasks to complete and gather their results
    responses = await asyncio.gather(*tasks)
    
    # Filter out None responses in case any proxy fails
    html_responses = [response for response in responses if response is not None]
    return html_responses


async def main():
    
    proxies = ['http://'+i for i in proxy_list]

    async with aiohttp.ClientSession() as session:
        html_responses = await fetch_all(session, url, proxies)
        
        # Print the number of successfully fetched HTML pages
        print(f"Successfully fetched {len(html_responses)} HTML responses")
        
        # You now have all HTML responses saved in this list
        for i, html in enumerate(html_responses):
            print(f"HTML from proxy {proxies[i]}: {html[:100]}...")  # Print first 100 characters as a preview

        return html_responses

if __name__ == '__main__':
    start = perf_counter()
    html_list = asyncio.run(main())  # Get the HTML list from main
    pd.DataFrame(html_list).to_csv('gathered.csv')
    stop = perf_counter()
    
    print("time taken:", stop - start)
    print(f"Collected {len(html_list)} HTML pages.")