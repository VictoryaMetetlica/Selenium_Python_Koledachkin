from selenium import webdriver
    # Инициализация драйвера.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


    # Открыть страницу сайта о пеларгониях https://pelargonii.ru.
driver.get('https://pelargonii.ru')
    # Получить и вывести title в консоль.
title1 = driver.title
print('заголовок первой страницы', title1)
    # Открыть другую страницу https://grasslandsilk.ru.
driver.get('https://grasslandsilk.ru')
    # Получить и вывести title в консоль.
title2 = driver.title
print('заголовок второй страницы', title2)
    # Вернуться назад к первой странице и, используя assert, убедиться, что вы точно вернулись обратно.
driver.back()
assert driver.title == title1, 'Это не первый заголовок'
    # Сделать рефреш страницы.
driver.refresh()
    # Получить и вывести URL-адрес текущей страницы.
print('Вернулись к первой странице, обновили ее, выводим ее url', driver.current_url)
    # Вернуться "вперед" к странице 2.
driver.forward()
    # Убедиться, что URL-адрес изменился.
assert driver.title == title2, 'Это не второй заголовок'
