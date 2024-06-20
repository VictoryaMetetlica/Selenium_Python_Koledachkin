from selenium import webdriver
    # Инициализация драйвера.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

    # Открыть страницу сайта https://testautomationpractice.blogspot.com/
driver.get(' https://testautomationpractice.blogspot.com')
    # Найти иконку Wikipedia по имени класса
el_c = driver.find_element('class name', 'wikipedia-icon')
print(el_c)
# Найти поле ввода Wikipedia по id
el_id = driver.find_element('id', 'Wikipedia1_wikipedia-search-input')
print(el_id)
# Найти кнопку поиска Wikipedia по классу
el_sc = driver.find_element('class name', 'wikipedia-search-button')
print(el_sc)
# Найти любой другой элемент на странице по тегу
el_body = driver.find_element('tag name', 'body')
print(el_body)



