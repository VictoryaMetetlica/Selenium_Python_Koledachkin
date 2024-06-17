import time

from selenium import webdriver
    # Инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1900, 800')
    # зададим опцию, которая отключает режим автоматизации (WebDriver)
    # - дуйствует не всегда, например, в режиме '--headless' не везде сработает
options.add_argument('--disable-blink-features=AutomationControlled')
   # дополнительно зададим опцию, которая поменяет User-Agent (https://useragents.ru/stable.html- ПК агенты
    # https://deviceatlas.com/blog/mobile-browser-user-agent-strings - мобильные)
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

    # откроем сайт для работы
driver.get("http://the-internet.herokuapp.com/checkboxes")
    # зададим локаторы для каждого чекбокса
check_1 = ('xpath', "//input[@type='checkbox'][1]")
check_2 = ('xpath', "//input[@type='checkbox'][2]")
time.sleep(3)

    # вариант 1 чекбокса: кликнем по каждому чекбоксу и проверим их состояния методом get_attribute('checked') -
    # у отмеченного будет строковый тип 'true', у пустого отсуствует - None
print('состояние атрибута чекбокса 1 до клика', driver.find_element(*check_1).get_attribute('checked'))
driver.find_element(*check_1).click()
print('состояние атрибута чекбокса 1 после клика', driver.find_element(*check_1).get_attribute('checked'))
time.sleep(3)
print('состояние атрибута чекбокса 2 до клика', driver.find_element(*check_2).get_attribute('checked'))
driver.find_element(*check_2).click()
print('состояние атрибута чекбокса 2 после клика', driver.find_element(*check_2).get_attribute('checked'))
time.sleep(3)

    # вариант 2 чекбокса: кликнем по каждому чекбоксу и проверим их состояния методом .is_selected() - True/False
print('состояние атрибута чекбокса 1 до клика', driver.find_element(*check_1).is_selected())
driver.find_element(*check_1).click()
print('состояние атрибута чекбокса 1 после клика', driver.find_element(*check_1).is_selected())
time.sleep(3)
print('состояние атрибута чекбокса 2 до клика', driver.find_element(*check_2).is_selected())
driver.find_element(*check_2).click()
print('состояние атрибута чекбокса 2 после клика', driver.find_element(*check_2).is_selected())
time.sleep(3)

    # вариант 3 чекбокса: когда не отображается при инспектировании атрибут input (он перекрыт другими атрибутами,
                            # которые над ним)
    # откроем сайт
driver.get('https://demoqa.com/checkbox')
check_status = ('xpath', '//input[@id="tree-node-home"]')   # этот атрибут не кликабелен
check_action = ('xpath', '//span[text()="Home"]')    # span, через который мы будем кликать на элемент,
                                                                    # после которого появится атрибут check
print('состояние атрибута чекбокса check_status до клика', driver.find_element(*check_status).is_selected())
wait.until(EC.element_to_be_clickable(check_action)).click()    # driver.find_element(*check_action).click() - не всегда срабатывает. поэтому оформила через wait
print('состояние атрибута чекбокса check_status после клика', driver.find_element(*check_status).is_selected())

    # вариант 4 чекбокса: когда нет атрибута input - ищем атрибут DevTools, который изменяется при нажатии на чекбокс
driver.get("https://demoqa.com/selectable")
    # Записываем локатор первого чек-бокса
FIRST_CHECKBOX = ("xpath", "(//ul[@id='verticalListContainer']/li)[1]")
    # Кликаем на него
wait.until(EC.element_to_be_clickable(FIRST_CHECKBOX))    # driver.find_element(*FIRST_CHECKBOX).click() - не всегда срабатывает. поэтому оформила через wait
    # Проверяем, что после клика, к нему добавился класс active
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"
