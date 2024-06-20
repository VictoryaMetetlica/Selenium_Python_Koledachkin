import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features+AutomationControlled")
driver = webdriver.Chrome(service=service, options=chrome_options)

    # 1 - Открываем 3 вкладки
for _ in range(2):
    driver.switch_to.new_window("tab")
time.sleep(2)
    # Получаем список открытых вкладок (дескрипторы)
opened_handles = driver.window_handles
handle_one = opened_handles[0]
handle_two = opened_handles[1]
handle_three = opened_handles[2]

    # 2 - В открытых вкладках переходим на указанные страницы:
link_one = "https://hyperskill.org/login"
link_two = "https://www.avito.ru/"
link_three = "https://oz.by/"

driver.switch_to.window(handle_one)
driver.get(link_one)
time.sleep(2)

driver.switch_to.window(handle_two)
driver.get(link_two)
time.sleep(2)

driver.switch_to.window(handle_three)
driver.get(link_three)
time.sleep(2)

    # 3 - Выводим в терминал title каждой страницы
for handle in opened_handles:
    driver.switch_to.window(handle)
    print(driver.title)

    # 4 - Кликаем на любую кнопку или ссылку на каждой странице
driver.switch_to.window(handle_one)
assert handle_one == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)
driver.find_element("xpath", "//button[text()='Start for free']").click()
assert driver.current_url != link_one, "Переход по клику НЕ произвелся"
time.sleep(2)

driver.switch_to.window(handle_two)
assert handle_two == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)
driver.find_element("xpath", "//a[@data-marker='header/login-button']").click()
assert driver.current_url != link_two, "Переход по клику НЕ произвелся"
time.sleep(2)

driver.switch_to.window(handle_three)
assert handle_three == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)
driver.find_element("xpath", "//a[@href='/help']").click()
assert driver.current_url != link_three, "Переход по клику НЕ произвелся"
time.sleep(2)