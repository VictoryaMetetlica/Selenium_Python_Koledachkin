import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features+AutomationControlled")
driver = webdriver.Chrome(service=service, options=chrome_options)
    # Создаем объект action
action = ActionChains(driver)

driver.get("https://demoqa.com/buttons")
    # зададим локатор для двойного клика
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
    # зададим переменную для кнопки
BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
    # выполним двойной клик по кнопке
action.double_click(BUTTON).perform()
time.sleep(2)

driver.get("https://demoqa.com/buttons")
    # зададим локатор для правого клика
RС_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
    # зададим переменную для кнопки
BUTTON = driver.find_element(*RС_BUTTON_LOCATOR)
    # выполним правый клик по кнопке
action.context_click(BUTTON).perform()
time.sleep(3)

    # Используем скролл до элемента
driver.get("https://clipboardjs.com/")
SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
(action.scroll_to_element(SOME_ELEMENT) \
    .perform())
time.sleep(4)