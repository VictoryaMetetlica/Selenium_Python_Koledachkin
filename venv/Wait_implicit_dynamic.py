import time
from selenium import webdriver

    # Инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

        # Неявные ожидания - прописывается один раз
driver.implicitly_wait(10)
    # откроем сайт
driver.get("https://demoqa.com/dynamic-properties")
    # рассмотрим работу кнопки, которая появляется на сайте через 5 с после его загрузки
Visible_After_5_Button = ('xpath', '//button[@id="visibleAfter"]')
    # передадим с помощью распаковщика переменную
driver.find_element(*Visible_After_5_Button).click()
time.sleep(3)
