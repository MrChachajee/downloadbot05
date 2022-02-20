from reprlib import recursive_repr
from selenium import webdriver
from selenium.common import exceptions as e
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
import time
# from sys import platform

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
options.add_argument('--disable-software-rasterizer')
options.add_argument(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
options.add_argument("--lang=en")

preferences = {"download.default_directory": os.getcwd(),
               "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
print("Headless Chrome Driver Initiated!")


def sendDocument(filename):
    driver.save_screenshot("test.png")
    files = {'document': open(f"./{filename}", 'rb')}
    url = "https://api.telegram.org/bot5243536300:AAFQrJVeFQKChsh8QEbwA-pZ4k2I2gOkLAU/sendDocument?chat_id=2083029174"
    res = requests.post(url, files=files)


def check_by_partial_link_text(path):
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, path)
    except e.NoSuchElementException:
        return False
    return True


# print("Deleting extra files")
# if platform == 'linux' or platform == 'linux2':
#     os.system('ls')


driver.get("https://www.whatsapp.com/download/")
time.sleep(3)
sendDocument("test.png")
if check_by_partial_link_text("ACCEPT"):
    driver.find_element(By.PARTIAL_LINK_TEXT, "ACCEPT").click()
if check_by_partial_link_text("64-bit"):
    driver.find_element(By.PARTIAL_LINK_TEXT, "64-bit").click()
print("Download Button Clicked")
sendDocument("test.png")
dlwait = False

# downloadingFile = "runtime.txt"

while True:
    time.sleep(5)
    files = os.listdir(os.getcwd())
    for fname in files:
        if fname.endswith('.crdownload'):
            downloadingFile = fname[:-11]
            print(
                f"{downloadingFile}: {int(os.path.getsize(fname) / (1024 * 1024))}MB Downloaded")
            dlwait = True
            break
        else:
            dlwait = False
    if not dlwait:
        print(f"File Downloaded: {downloadingFile}")
        break
