import time
from selenium import webdriver

    # Инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1980,1080')  # type: ignore
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)


    # импортируем WebDriverWait и expected_conditions as EC для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

        # Явные ожидания (необходимо предварительно импортировать WebDriverWait и expected_conditions as EC)
    # - прописывается для каждого элемента отдельно
wait = WebDriverWait(driver, 15, poll_frequency=1)

        #  Задание 1: Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
    # откроем сайт
driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки
Change_Text_Button = ('xpath', '//button[@id="populate-text"]')
    # Кликнем на кнопку “Change Text to Selenium Webdriver” с помощью распаковщика кортежей
driver.find_element(*Change_Text_Button).click()
    # задададим переменную (локатор-кортеж) для дальнейшего поиска текста
Text_for_chenging = ('xpath', '//h2[@class="target-text"]')
    # передадим в text_to_be_present_in_element итерируемый объект - кортеж и ожидаемый по условию текст
wait.until(EC.text_to_be_present_in_element(Text_for_chenging, 'Selenium Webdriver'))

        #  Задание 2: Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
    # откроем сайт
driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки “Display button after 10 seconds”
Display_button_after_10 = ('xpath', '//button[@id="display-other-button"]')
    # Кликнем на кнопку “Display button after 10 seconds” с помощью распаковщика кортежей
driver.find_element(*Display_button_after_10).click()
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки “Enabled”
Button_Enable = ('xpath', '//button[@id="hidden"]')
    # передадим в visibility_of_element_located итерируемый объект - кортеж, чтобы дождаться появления кнопки “Enabled”
wait.until(EC.visibility_of_element_located(Button_Enable), message='No visible')

       #  Задание 3: Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
    # откроем сайт
driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки “Enable button after 10 seconds”
Enable_button_after_10 = ('xpath', '//button[@id="enable-button"]')
    # Кликнем на кнопку “Enable button after 10 seconds” с помощью распаковщика кортежей
driver.find_element(*Enable_button_after_10).click()
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки “Button”
Button = ('xpath', '//button[@id="disable"]')
    # передадим в element_to_be_clickable итерируемый объект - кортеж, чтобы дождаться кликабельности кнопки “Enabled”
wait.until(EC.element_to_be_clickable(Button), message='No clickable')

      #  Задание 4: Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
    # откроем сайт
driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки “Click me, to Open an alert after 5 seconds”
Click_me_to_Open_alert = ('xpath', '//button[@id="alert"]')
    # Кликнем на кнопку “Click_me_to_Open_alert” с помощью распаковщика кортежей
driver.find_element(*Click_me_to_Open_alert).click()
    # задададим переменную (локатор-кортеж) для дальнейшего поиска кнопки “Button”

    # передадим в visibility_of_any_elements_located итерируемый объект - кортеж, чтобы дождаться кликабельности кнопки “Enabled”
alert = wait.until(EC.alert_is_present(), message='No Alert: Всплывающее окно отсутствует')
if alert:
    alert.accept()

time.sleep(5)