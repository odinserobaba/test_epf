import datetime
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright import *
import logging
from HttpRequest import *  # Импортируем класс HttpRequest
import time
import json  # Для обработки JSON данных
from datetime import date
from test_utils import *
from logs import *
import uuid

def create_license(q):

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('create_license Добавляем заявление о выдаче ПХП_СХП')
    def run(playwright: Playwright) -> None:
        # Запуск браузера
        browser = playwright.firefox.launch(
            headless=False, proxy={"server": "socks5://127.0.0.1:1080"})
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Переход на страницу авторизации
        page.goto(
            "http://delotc.fsrar.ru/DELEC/CoreHost/auth/login?ReturnUrl=%2fDELEC%2f")
        page.get_by_placeholder("Логин").click()
        page.get_by_placeholder("Логин").fill("SYSLICENCE")
        page.get_by_placeholder("Пароль").click()
        page.get_by_placeholder("Пароль").fill("SYSLICENCE")
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("button", name="Продолжить").click()
        logger.debug('create_license Входим на страницу')
        # Переход на страницу документа
        today = date.today() # 27.02.2025
        date_string = today.strftime('%d.%m.%Y') # '%Y-%m-%d'
        # page.goto("http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF{%22dg%22:%220.LLGJ.LLGZ.LLH1.%22,%22kind_doc%22:%221%22,%22date%22:%2218.03.2025%22,%22inp%22:%220%22,%22sl%22:1}%D0%A7card_id%D0%AF0.2R58A.%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF")
        # Получаем текущую дату
        # current_date = datetime.now()

        # Форматируем дату в формат дд.мм.гггг
        formatted_date = date_string

        # Вставляем дату в URL
        url = (
            f"http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF"
            "{"
            "%22dg%22:%220.LLGJ.LLGZ.LLH1.%22,"
            "%22kind_doc%22:%221%22,"
            f"%22date%22:%22{formatted_date}%22,"
            "%22inp%22:%220%22,"
            "%22sl%22:1"
            "}"
            "%D0%A7card_id%D0%AF0.2R58A."
            "%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF"
        )
        logging.debug(f'url - {url}')
        page.goto(url)
        # Ожидание загрузки страницы
        page.wait_for_timeout(2000)

        # Открываем окно выбора файла
        page.locator(".toolbarAdd").click()
        page.get_by_text("Загрузить файл").click()
        logger.debug('create_license Загружаем файл')
        # Загружаем файл
        page.locator("input[type='file']").set_input_files(
            "/home/nuanred/1.pdf")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        with page.expect_popup() as page3_info:
            page.get_by_title("Добавить получателя").click()
        page3 = page3_info.value
        page3.locator("span").filter(
            has_text="Афанасенко Е.Г. - Заместитель руков").click()
        page3.get_by_role("link", name="Выбрать").click()
        page3.close()
        logger.debug('create_license Добавить получателя')
        with page.expect_popup() as page4_info:
            page.get_by_title("Добавить корреспондента").click()
        page4 = page4_info.value
        page4.get_by_text("ЦИ", exact=True).click()
        page4.locator("span").filter(
            has_text="АО \"ЦентрИнформ\" (а/я 149)").click()
        page4.get_by_title("Отметить все/Снять все отметки").click()
        page4.get_by_role("link", name="Выбрать").click()
        page4.close()
        page.locator("a").filter(has_text="Рубрики").click()
        logger.debug('create_license Рубрики')
        with page.expect_popup() as page5_info:
            page.get_by_title("Добавить рубрику").click()
        page5 = page5_info.value
        page5.get_by_text("ПРОИЗВОДСТВО", exact=True).click()
        page5.locator("span").filter(
            has_text="Производство, хранение и поставки п").click()
        page5.get_by_role("link", name="Выбрать").click()
        page5.close()
        logger.debug('create_license Регистрировать')
        # Регистрируем документ
        page.get_by_text("Регистрировать").click()
        page.wait_for_timeout(5000)

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)

