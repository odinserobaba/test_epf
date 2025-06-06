import io
import re

import logging
import re
from playwright.sync_api import Playwright, sync_playwright, expect


import test_utils
from HttpRequest import *  # Импортируем класс HttpRequest
import time
import json  # Для обработки JSON данных
from datetime import date
from test_utils import *
from logs import *
import pandas as pd
import uuid
from jsonschema import validate,ValidationError

def set_info_pl(playwright: Playwright,request_id) -> None:
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[set_info_pl]-----=====/////Установка доп инфо/////=====-----")
    browser =  playwright.chromium.launch(
        headless=False,  # Запуск браузера в режиме с графическим интерфейсом
        #slow_mo=50,  # Замедление выполнения для наглядности
        args=[
            '--start-maximized'  # Запуск браузера в максимальном размере окна
            # '--disable-infobars',  # Отключение информационных панелей
            # '--disable-notifications',  # Отключение уведомлений
            # '--lang=en-US',  # Установка языка браузера
        ]
    )
    context =  browser.new_context()
    page =  context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    logger.debug('[set_info_pl]  page.goto("https://lk-test.egais.ru/dev")')
    page.goto("https://lk-test.egais.ru/dev")
    page.get_by_label("Login *").click()
    page.get_by_label("Login *").fill("wageworker")
    logger.debug('[set_info_pl]  Login')
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill("GetMeT0kenPlease-246")
    logger.debug('[set_info_pl]  Password')
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="").click()
    logger.debug(f'[set_info_pl]  Переход на страницу с заявлением')
    page.goto(f"https://lk-test.egais.ru/cabinet/licenses/inProcess/{request_id}")
    page.get_by_role("button", name="Продолжить").click()
    page.locator(".mat-checkbox-inner-container").first.click()
    page.locator("#mat-checkbox-2 > .mat-checkbox-layout > .mat-checkbox-inner-container").click()
    page.locator("#mat-checkbox-3 > .mat-checkbox-layout > .mat-checkbox-inner-container").click()
    page.get_by_placeholder("Номер виноградного насаждения").click()
    page.get_by_placeholder("Номер виноградного насаждения").fill("11111111111111111")
    page.locator("form").filter(has_text="Данные для запроса в Минсельхоз").get_by_role("button").click()
    page.get_by_role("button", name="Сохранить", exact=True).click()
    logger.debug(f'[set_info_pl]  Доп инфо успешно установлено')
    # ---------------------
    context.close()
    browser.close()

