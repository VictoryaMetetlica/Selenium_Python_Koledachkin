from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
import time


driver.get('https://habr.com/ru/articles/250975/')
time.sleep(10)
driver.back()
time.sleep(5)
driver.forward()
driver.refresh()