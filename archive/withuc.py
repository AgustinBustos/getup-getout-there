from datetime import datetime, timedelta
import time
import selenium
import pyautogui
import undetected_chromedriver as uc

pyautogui.FAILSAFE = False

user_data_dir='/home/agus/.config/google-chrome'
profile_directory='Default'

def open_browser(user_data_dir,profile_directory,url):
# log = logging.getLogger(__name__)
# driver = webdriver.Chrome(ChromeDriverManager().install())
    options = uc.ChromeOptions()
    options.add_argument('--user-data-dir='+user_data_dir) 
    options.add_argument(r'--profile-directory='+profile_directory) #e.g. Profile 3
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    # Disable webdriver flags or you will be easily detectable
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver=uc.Chrome(options=options)
    driver.get(url)
    return driver

def avoid_lock() -> None:
        x, _ = pyautogui.position()
        pyautogui.moveTo(x + 200, pyautogui.position().y, duration=1.0)
        pyautogui.moveTo(x, pyautogui.position().y, duration=0.5)
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.press('esc')
def fill_data(driver) -> None:
    driver.set_window_size(1, 1)
    driver.set_window_position(2000, 2000)
    driver.maximize_window()

if __name__ == '__main__':
    driver=open_browser(user_data_dir,profile_directory,"https://www.despegar.com.ar/shop/flights/results/roundtrip/BUE/MIA/2025-06-06/2025-06-22/4/0/0?from=SB&di=4")
    time.sleep(10)
    html = driver.page_source
    print(len(html))
    with open('saved.html','w') as file:
        file.write(html) 
    time.sleep(10000)