def set_vos(playwright: Playwright,request_id) -> None:
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[set_vos]-----=====/////Установка ВОС/////=====-----")
    browser =  playwright.chromium.launch(
        headless=True,  # Запуск браузера в режиме с графическим интерфейсом
        #slow_mo=5,  # Замедление выполнения для наглядности
        args=[
            '--start-maximized'  # Запуск браузера в максимальном размере окна
            '--disable-infobars',  # Отключение информационных панелей
            '--disable-notifications',  # Отключение уведомлений
            # '--lang=en-US',  # Установка языка браузера
        ]
    )
    context =  browser.new_context()
    page =  context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    logger.debug('[set_vos]  page.goto("https://lk-test.egais.ru/dev")')
    page.goto("https://lk-test.egais.ru/dev")
    page.get_by_label("Login *").click()
    page.get_by_label("Login *").fill("wageworker")
    logger.debug('[set_vos]  Login')
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill("GetMeT0kenPlease-246")
    logger.debug('[set_vos]  Password')
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="").click()

    #-----=====     Переход к заявлению     =====-----
    page.goto(f"https://lk-test.egais.ru/cabinet/licenses/inProcess/{request_id}")
    logger.debug('[set_info_pl]  Переход к заявлению')
    page.get_by_role("tab", name="Приказ").click()
    logger.debug('[set_info_pl]  Приказ')
    page.get_by_text("Акт", exact=True).click()
    logger.debug('[set_info_pl]  Акт')
    page.get_by_text("Задание", exact=True).click()
    logger.debug('[set_info_pl]  Задание')
    # # ---- Задание
    # # -----=====     Адреса мест ведения деятельности$     =====-----
    # page.locator("div").filter(has_text=re.compile(r"^Адреса мест ведения деятельности$")).nth(1).click()
    # logger.debug('[set_info_pl]  Задание - Адреса мест ведения деятельности')
    # page.get_by_role("option", name=re.compile(r"Республика Крым")).locator("span").click()
    # page.get_by_role("button", name="").click()
    # logger.debug('[set_info_pl]  Задание - Адреса мест ведения деятельности  Республика Крым 91')
    # # -----=====     Адреса мест ведения деятельности$     =====-----
    # logger.debug('[set_info_pl]  Задание - Межрегиональное управление *')
    # page.get_by_role("combobox", name="Межрегиональное управление").locator("span").click()
    # page.get_by_role("option", name="МРУ по ЦФО").locator("span").click()
    #
    # # -----=====     Информация, по     =====-----
    # logger.debug('[set_info_pl]  Задание - Информация, по *')
    # page.locator("form div").filter(has_text=re.compile(r"Информация, по")).nth(1).click()
    # page.get_by_role("option", name="сведения о месте нахождения крестьянского (фермерского хозяйства);").locator(
    #     "mat-pseudo-checkbox").click()
    # page.keyboard.press('Escape')
    #
    # # -----=====     Приложение к акту     =====-----
    # logger.debug('[set_info_pl]  Задание - Приложение к акту *')
    #
    # page.locator('form div').filter(has_text=re.compile(r"Приложение к акту")).nth(2).click()
    # logger.debug('[set_info_pl]  Задание - перечень установленного организацией основного технологического оборудования для ')
    # page.get_by_role("option",
    #                  name="копии сертификатов соответствия или деклараций о соответствии на основное технол").nth(1).locator(
    #     "span").click()
    #
    # # page.locator("#mat-option-27").nth(1).click()
    # page.keyboard.press('Escape')
    # logger.debug('[set_info_pl]  Задание - нажали на - перечень оборудования ')
    #
    # # -----=====     Срок предоставления до *    =====-----
    # logger.debug('[set_info_pl]  Задание - Срок предоставления до *')
    # page.keyboard.press('Escape')
    # # page.locator("div").filter(has_text=re.compile(r"Срок предоставления до")).nth(2).click()
    # #
    # # logger.debug('[set_info_pl]  Задание - Открываем выбор дат для срока предоставления ')
    # # # today = page.locator(".today")
    # # # today.click()О
    # page.get_by_role("textbox", name="Срок предоставления до").fill("2025-06-05")
    #
    # # -----=====     Задание - Сохранить как черновик    =====-----
    # logger.debug('[set_info_pl]  Задание - Сохранить как черновик*')
    # page.get_by_role("button", name="Сохранить как черновик").click()

    # -----=====     Приказ    =====-----
    # logger.debug('[set_info_pl]  Приказ')
    # page.get_by_role("tab", name="Приказ").click()
    # page.locator("form div").filter(has_text=re.compile(r"Адреса мест ведения деятельности")).nth(2).click()
    # # page.locator("mat-pseudo-checkbox").click()
    # logger.debug('[set_info_pl]  Адреса мест ведения деятельности')
    # page.get_by_role("option", name="Республика Крым 91").locator("span").click()
    # page.keyboard.press('Escape')
    # logger.debug('[set_info_pl]  БАХЧИСАРАЙСКИЙ')
    # page.get_by_role("textbox", name="ФИО сотрудника, уполномоченного на проведение оценки соответствия").click()
    # page.get_by_role("textbox", name="ФИО сотрудника, уполномоченного на проведение оценки соответствия").fill("123")
    # logger.debug('[set_info_pl]  ФИО сотрудника')
    # page.get_by_role("textbox", name="ФИО эксперта").click()
    # page.get_by_role("textbox", name="ФИО эксперта").fill("123")
    # logger.debug('[set_info_pl]  ФИО эксперта')
    # page.get_by_role("textbox", name="Задачи настоящей оценки").click()
    # page.get_by_role("textbox", name="Задачи настоящей оценки").fill("123")
    # logger.debug('[set_info_pl]  Задачи настоящей оценки')
    # page.get_by_role("spinbutton", name="Срок проведения оценки").click()
    # page.get_by_role("spinbutton", name="Срок проведения оценки").fill("01")
    # logger.debug('[set_info_pl]  Срок проведения оценки')
    # page.get_by_role("textbox", name="Дата начала проведения оценки соответствия").fill("2025-05-05")
    # page.get_by_role("textbox", name="Дата конца проведения оценки соответствия").fill("2025-05-05")
    # page.get_by_role("textbox", name="Иные нормативные акты").click()
    # page.get_by_role("textbox", name="Иные нормативные акты").fill("test")
    # page.get_by_role("button", name="Сохранить как черновик").click()
    # logger.debug('[set_info_pl]  Приказ - Сохранить как черновик*')
    # -----=====     Акт    =====-----
    logger.debug('[set_info_pl]  АКТ')
    page.get_by_text("Акт", exact=True).click()
    logger.debug('[set_info_pl]  Адреса мест ведения деятельности')
    page.locator("form div").filter(has_text=re.compile(r"Адреса мест ведения деятельности")).nth(2).click()
    logger.debug('[set_info_pl]  Адреса мест ведения деятельности Республика Крым 91')
    page.get_by_role("option", name="Республика Крым 91").locator("span").click()
    page.keyboard.press('Escape')
    logger.debug('[set_info_pl]  Дата и время составления акта')
    page.get_by_role("textbox", name="Дата и время составления акта").click()
    page.get_by_role("textbox", name="Дата и время составления акта").fill("2025-05-05T00:00")
    logger.debug('[set_info_pl]  Общая продолжительность оценки (дней)')
    page.get_by_role("spinbutton", name="Общая продолжительность оценки (дней)").click()
    page.get_by_role("spinbutton", name="Общая продолжительность оценки (дней)").fill("1")
    logger.debug('[set_info_pl]  Общая продолжительность оценки Часов:Минут ')
    page.get_by_role("textbox", name="Часов:Минут").click()
    page.get_by_role("textbox", name="Часов:Минут").fill("00:00")
    logger.debug('[set_info_pl]  Дата проведения оценки ')
    page.get_by_role("textbox", name="Дата проведения оценки").fill("2025-12-01")
    logger.debug('[set_info_pl]  Время начала ')
    page.get_by_role("textbox", name="Время начала").click()
    page.get_by_role("textbox", name="Время начала").fill("00:00")
    logger.debug('[set_info_pl]  Время окончания ')
    page.get_by_role("textbox", name="Время окончания").click()
    page.get_by_role("textbox", name="Время окончания").fill("00:09")
    logger.debug('[set_info_pl]  ФИО заявителя ')
    page.get_by_role("textbox", name="ФИО заявителя").click()
    page.get_by_role("textbox", name="ФИО заявителя").fill("Туров Флор Феликсович")
    logger.debug('[set_info_pl]  ФИО проводящего оценку соответствия * ')
    page.locator("form div").filter(has_text="ФИО проводящего оценку соответствия *").nth(3).click()
    page.get_by_role("textbox", name="ФИО проводящего оценку соответствия").fill("Шубин Карл Владиславович")
    logger.debug('[set_info_pl]  Должность проводящего оценку соответствия ')
    page.get_by_role("textbox", name="Должность проводящего оценку соответствия").click()
    page.get_by_role("textbox", name="Должность проводящего оценку соответствия").fill("Проверяющий МРУ0")
    logger.debug('[set_info_pl]  Должность проводящего оценку соответствия ')
    page.get_by_role("textbox", name="Номер сопроводительного письма").click()
    page.get_by_role("textbox", name="Номер сопроводительного письма").fill("№14321 от 2025-01-02  \ 23421")
    logger.debug('[set_info_pl]  Дата сопроводительного письма ')
    page.get_by_role("textbox", name="Дата сопроводительного письма").fill("2025-05-05")
    logger.debug('[set_info_pl]  Дата и время получения уведомления и приказа')
    page.get_by_role("textbox", name="Дата и время получения уведомления и приказа").click()
    page.get_by_role("textbox", name="Дата и время получения уведомления и приказа").fill("2025-05-05T00:00")
    logger.debug('[set_info_pl]  Марка и модель аппарата')
    page.get_by_role("textbox", name="Марка и модель аппарата").click()
    page.get_by_role("textbox", name="Марка и модель аппарата").fill("САМСУНГ ГАЛАКСИЕ 42")
    logger.debug('[set_info_pl]  Заметки сотрудника МРУ')
    page.get_by_role("textbox", name="Заметки сотрудника МРУ").click()
    page.get_by_role("textbox", name="Заметки сотрудника МРУ").fill("Нет заметок")
    logger.debug('[set_info_pl]  Возражения заявителя')
    page.get_by_role("textbox", name="Возражения заявителя").click()
    page.get_by_role("textbox", name="Возражения заявителя").fill("Без возражений")
    logger.debug('[set_info_pl]  Сохранить как черновик')
    page.get_by_role("button", name="Сохранить как черновик").click()

    # ---------------------
    context.close()
    browser.close()

