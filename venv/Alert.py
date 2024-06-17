import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
		# Создание экземпляра веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
		# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")
		# Клик на кнопку, которая вызывает alert
BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
		# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
		# Переключение на alert
driver.switch_to.alert
		# Клик на кнопку, которая вызывает alert
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
print(alert.text)
alert.accept() 			# Принимаем алерт
		# Клик на кнопку, которая вызывает alert
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.dismiss() 			# Отклоняем алерт
    # Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
print(alert.text)  # Вывод текста из алерта

    # Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
    # Ввод данных в alert
alert.send_keys("Hello world")
    # Обязательно либо примите либо отклоните alert после вводад анных
alert.accept()