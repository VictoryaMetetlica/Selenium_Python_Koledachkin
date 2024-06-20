import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features+AutomationControlled")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://testautomationpractice.blogspot.com')
    # найдем нужный iframe и поместим веб-элемент в переменную
iframe_volunteer = driver.find_element(By.XPATH, "//iframe")
    # Теперь переключимся на iframe
driver.switch_to.frame(iframe_volunteer)
    # введем данные в поле First Name
name_field = driver.find_element(By.XPATH, "//input[@name='RESULT_TextField-0']")
name_field.send_keys("Viktoria")
time.sleep(5)
    # переключиться обратно с iframe на главный контент страницы (на дефолтный)
driver.switch_to.default_content()