from selenium import webdriver
import os
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from sys import platform

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


print("Deleting extra files")
if platform == 'linux' or platform == 'linux2':
    os.system('ls')

driver.get("https://www.whatsapp.com/download/")
time.sleep(10)
sendDocument("test.png")
driver.find_element('By.XPATH',
                    '//*[@id="content-wrapper"]/div/div/div/div/div/div/div[2]/div/div/div/div/div/h5[1]/a').click()
print("Download Button Clicked")

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
        print(f"File Downloaded: {downloadingFile}")
        sendDocument(downloadingFile)
        break
