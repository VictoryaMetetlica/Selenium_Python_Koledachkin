import os
import time

from selenium import webdriver
    # Инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
    # импортируем WebDriverWait и expected_conditions as EC для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1980,800')
options.add_argument('--headless')
    # зададим опцию, которая отключает режим автоматизации (WebDriver)
    # - дуйствует не всегда, например, в режиме '--headless' не везде сработает
options.add_argument("--disable-blink-features=AutomationControlled")
   # дополнительно зададим опцию, которая поменяет User-Agent (https://useragents.ru/stable.html- ПК агенты
    # https://deviceatlas.com/blog/mobile-browser-user-agent-strings - мобильные)
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
      # Явные ожидания (необходимо предварительно импортировать WebDriverWait и expected_conditions as EC)
wait = WebDriverWait(driver, 15, poll_frequency=1)
    # Откроем сайт, который определяет, включен ли режим WebDriver
driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    # Зададим путь для сохранения скринов
driver.save_screenshot(f'{os.getcwd()}/files/downloads/screenAgent.png')
time.sleep(2)