def set_vos_order(playwright: Playwright,request_id) -> None:
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[set_vos]-----=====/////Установка ВОС/////=====-----")
    browser =  playwright.chromium.launch(
        headless=True,  # Запуск браузера в режиме с графическим интерфейсом
        #slow_mo=5,  # Замедление выполнения для наглядности
        args=[
            '--start-maximized'  # Запуск браузера в максимальном размере окна
            '--disable-infobars',  # Отключение информационных панелей
            '--disable-notifications',  # Отключение уведомлений
            # '--lang=en-US',  # Установка языка браузера
        ]
    )
    context =  browser.new_context()
    page =  context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    logger.debug('[set_vos]  page.goto("https://lk-test.egais.ru/dev")')
    page.goto("https://lk-test.egais.ru/dev")
    page.get_by_label("Login *").click()
    page.get_by_label("Login *").fill("wageworker")
    logger.debug('[set_vos]  Login')
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill("GetMeT0kenPlease-246")
    logger.debug('[set_vos]  Password')
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="").click()

    #-----=====     Переход к заявлению     =====-----
    page.goto(f"https://lk-test.egais.ru/cabinet/licenses/inProcess/{request_id}")
    logger.debug('[set_info_pl]  Переход к заявлению')
    page.get_by_role("tab", name="Приказ").click()
    logger.debug('[set_info_pl]  Приказ')
    page.get_by_text("Акт", exact=True).click()
    logger.debug('[set_info_pl]  Акт')
    page.get_by_text("Задание", exact=True).click()
    logger.debug('[set_info_pl]  Задание')

    # -----=====     Приказ    =====-----
    logger.debug('[set_info_pl]  Приказ')
    page.get_by_role("tab", name="Приказ").click()
    page.locator("form div").filter(has_text=re.compile(r"Адреса мест ведения деятельности")).nth(2).click()

    logger.debug('[set_info_pl]  Адреса мест ведения деятельности')
    page.get_by_role("option", name="Республика Крым 91").locator("span").click()
    page.keyboard.press('Escape')
    logger.debug('[set_info_pl]  БАХЧИСАРАЙСКИЙ')
    page.get_by_role("textbox", name="ФИО сотрудника, уполномоченного на проведение оценки соответствия").click()
    page.get_by_role("textbox", name="ФИО сотрудника, уполномоченного на проведение оценки соответствия").fill("Тихонов Гордий Агафонович")
    logger.debug('[set_info_pl]  ФИО сотрудника')
    page.get_by_role("textbox", name="ФИО эксперта").click()
    page.get_by_role("textbox", name="ФИО эксперта").fill("123")
    logger.debug('[set_info_pl]  ФИО эксперта')
    page.get_by_role("textbox", name="Задачи настоящей оценки").click()
    page.get_by_role("textbox", name="Задачи настоящей оценки").fill("Егоров Артем Владленович")
    logger.debug('[set_info_pl]  Задачи настоящей оценки')
    page.get_by_role("spinbutton", name="Срок проведения оценки").click()
    page.get_by_role("spinbutton", name="Срок проведения оценки").fill("1")
    logger.debug('[set_info_pl]  Срок проведения оценки')
    page.get_by_role("textbox", name="Дата начала проведения оценки соответствия").fill("2025-05-05")
    page.get_by_role("textbox", name="Дата конца проведения оценки соответствия").fill("2025-05-05")
    page.get_by_role("textbox", name="Иные нормативные акты").click()
    page.get_by_role("textbox", name="Иные нормативные акты").fill("ГОСТ 2143")
    page.get_by_role("button", name="Сохранить как черновик").click()
    logger.debug('[set_info_pl]  Приказ - Сохранить как черновик*')

    # ---------------------
    context.close()
    browser.close()