def extension_license(q):

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('create_license Добавляем заявление о выдаче ПХП_СХП')
    def run(playwright: Playwright) -> None:
        # Запуск браузера
        browser = playwright.firefox.launch(
            headless=False, proxy={"server": "socks5://127.0.0.1:1080"})
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Переход на страницу авторизации
        page.goto(
            "http://delotc.fsrar.ru/DELEC/CoreHost/auth/login?ReturnUrl=%2fDELEC%2f")
        page.get_by_placeholder("Логин").click()
        page.get_by_placeholder("Логин").fill("SYSLICENCE")
        page.get_by_placeholder("Пароль").click()
        page.get_by_placeholder("Пароль").fill("SYSLICENCE")
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("button", name="Продолжить").click()
        logger.debug('create_license Входим на страницу')
        # Переход на страницу документа
        today = date.today() # 27.02.2025
        date_string = today.strftime('%d.%m.%Y') # '%Y-%m-%d'
        # page.goto("http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF{%22dg%22:%220.LLGJ.LLGZ.LLH1.%22,%22kind_doc%22:%221%22,%22date%22:%2218.03.2025%22,%22inp%22:%220%22,%22sl%22:1}%D0%A7card_id%D0%AF0.2R58A.%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF")
        # Получаем текущую дату
        # current_date = datetime.now()

        # Форматируем дату в формат дд.мм.гггг
        formatted_date = date_string

        # Вставляем дату в URL
        url = (
            f"http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF"
            "{"
            "%22dg%22:%220.LLGJ.LLGZ.LLH3.%22,"
            "%22kind_doc%22:%221%22,"
            f"%22date%22:%22{formatted_date}%22,"
            "%22inp%22:%220%22,"
            "%22sl%22:1"
            "}"
            "%D0%A7card_id%D0%AF0.2R58A."
            "%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF"
        )
        logging.debug(f'url - {url}')
        page.goto(url)
        # Ожидание загрузки страницы
        page.wait_for_timeout(2000)

        # Открываем окно выбора файла
        page.locator(".toolbarAdd").click()
        page.get_by_text("Загрузить файл").click()
        logger.debug('create_license Загружаем файл')
        # Загружаем файл
        page.locator("input[type='file']").set_input_files(
            "/home/nuanred/1.pdf")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        with page.expect_popup() as page3_info:
            page.get_by_title("Добавить получателя").click()
        page3 = page3_info.value
        page3.locator("span").filter(
            has_text="Афанасенко Е.Г. - Заместитель руков").click()
        page3.get_by_role("link", name="Выбрать").click()
        page3.close()
        logger.debug('create_license Добавить получателя')
        with page.expect_popup() as page4_info:
            page.get_by_title("Добавить корреспондента").click()
        page4 = page4_info.value
        page4.get_by_text("ЦИ", exact=True).click()
        page4.locator("span").filter(
            has_text="АО \"ЦентрИнформ\" (а/я 149)").click()
        page4.get_by_title("Отметить все/Снять все отметки").click()
        page4.get_by_role("link", name="Выбрать").click()
        page4.close()
        page.locator("a").filter(has_text="Рубрики").click()
        logger.debug('create_license Рубрики')
        with page.expect_popup() as page5_info:
            page.get_by_title("Добавить рубрику").click()
        page5 = page5_info.value
        page5.get_by_text("ПРОИЗВОДСТВО", exact=True).click()
        page5.locator("span").filter(
            has_text="Производство, хранение и поставки п").click()
        page5.get_by_role("link", name="Выбрать").click()
        page5.close()
        logger.debug('create_license Регистрировать')
        # Регистрируем документ
        page.get_by_text("Регистрировать").click()
        page.wait_for_timeout(5000)

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)

