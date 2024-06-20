import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
    # импортируем класс Select
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

        # Страница для работы
driver.get("http://the-internet.herokuapp.com/dropdown")
    # напишем локатор для селектора - он реализован через тэг <select>
select_locator = ("xpath", "//select[@id='dropdown']")
    # создадим объект выпадающего списка DropDown - внутрь класса Select поместим веб-элемент (локатор для селектора)
DropDown = Select(driver.find_element(*select_locator))     # теперь DROPDOWN будет восприниматься Selenium’ом,
                                                            # как элемент выпадающего списка, и позволит работать с ним
time.sleep(2)
    # Выбор элемента по содержимому text
DropDown.deselect_by_visible_text('Option 2')
    # Выбор элемента по index
DropDown.select_by_index(2)
    # Выбор элемента по value - наиболее приемлем
DropDown.select_by_value('')
    # Выбор всех элементов
print(DropDown.options)
