from reprlib import recursive_repr
from selenium import webdriver
from selenium.common import exceptions as e
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
import time
from sys import platform

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
# options.add_argument("--enable-javascript")
# options.add_argument("--disable-extensions")
# options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
# options.add_argument('--disable-software-rasterizer')
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
options.add_argument("--lang=en")

preferences = {"download.default_directory": os.getcwd(),
               "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

if platform == 'linux' or platform == 'linux2':
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
else:
    driver = webdriver.Chrome(service=Service(
        'C:/Users/argam/Documents/chromedriver.exe'), options=options)


print("Headless Chrome Driver Initiated!")
driver.get("https://www.whatsapp.com/download/")

x = 0


def sendDocument(filename):
    global x
    x += 1
    driver.save_screenshot("test.png")
    files = {'document': open(f"{os.getcwd()}/{filename}", 'rb')}
    url = "https://api.telegram.org/bot5243536300:AAFQrJVeFQKChsh8QEbwA-pZ4k2I2gOkLAU/sendDocument?chat_id=2083029174&caption=Number: " + \
        str(x)
    res = requests.post(url, files=files)
    print(res.status_code)
    print(f"File Sended: {filename}")


def download_file():
    sendDocument("test.png")
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "64-bit").click()
    except e.ElementClickInterceptedException:
        print(driver.current_url)
        driver.refresh()
        element = driver.find_element(By.PARTIAL_LINK_TEXT, "64-bit")
        driver.execute_script("arguments[0].click();", element)

    print("Download Button Clicked")
    sendDocument("test.png")
    saving_file()


downloadingFile = ""


def saving_file():
    global downloadingFile
    dlwait = False
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
            if downloadingFile:
                sendDocument(downloadingFile)
                print(f"File Downloaded: {downloadingFile}")
            else:
                print("File Not Downloaded... Retrying...")
                download_file()
            break


download_file()