def create_license_from_req(q):
    reg_type={'0.LLGJ.LLGZ.LLH1.':'Заявление о выдаче лицензии',
    '0.LLGJ.LLGZ.LLH3.':'Заявление о продлении лицензии',
    '0.LLGJ.LLGZ.LLH5.':'Заявление о переоформлении лицензии',
    '0.LLGJ.LLGZ.LLH7.':'Заявление о прекращении действия лицензии'}
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    lic =q.setup['lic']
    logger.debug(f'create_license Добавляем {reg_type[lic]}')
    def run(playwright: Playwright,lic) -> None:
        # Запуск браузера
        browser = playwright.firefox.launch(
            headless=True, proxy={"server": "socks5://127.0.0.1:1080"})
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Переход на страницу авторизации
        page.goto(
            "http://delotc.fsrar.ru/DELEC/CoreHost/auth/login?ReturnUrl=%2fDELEC%2f")
        page.get_by_placeholder("Логин").click()
        page.get_by_placeholder("Логин").fill("SYSLICENCE")
        page.get_by_placeholder("Пароль").click()
        page.get_by_placeholder("Пароль").fill("SYSLICENCE")
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("button", name="Продолжить").click()
        logger.debug('create_license Входим на страницу')
        # Переход на страницу документа
        today = date.today() # 27.02.2025
        date_string = today.strftime('%d.%m.%Y') # '%Y-%m-%d'
        # page.goto("http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF{%22dg%22:%220.LLGJ.LLGZ.LLH1.%22,%22kind_doc%22:%221%22,%22date%22:%2218.03.2025%22,%22inp%22:%220%22,%22sl%22:1}%D0%A7card_id%D0%AF0.2R58A.%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF")
        # Получаем текущую дату
        # current_date = datetime.now()

        # Форматируем дату в формат дд.мм.гггг
        formatted_date = date_string

        # Вставляем дату в URL
        url = (
            f"http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF"
            "{"
            f"%22dg%22:%22{lic}%22,"
            "%22kind_doc%22:%221%22,"
            f"%22date%22:%22{formatted_date}%22,"
            "%22inp%22:%220%22,"
            "%22sl%22:1"
            "}"
            "%D0%A7card_id%D0%AF0.2R58A."
            "%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF"
        )
        logging.debug(f'url - {url}')
        page.goto(url)
        # Ожидание загрузки страницы
        page.wait_for_timeout(2000)

        # Открываем окно выбора файла
        page.locator(".toolbarAdd").click()
        page.get_by_text("Загрузить файл").click()
        logger.debug('create_license Загружаем файл')
        # Загружаем файл
        page.locator("input[type='file']").set_input_files(
            "/home/nuanred/1.pdf")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        with page.expect_popup() as page3_info:
            page.get_by_title("Добавить получателя").click()
        page3 = page3_info.value
        page3.locator("span").filter(
            has_text="Афанасенко Е.Г. - Заместитель руков").click()
        page3.get_by_role("link", name="Выбрать").click()
        page3.close()
        logger.debug('create_license Добавить получателя')
        with page.expect_popup() as page4_info:
            page.get_by_title("Добавить корреспондента").click()
        page4 = page4_info.value
        page4.get_by_text("ЦИ", exact=True).click()
        page4.locator("span").filter(
            has_text="АО \"ЦентрИнформ\" (а/я 149)").click()
        page4.get_by_title("Отметить все/Снять все отметки").click()
        page4.get_by_role("link", name="Выбрать").click()
        page4.close()
        page.locator("a").filter(has_text="Рубрики").click()
        logger.debug('create_license Рубрики')
        with page.expect_popup() as page5_info:
            page.get_by_title("Добавить рубрику").click()
        page5 = page5_info.value
        page5.get_by_text("ПРОИЗВОДСТВО", exact=True).click()
        page5.locator("span").filter(
            has_text="Производство, хранение и поставки п").click()
        page5.get_by_role("link", name="Выбрать").click()
        page5.close()
        logger.debug('create_license Регистрировать')
        # Регистрируем документ
        page.get_by_text("Регистрировать").click()
        page.wait_for_timeout(5000)

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright,lic=lic)

