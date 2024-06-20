import time
import os

from selenium import webdriver
    # Инициализация драйвера.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

    # выгрузка файлов использует pref oпции для изменения дирректории загрузок по умолчанию, поэтому
    # инициализирем ChromOptions и добавим их в driver

chrom_options = webdriver.ChromeOptions()
    # создадим словарь для создания специфичной настройки браузера: дирректории для скачивания
preferences = {
    'download.default_directory': f'{os.getcwd()}/files/downloads'
}
    # указываем браузеру, куда по дефолту нужно сохранять файлы
chrom_options.add_experimental_option("prefs", preferences)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrom_options)

        # Загрузка файлов
# в проекте необходимо предварительно создать папку Uploads с файлами, которые мы планируем загрузить на сайт
    # Открыть страницу сайта
elem = driver.get('https://demoqa.com/upload-download')
time.sleep(3)
    # Записываем поле ввода в переменную
upload_file_field = driver.find_element('xpath', "//input[@id='uploadFile']")
    # загружаем файл на сайт (файл берется из папки данного проекта /files/uploads/Screen1.png, а
    # f'{os.getcwd()} определяет абсолютный путь до папки проекта files)

upload_file_field.send_keys(f'{os.getcwd()}/files/uploads/Screen1.png')
time.sleep(3)
    # отображение названия загружаемого файла рядом с кнопкой загрузки свидетельствует об успешной загрузке


        # Скачивание файлов
# в проекте необходимо предварительно создать папку Downloads, в которую будем скачивать файлы и к которой укажем
# путь скачивания файлов для этого проекта

    # откроем файл с прямыми ссылками для скачивания (файлы скачиваются по клику)
#driver.get('http://the-internet.herokuapp.com/download')
    # найдем третий элемент из списка всех ссылок на сайте [3]
#element = driver.find_elements('xpath', '//a')[3]
#time.sleep(3)
#element.click()
#time.sleep(3)
    # в папке downloads добавится скачанный файл

        # Задание. С помощью цикла for скачать с 4го по 7й включительно файлы в папку downloads.
        # Страница для выполнения задания: http://the-internet.herokuapp.com/download

    # откроем сайт с прямыми ссылками для скачивания (файлы скачиваются по клику)
driver.get('https://the-internet.herokuapp.com/download')
url = driver.current_url
print(f"URL страницы: {url}")
assert url == 'https://the-internet.herokuapp.com/download', 'Ошибка в URL, открыта не та страница'


els = driver.find_elements('xpath', '//a')[4:8]
count = 0
count_links = len(els)
print(f'Всего ссылок для скачивания: {count_links}')
for href in els:
    link_text = href.get_attribute('text')
    print(f'Скачивание файла - {link_text}')
    href.click()
    time.sleep(3)
    count += 1
assert count_links == 4, 'Количество не соответствует'
time.sleep(3)