from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

    # опции браузера - создаем объект options
options = webdriver.ChromeOptions()

    # "--headless" - запускает браузер в режиме без графического интерфейса.
    # Это позволяет выполнять тесты в фоновом режиме без отображения окна браузера.
#options.add_argument("--headless")

    # "--incognito" - запускает браузер в режиме инкогнито (приватного просмотра).
    # Это позволяет тестировать поведение сайта без использования кэша и сохраненных данных.
#options.add_argument("--incognito")

    # "--window-size=X,Y"- устанавливает размер окна браузера. Можно указать ширину и высоту в пикселях.
    # Например, --window-size=1280,800.
options.add_argument('--window-size=800,800')

    # "--disable-cache"- отключает кэширование в браузере. Это позволяет загружать каждый ресурс (например,
    # изображения, стили, скрипты) с сервера при каждой загрузке страницы.
options.add_argument('--disable-cache')

service = Service(ChromeDriverManager().install())

            # strategy:
    # Реализация normal strategy: браузер не закроется, пока все ресурсы страницы не будут загружены.
#options.page_load_strategy = 'normal'

    # Реализация eager strategy: визуально заметим, что браузер закрывается еще не дождавшись подгрузки картинок.
options.page_load_strategy = 'eager'

    # прокиньте созданный обьект options в аргументы Chrome в виде options=options
driver = webdriver.Chrome(service=service, options=options)
import time

    # Открыть страницу сайта
driver.get('https://pelargonii.ru')
time.sleep(3)
el = driver.find_element('xpath', '//a[contains(@href, "zolotolistnye")]')
el.click()
#time.sleep(3)
named = driver.find_elements('xpath', '//h3')
for name in named:
    print(name.get_attribute('value'))
