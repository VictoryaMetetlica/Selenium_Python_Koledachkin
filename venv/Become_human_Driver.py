import os
from selenium import webdriver
    # Инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1980,800')
#options.add_argument('--headless')
    # зададим опцию, которая отключает режим автоматизации (WebDriver)
    # - дуйствует не всегда, например, в режиме '--headless' не везде сработает
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

    # Откроем сайт, который определяет, включен ли режим WebDriver
driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    # Зададим путь для сохранения скринов и сохраним в нее скрин
driver.save_screenshot(f'{os.getcwd()}/files/downloads/screenNoDriver.png')

