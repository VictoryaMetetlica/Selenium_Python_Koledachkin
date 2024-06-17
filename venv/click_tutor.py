from time import sleep

from selenium import webdriver
    # Инициализация драйвера.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Задание 1: Заполнить все текстовые поля данными (почистить поля перед заполнением). Проверить, что данные действительно
# введены, используя get_attribute() и assert. Страница для выполнения задания: https: // demoqa.com / text - box


driver.get('https://demoqa.com/text-box')
full_name = driver.find_element('xpath', '//input[@id="userName"]')
email = driver.find_element('xpath', '//input[@id="userEmail"]')
current_address = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
permanent_address = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')

data = {
    full_name: 'Vika Miatselitsa',
    email: 'XXX@mail.com',
    current_address: 'The World',
    permanent_address: 'North'
}

for key, value in data.items():
    key.clear()
    key.send_keys(value)
    assert value in key.get_attribute('value')

sleep(3)
driver.find_element('xpath', '//button[@id="submit"]').click()
sleep(5)

# Задание 2: Прокликать все ссылки со статус - кодами на странице, используя алгоритм перебора элементов.
# После каждого клика возвращаться на стартовую страницу. Страница для выполнения задания:
# http: // the - internet.herokuapp.com / status_codes

driver.get('https://the-internet.herokuapp.com/status_codes')
data_lst = driver.find_elements('xpath', '//a[contains(@href, "status_code")]')
sleep(5)
for item in data_lst:
    item.click()
    sleep(3)
    driver.back()
sleep(5)