def set_vos_request(playwright: Playwright,request_id) -> None:
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[set_vos]-----=====/////Установка ВОС/////=====-----")
    browser =  playwright.chromium.launch(
        headless=True,  # Запуск браузера в режиме с графическим интерфейсом
        #slow_mo=5,  # Замедление выполнения для наглядности
        args=[
            '--start-maximized'  # Запуск браузера в максимальном размере окна
            '--disable-infobars',  # Отключение информационных панелей
            '--disable-notifications',  # Отключение уведомлений
            # '--lang=en-US',  # Установка языка браузера
        ]
    )
    context =  browser.new_context()
    page =  context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    logger.debug('[set_vos]  page.goto("https://lk-test.egais.ru/dev")')
    page.goto("https://lk-test.egais.ru/dev")
    page.get_by_label("Login *").click()
    page.get_by_label("Login *").fill("wageworker")
    logger.debug('[set_vos]  Login')
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill("GetMeT0kenPlease-246")
    logger.debug('[set_vos]  Password')
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="").click()

    #-----=====     Переход к заявлению     =====-----
    page.goto(f"https://lk-test.egais.ru/cabinet/licenses/inProcess/{request_id}")
    logger.debug('[set_info_pl]  Переход к заявлению')
    page.get_by_role("tab", name="Приказ").click()
    logger.debug('[set_info_pl]  Приказ')
    page.get_by_text("Акт", exact=True).click()
    logger.debug('[set_info_pl]  Акт')
    page.get_by_text("Задание", exact=True).click()
    logger.debug('[set_info_pl]  Задание')
    # ---- Задание
    # -----=====     Адреса мест ведения деятельности$     =====-----
    page.locator("div").filter(has_text=re.compile(r"^Адреса мест ведения деятельности$")).nth(1).click()
    logger.debug('[set_info_pl]  Задание - Адреса мест ведения деятельности')
    page.get_by_role("option", name=re.compile(r"Республика Крым")).locator("span").click()
    page.get_by_role("button", name="").click()
    logger.debug('[set_info_pl]  Задание - Адреса мест ведения деятельности  Республика Крым 91')
    # -----=====     Адреса мест ведения деятельности$     =====-----
    logger.debug('[set_info_pl]  Задание - Межрегиональное управление *')
    page.get_by_role("combobox", name="Межрегиональное управление").locator("span").click()
    page.get_by_role("option", name="МРУ по ЦФО").locator("span").click()

    # -----=====     Информация, по     =====-----
    logger.debug('[set_info_pl]  Задание - Информация, по *')
    page.locator("form div").filter(has_text=re.compile(r"Информация, по")).nth(1).click()
    page.get_by_role("option", name="сведения о месте нахождения крестьянского (фермерского хозяйства);").locator(
        "mat-pseudo-checkbox").click()
    page.keyboard.press('Escape')

    # -----=====     Приложение к акту     =====-----
    logger.debug('[set_info_pl]  Задание - Приложение к акту *')

    page.locator('form div').filter(has_text=re.compile(r"Приложение к акту")).nth(2).click()
    logger.debug('[set_info_pl]  Задание - перечень установленного организацией основного технологического оборудования для ')
    page.get_by_role("option",
                     name="копии сертификатов соответствия или деклараций о соответствии на основное технол").nth(1).locator(
        "span").click()
    # page.locator("#mat-option-27").nth(1).click()
    page.keyboard.press('Escape')
    logger.debug('[set_info_pl]  Задание - нажали на - перечень оборудования ')
    # -----=====     Срок предоставления до *    =====-----
    logger.debug('[set_info_pl]  Задание - Срок предоставления до *')
    page.keyboard.press('Escape')
    page.get_by_role("textbox", name="Срок предоставления до").fill("2025-06-05")

    # -----=====     Задание - Сохранить как черновик    =====-----
    logger.debug('[set_info_pl]  Задание - Сохранить как черновик*')
    page.get_by_role("button", name="Сохранить как черновик").click()
    # ---------------------
    context.close()
    browser.close()

