import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
    # зададим опцию, которая отключает режим автоматизации (WebDriver)
    # - дуйствует не всегда, например, в режиме '--headless' не везде сработает
options.add_argument('--disable-blink-features=AutomationControlled')
   # дополнительно зададим опцию, которая поменяет User-Agent (https://useragents.ru/stable.html- ПК агенты
    # https://deviceatlas.com/blog/mobile-browser-user-agent-strings - мобильные)
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.maximize_window()  # пробовала увеличить экран, чтоб селениум увидел все кнопки - не всегда помогло

driver.get("https://demoqa.com/selectable")

Grid_button = ("xpath", "//a[@id='demo-tab-grid']")
One_button = ("xpath", "//div[@id='row1']/li[1]")
Five_button = ("xpath", "//div[@id='row2']/li[2]")

    # если кнопки перекрываются рекламой и из-за этого селениум не может найти элемент,
        # нужно убрать iframe с рекламой через javaScript, чтобы селениум смог найти этот элемент.
driver.execute_script("var elem = document.getElementById('google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0'); "
                      "if (elem) elem.parentNode.removeChild(elem);")

    # перейдем во вкладку Grid кликом по кнопке
wait.until(EC.element_to_be_clickable(Grid_button)).click()

    # выделим кнопку One
# wait.until(EC.element_to_be_clickable(One_button))
driver.find_element(*One_button).click() # - не всегда срабатывает. поэтому оформила через wait
    # проверим, выполнилось ли выделение кнопки (чекбокса) One
One_clicked = driver.find_element(*One_button).get_attribute('class')
assert "active" in One_clicked, 'Выделение кнопки (чекбокса) One не выполнено'
time.sleep(2)

    # выделим кнопку Five
wait.until(EC.element_to_be_clickable(Five_button)).click()
    # проверим, выполнилось ли выделение кнопки (чекбокса) Five
Five_clicked = driver.find_element(*Five_button).get_attribute("class")
assert "active" in Five_clicked, 'Выделение кнопки (чекбокса) Five не выполнено!'
time.sleep(2)

    # снимем выделение кнопки Five
wait.until(EC.element_to_be_clickable(Five_button))
# driver.find_element(*Five_button).click() - не всегда срабатывает. поэтому оформила через wait
    # проверим, снялось ли выделение кнопки (чекбокса) Five
Five_unclicked = driver.find_element(*Five_button).get_attribute("class")
assert "active" not in Five_unclicked, 'Снять выделение кнопки (чекбокса) Five:  не выполнено!'
time.sleep(2)

    # снимем выделение кнопки One
wait.until(EC.element_to_be_clickable(One_button))
# driver.find_element(*One_button).click() - не всегда срабатывает. поэтому оформила через wait
    # проверим, снялось ли выделение кнопки (чекбокса) One
One_unclicked = driver.find_element(*One_button).get_attribute("class")
assert "active" not in One_unclicked, 'Снять выделение кнопки (чекбокса) One:  не выполнено!'
time.sleep(2)

    # выполним проверку снятия выдеелния методом is_selected()
print(driver.find_element(*One_unclicked).is_selected())
print(driver.find_element(*Five_unclicked).is_selected())