def create_license_from_req(q):
    reg_type={'0.LLGJ.LLGZ.LLH1.':'Заявление о выдаче лицензии',
    '0.LLGJ.LLGZ.LLH3.':'Заявление о продлении лицензии',
    '0.LLGJ.LLGZ.LLH5.':'Заявление о переоформлении лицензии',
    '0.LLGJ.LLGZ.LLH7.':'Заявление о прекращении действия лицензии'}
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    lic =q.setup['lic']
    logger.debug(f'create_license Добавляем {reg_type[lic]}')
    def run(playwright: Playwright,lic) -> None:
        # Запуск браузера
        browser = playwright.firefox.launch(
            headless=True, proxy={"server": "socks5://127.0.0.1:1080"})
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Переход на страницу авторизации
        page.goto(
            "http://delotc.fsrar.ru/DELEC/CoreHost/auth/login?ReturnUrl=%2fDELEC%2f")
        page.get_by_placeholder("Логин").click()
        page.get_by_placeholder("Логин").fill("SYSLICENCE")
        page.get_by_placeholder("Пароль").click()
        page.get_by_placeholder("Пароль").fill("SYSLICENCE")
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("button", name="Продолжить").click()
        logger.debug('create_license Входим на страницу')
        # Переход на страницу документа
        today = date.today() # 27.02.2025
        date_string = today.strftime('%d.%m.%Y') # '%Y-%m-%d'
        # page.goto("http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF{%22dg%22:%220.LLGJ.LLGZ.LLH1.%22,%22kind_doc%22:%221%22,%22date%22:%2218.03.2025%22,%22inp%22:%220%22,%22sl%22:1}%D0%A7card_id%D0%AF0.2R58A.%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF")
        # Получаем текущую дату
        # current_date = datetime.now()

        # Форматируем дату в формат дд.мм.гггг
        formatted_date = date_string

        # Вставляем дату в URL
        url = (
            f"http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF"
            "{"
            f"%22dg%22:%22{lic}%22,"
            "%22kind_doc%22:%221%22,"
            f"%22date%22:%22{formatted_date}%22,"
            "%22inp%22:%220%22,"
            "%22sl%22:1"
            "}"
            "%D0%A7card_id%D0%AF0.2R58A."
            "%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF"
        )
        logging.debug(f'url - {url}')
        page.goto(url)
        # Ожидание загрузки страницы
        page.wait_for_timeout(2000)

        # Открываем окно выбора файла
        page.locator(".toolbarAdd").click()
        page.get_by_text("Загрузить файл").click()
        logger.debug('create_license Загружаем файл')
        # Загружаем файл
        page.locator("input[type='file']").set_input_files(
            "/home/nuanred/1.pdf")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        with page.expect_popup() as page3_info:
            page.get_by_title("Добавить получателя").click()
        page3 = page3_info.value
        page3.locator("span").filter(
            has_text="Афанасенко Е.Г. - Заместитель руков").click()
        page3.get_by_role("link", name="Выбрать").click()
        page3.close()
        logger.debug('create_license Добавить получателя')
        with page.expect_popup() as page4_info:
            page.get_by_title("Добавить корреспондента").click()
        page4 = page4_info.value
        page4.get_by_text("ЦИ", exact=True).click()
        page4.locator("span").filter(
            has_text="АО \"ЦентрИнформ\" (а/я 149)").click()
        page4.get_by_title("Отметить все/Снять все отметки").click()
        page4.get_by_role("link", name="Выбрать").click()
        page4.close()
        page.locator("a").filter(has_text="Рубрики").click()
        logger.debug('create_license Рубрики')
        with page.expect_popup() as page5_info:
            page.get_by_title("Добавить рубрику").click()
        page5 = page5_info.value
        page5.get_by_text("ПРОИЗВОДСТВО", exact=True).click()
        page5.locator("span").filter(
            has_text="Производство, хранение и поставки п").click()
        page5.get_by_role("link", name="Выбрать").click()
        page5.close()
        logger.debug('create_license Регистрировать')
        # Регистрируем документ
        page.get_by_text("Регистрировать").click()
        page.wait_for_timeout(5000)

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright,lic=lic)