def set_vos_exec(playwright: Playwright,request_id) -> None:
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[set_vos]-----=====/////Установка ВОС/////=====-----")
    browser =  playwright.chromium.launch(
        headless=True,  # Запуск браузера в режиме с графическим интерфейсом
        #slow_mo=5,  # Замедление выполнения для наглядности
        args=[
            '--start-maximized'  # Запуск браузера в максимальном размере окна
            '--disable-infobars',  # Отключение информационных панелей
            '--disable-notifications',  # Отключение уведомлений
            # '--lang=en-US',  # Установка языка браузера
        ]
    )
    context =  browser.new_context()
    page =  context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    logger.debug('[set_vos]  page.goto("https://lk-test.egais.ru/dev")')
    page.goto("https://lk-test.egais.ru/dev")
    page.get_by_label("Login *").click()
    page.get_by_label("Login *").fill("wageworker")
    logger.debug('[set_vos]  Login')
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill("GetMeT0kenPlease-246")
    logger.debug('[set_vos]  Password')
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="").click()

    #-----=====     Переход к заявлению     =====-----
    page.goto(f"https://lk-test.egais.ru/cabinet/licenses/inProcess/{request_id}")
    logger.debug('[set_info_pl]  Переход к заявлению')
    page.get_by_role("tab", name="Приказ").click()
    logger.debug('[set_info_pl]  Приказ')
    page.get_by_text("Акт", exact=True).click()
    logger.debug('[set_info_pl]  Акт')
    page.get_by_text("Задание", exact=True).click()
    logger.debug('[set_info_pl]  Задание')

    # -----=====     Акт    =====-----
    logger.debug('[set_info_pl]  АКТ')
    page.get_by_text("Акт", exact=True).click()
    logger.debug('[set_info_pl]  Адреса мест ведения деятельности')
    page.locator("form div").filter(has_text=re.compile(r"Адреса мест ведения деятельности")).nth(2).click()
    logger.debug('[set_info_pl]  Адреса мест ведения деятельности Республика Крым 91')
    page.get_by_role("option", name="Республика Крым 91").locator("span").click()
    page.keyboard.press('Escape')
    logger.debug('[set_info_pl]  Дата и время составления акта')
    page.get_by_role("textbox", name="Дата и время составления акта").click()
    page.get_by_role("textbox", name="Дата и время составления акта").fill("2025-05-05T00:00")
    logger.debug('[set_info_pl]  Общая продолжительность оценки (дней)')
    page.get_by_role("spinbutton", name="Общая продолжительность оценки (дней)").click()
    page.get_by_role("spinbutton", name="Общая продолжительность оценки (дней)").fill("1")
    logger.debug('[set_info_pl]  Общая продолжительность оценки Часов:Минут ')
    page.get_by_role("textbox", name="Часов:Минут").click()
    page.get_by_role("textbox", name="Часов:Минут").fill("00:00")
    logger.debug('[set_info_pl]  Дата проведения оценки ')
    page.get_by_role("textbox", name="Дата проведения оценки").fill("2025-12-01")
    logger.debug('[set_info_pl]  Время начала ')
    page.get_by_role("textbox", name="Время начала").click()
    page.get_by_role("textbox", name="Время начала").fill("00:00")
    logger.debug('[set_info_pl]  Время окончания ')
    page.get_by_role("textbox", name="Время окончания").click()
    page.get_by_role("textbox", name="Время окончания").fill("00:09")
    logger.debug('[set_info_pl]  ФИО заявителя ')
    page.get_by_role("textbox", name="ФИО заявителя").click()
    page.get_by_role("textbox", name="ФИО заявителя").fill("Туров Флор Феликсович")
    logger.debug('[set_info_pl]  ФИО проводящего оценку соответствия * ')
    page.locator("form div").filter(has_text="ФИО проводящего оценку соответствия *").nth(3).click()
    page.get_by_role("textbox", name="ФИО проводящего оценку соответствия").fill("Шубин Карл Владиславович")
    logger.debug('[set_info_pl]  Должность проводящего оценку соответствия ')
    page.get_by_role("textbox", name="Должность проводящего оценку соответствия").click()
    page.get_by_role("textbox", name="Должность проводящего оценку соответствия").fill("Проверяющий МРУ0")
    logger.debug('[set_info_pl]  Должность проводящего оценку соответствия ')
    page.get_by_role("textbox", name="Номер сопроводительного письма").click()
    page.get_by_role("textbox", name="Номер сопроводительного письма").fill("№14321 от 2025-01-02  \ 23421")
    logger.debug('[set_info_pl]  Дата сопроводительного письма ')
    page.get_by_role("textbox", name="Дата сопроводительного письма").fill("2025-05-05")
    logger.debug('[set_info_pl]  Дата и время получения уведомления и приказа')
    page.get_by_role("textbox", name="Дата и время получения уведомления и приказа").click()
    page.get_by_role("textbox", name="Дата и время получения уведомления и приказа").fill("2025-05-05T00:00")
    logger.debug('[set_info_pl]  Марка и модель аппарата')
    page.get_by_role("textbox", name="Марка и модель аппарата").click()
    page.get_by_role("textbox", name="Марка и модель аппарата").fill("САМСУНГ ГАЛАКСИЕ 42")
    logger.debug('[set_info_pl]  Заметки сотрудника МРУ')
    page.get_by_role("textbox", name="Заметки сотрудника МРУ").click()
    page.get_by_role("textbox", name="Заметки сотрудника МРУ").fill("Нет заметок")
    logger.debug('[set_info_pl]  Возражения заявителя')
    page.get_by_role("textbox", name="Возражения заявителя").click()
    page.get_by_role("textbox", name="Возражения заявителя").fill("Без возражений")
    logger.debug('[set_info_pl]  Сохранить как черновик')
    page.get_by_role("button", name="Сохранить как черновик").click()

    # ---------------------
    context.close()
    browser.close()

