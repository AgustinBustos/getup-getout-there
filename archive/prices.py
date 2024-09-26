# pip install --upgrade pip
# pip install playwright
# playwright install
import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4")
    html=page.content()
    print(len(html))
    with open('saved.html','w') as file:
        file.write(html) 
    time.sleep(100000)
    browser.close()
