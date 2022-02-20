from selenium import webdriver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()

preferences = {"download.default_directory": os.getcwd(),
               "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get("https://www.whatsapp.com/download/")
driver.find_element_by_xpath(
    '//*[@id="content-wrapper"]/div/div/div/div/div/div/div[2]/div/div/div/div/div/a').click()


def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    time.sleep(3)
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items[0].state === 'COMPLETE') return "Completed";
        else if(items[0].state === 'IN_PROGRESS') return items[0].progressStatusText;
        else return items[0].state;
        """)


print("Starting loop...")

while True:
    if every_downloads_chrome(driver) == 'CANCELLED':
        print("Cancelled")
    else:
        print(every_downloads_chrome(driver))
    time.sleep(5)
