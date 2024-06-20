import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

        # Страница для работы
driver.get("http://the-internet.herokuapp.com/key_presses")
time.sleep(2)
    # Поле ввода
KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")
    # Ввод текста
driver.find_element(*KEY_PRESS_INPUT).send_keys('I am')
time.sleep(3)
    # Выделение всего текста
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.COMMAND + "A")
time.sleep(2)
    # Удаление выделенного текста
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACK_SPACE)
time.sleep(2)