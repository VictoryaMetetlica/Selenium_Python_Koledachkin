from selenium import webdriver
    # Инициализация драйвера.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

    # На странице https://hyperskill.org/tracks
driver.get('https://hyperskill.org/tracks')
    # Найти заголовок What is yur goal
el_c = driver.find_element('xpath', "//h1[@class='mb-4']").text
print(el_c)
