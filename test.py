from selenium import webdriver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from sys import platform

options = webdriver.ChromeOptions()
options.add_argument("--headless --sandbox --disable-gpu")


preferences = {"download.default_directory": os.getcwd(),
               "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
print("Headless Chrome Driver Initiated!")

print("Deleting extra files")
if platform == 'linux' or platform == 'linux2':
    os.system(
        'rm -rf -v !("bot.py"|"Procfile"|"requirements.txt"|"runtime.txt"|"test.py")')

driver.get("https://www.whatsapp.com/download/")
driver.find_element_by_xpath(
    '//*[@id="content-wrapper"]/div/div/div/div/div/div/div[2]/div/div/div/div/div/a').click()
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
        break
