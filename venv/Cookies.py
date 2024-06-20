import pickle   # for download/upload cookies
import os
import time

from selenium import webdriver
    # Инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1980,800')

    # зададим опцию, которая отключает режим автоматизации (WebDriver)
    # - дуйствует не всегда, например, в режиме '--headless' не везде сработает
options.add_argument("--disable-blink-features=AutomationControlled")
   # дополнительно зададим опцию, которая поменяет User-Agent (https://useragents.ru/stable.html- ПК агенты
    # https://deviceatlas.com/blog/mobile-browser-user-agent-strings - мобильные)
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

    # Задание 1 (Установка и чтение куки)
        # - Откройте любой сайт и добавьте куки с именем "username" и значением "user123".
        # - Затем обновите страницу и убедитесь, что кука "username" была успешно установлена.
        # - Получите и провалидируйте значение куки "username" и выведете его на экран.
        # Используйте режим отключения WebDriver и User-agent
    # - Открем сайт
driver.get('https://habr.com/ru/articles/250975/')
time.sleep(5)
    # для начала просмотрим имеющиеся куки
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
    # для наглядности добавим пустые строчки
print()
print()
    # добавим куки с именем "username" и значением "user123" и выведем на экран
driver.add_cookie({'name': 'username', 'value': 'user123'})
    # обновим страницу и проверим добавлнение куки с именем "username" выводом на экран
after = driver.get_cookie("username")
driver.refresh()
before = driver.get_cookie("username")
assert after == before, 'Куки не добавилась'
print(driver.get_cookie('username'))
print()


    # Задание 2 (Удаление куков)
        # - Откройте любой сайт и через Devtools выберете куку.
        # - Удалите выбранную куку.
        # - После удаления куки, обновите страницу и проверьте, что она отсутствует.
    # - Открем сайт
driver.get("https://demoqa.com/alerts")
    # - Сохраним куки в переменную
before = driver.get_cookie("panoramaIdType")
print('кука до', before)
    # Очистим куку, чтобы не было наложений
driver.delete_cookie("panoramaIdType")
    # обновим страницу и проверим ее отсуствие
driver.refresh()
after = driver.get_cookie("panoramaIdType")
print('кука после', after)

    # Задание 3 (Автоматизация корзины покупок)
        # Напишите сценарий, который использует Selenium WebDriver для автоматического добавления товаров в корзину, в интернет-магазине.
        # После добавления товаров, сохраните состояние корзины, записав куки в переменную или файл.
        # Затем удалите все товары из корзины, очистив все куки и перезагрузив страницу.
        # Восстановите сессию путем подставления ранее сохраненных куков и перезагрузкой странцы после.

driver.get("https://www.wildberries.by/")
driver.delete_all_cookies()
COOKIES = ("xpath", "//div[@class ='modal-body__buttons']//button[@data-tag = 'confirm']")
wait.until(EC.visibility_of_element_located(COOKIES))
driver.find_element(*COOKIES).click()
LIST_1 = driver.find_elements("xpath", "//a[@class='product-card__link']")
for i in range(int(len(LIST_1))):
    wait.until(EC.presence_of_element_located(("xpath", "//a[@class='product-card__link']")))
    ITEM = LIST_1[i]
    ITEM.click()
    wait.until(EC.presence_of_element_located(("xpath","(//button[@data-tag='basketButtonMain'])[1]")))
    BUTTON = driver.find_element("xpath","(//button[@data-tag='basketButtonMain'])[1]")
    BUTTON.click()
    driver.back()
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))   #сохраняем куки в папку
driver.delete_all_cookies()
driver.refresh()
cookies = pickle.load(open(os.getcwd()+"/files/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()    # чтобы куки применились
time.sleep(3)