def playwright_set_info(q):
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[playwright_set_info]------------------------Установка доп инфо")
    request_id = q.setup['request_id']
    if request_id:
        with sync_playwright() as playwright:
            set_info_pl(playwright,request_id)
    else:
        logger.error(f"[playwright_set_info]------------------------НЕТ request_id")
    return 0

def playwright_set_vos(q):
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[playwright_set_vos]------------------------Установка ВОС")
    request_id = q.setup['request_id']
    if request_id:
        with sync_playwright() as playwright:
            set_vos(playwright,request_id)
    else:
        logger.error(f"[playwright_set_vos]------------------------НЕТ request_id")
    return 0

def playwright_set_vos_request(q):
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[playwright_set_vos]------------------------Установка ВОС")
    request_id = q.setup['request_id']
    if request_id:
        with sync_playwright() as playwright:
            set_vos_request(playwright,request_id)
    else:
        logger.error(f"[playwright_set_vos]------------------------НЕТ request_id")
    return 0

def playwright_set_vos_order(q):
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[playwright_set_vos]------------------------Установка ВОС")
    request_id = q.setup['request_id']
    if request_id:
        with sync_playwright() as playwright:
            set_vos_order(playwright,request_id)
    else:
        logger.error(f"[playwright_set_vos]------------------------НЕТ request_id")
    return 0

def playwright_set_vos_exec(q):
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[playwright_set_vos]------------------------Установка ВОС")
    request_id = q.setup['request_id']
    if request_id:
        with sync_playwright() as playwright:
            set_vos_exec(playwright,request_id)
    else:
        logger.error(f"[playwright_set_vos]------------------------НЕТ request_id")
    return 0