def create_license_from_req_ip(q):
    reg_type={'0.LLGJ.LLGZ.LLH1.':'Заявление о выдаче лицензии',
    '0.LLGJ.LLGZ.LLH3.':'Заявление о продлении лицензии',
    '0.LLGJ.LLGZ.LLH5.':'Заявление о переоформлении лицензии',
    '0.LLGJ.LLGZ.LLH7.':'Заявление о прекращении действия лицензии'}
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    lic =q.setup['lic']
    logger.debug(f'create_license Добавляем {reg_type[lic]}')
    def run(playwright: Playwright,lic) -> None:
        # Запуск браузера
        browser = playwright.firefox.launch(
            headless=True, proxy={"server": "socks5://127.0.0.1:1080"})
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Переход на страницу авторизации
        page.goto(
            "http://delotc.fsrar.ru/DELEC/CoreHost/auth/login?ReturnUrl=%2fDELEC%2f")
        page.get_by_placeholder("Логин").click()
        page.get_by_placeholder("Логин").fill("SYSLICENCE")
        page.get_by_placeholder("Пароль").click()
        page.get_by_placeholder("Пароль").fill("SYSLICENCE")
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("button", name="Продолжить").click()
        logger.debug('create_license Входим на страницу')
        # Переход на страницу документа
        today = date.today() # 27.02.2025
        date_string = today.strftime('%d.%m.%Y') # '%Y-%m-%d'
        # page.goto("http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF{%22dg%22:%220.LLGJ.LLGZ.LLH1.%22,%22kind_doc%22:%221%22,%22date%22:%2218.03.2025%22,%22inp%22:%220%22,%22sl%22:1}%D0%A7card_id%D0%AF0.2R58A.%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF")
        # Получаем текущую дату
        # current_date = datetime.now()

        # Форматируем дату в формат дд.мм.гггг
        formatted_date = date_string

        # Вставляем дату в URL
        url = (
            f"http://delotc.fsrar.ru/DELEC/WebRc/DOC_RC/DOC_RC.aspx#regParams%D0%AF"
            "{"
            f"%22dg%22:%22{lic}%22,"
            "%22kind_doc%22:%221%22,"
            f"%22date%22:%22{formatted_date}%22,"
            "%22inp%22:%220%22,"
            "%22sl%22:1"
            "}"
            "%D0%A7card_id%D0%AF0.2R58A."
            "%D0%A7cabinet_id%D0%AF4743715%D0%A7current_dl%D0%AF"
        )
        logging.debug(f'url - {url}')
        page.goto(url)
        # Ожидание загрузки страницы
        page.wait_for_timeout(2000)

        # Открываем окно выбора файла
        page.locator(".toolbarAdd").click()
        page.get_by_text("Загрузить файл").click()
        logger.debug('create_license Загружаем файл')
        # Загружаем файл
        page.locator("input[type='file']").set_input_files(
            "/home/nuanred/1.pdf")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        page.keyboard.press("Escape")
        with page.expect_popup() as page3_info:
            page.get_by_title("Добавить получателя").click()
        page3 = page3_info.value
        page3.locator("span").filter(
            has_text="Афанасенко Е.Г. - Заместитель руков").click()
        page3.get_by_role("link", name="Выбрать").click()
        page3.close()
        logger.debug('create_license Добавить получателя')
        with page.expect_popup() as page4_info:
            page.get_by_title("Добавить корреспондента").click()
        page4 = page4_info.value
        page4.get_by_text("ИП", exact=True).click()
        page4.locator("span").filter(
            has_text="ИП Попова Д. А.").click()
        page4.get_by_title("Отметить все/Снять все отметки").click()
        page4.get_by_role("link", name="Выбрать").click()
        page4.close()
        page.locator("a").filter(has_text="Рубрики").click()
        logger.debug('create_license Рубрики')
        with page.expect_popup() as page5_info:
            page.get_by_title("Добавить рубрику").click()
        page5 = page5_info.value
        page5.get_by_text("ПРОИЗВОДСТВО", exact=True).click()
        page5.locator("span").filter(
            has_text="Производство, хранение и поставки п").click()
        page5.get_by_role("link", name="Выбрать").click()
        page5.close()
        logger.debug('create_license Регистрировать')
        # Регистрируем документ
        page.get_by_text("Регистрировать").click()
        page.wait_for_timeout(5000)

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright,lic=lic)
        
        
        
      
        
        
        
        
