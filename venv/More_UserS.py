import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features+AutomationControlled")

    # Чтобы подключить несколько пользователей, необходимо использовать несколько driver - users (будут разные сессии)
driver1 = webdriver.Chrome(service=service, options=chrome_options)
driver2 = webdriver.Chrome(service=service, options=chrome_options)
driver3 = webdriver.Chrome(service=service, options=chrome_options)

