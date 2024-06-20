import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

        # Страница для работы
driver.get("https://demoqa.com/select-menu")
    # напишем локатор для селектора окна ввода Select One
select_locator = ("xpath", "//input[@id='react-select-3-input']")
time.sleep(3)
    # введем в поле ввода под Select One нужную позицию
driver.find_element(*select_locator).send_keys('Ms.')
    # подтвердим выбор позиции командой клавиатуры ENTER
driver.find_element(*select_locator).send_keys(Keys.ENTER)
time.sleep(3)

        # Страница для работы
driver.get("https://demoqa.com/select-menu")
    # напишем локатор для селектора окна ввода Multi (можно выбирать несколько позиций)
multiSelect_locator = ('xpath', '//input[@id="react-select-4-input"]')
    # введем в поле ввода под Multiselect нужную позицию
driver.find_element(*multiSelect_locator).send_keys('Green')
time.sleep(3)
    # подтвердим выбор позиции командой клавиатуры ENTER
driver.find_element(*multiSelect_locator).send_keys(Keys.ENTER)
time.sleep(3)
    # введем в поле ввода под Multiselect нужную позицию
driver.find_element(*multiSelect_locator).send_keys('Black')
time.sleep(3)
driver.find_element(*multiSelect_locator).send_keys(Keys.ENTER)
time.sleep(3)

