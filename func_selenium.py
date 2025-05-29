import logging
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Настройка логгера
logger = logging.getLogger(__name__)


def load_local_storage(driver: webdriver.Chrome, base_url: str) -> webdriver.Chrome:
    """
    Загружает данные из JSON-файла в localStorage браузера
    """
    logger.info(f"Начало загрузки данных в localStorage для {base_url}")
    
    # Переход на целевую страницу для активации домена
    driver.get(f"https://{base_url}/")
    time.sleep(1)  # Краткая пауза для инициализации страницы

    try:
        # Чтение данных из JSON-файла
        with open('/media/nuanred/backup/license_eng/storage/local.json', 'r', encoding='utf-8') as file:
            storage_data = json.load(file)
            logger.debug(f"Прочитано {len(storage_data)} записей из local.json")

        # Запись данных в localStorage
        for key, value in storage_data.items():
            # Преобразование значений к строковому формату
            str_value = str(value).lower() if isinstance(value, bool) else str(value)
            
            # Формирование JS-команды
            script = f"localStorage.setItem('{key}', '{str_value}');"
            driver.execute_script(script)
            logger.debug(f"Записано в localStorage: {key} = {str_value}")

        # Верификация записанных данных
        verification_script = "return JSON.stringify(localStorage);"
        stored_data = driver.execute_script(verification_script)
        logger.info(f"Данные в localStorage: {stored_data[:200]}...")  # Логируем первые 200 символов

    except Exception as error:
        logger.error(f"Ошибка при работе с localStorage: {str(error)}")
        raise

    return driver


def initialize_webdriver() -> Options:
    """
    Инициализация настроек браузера
    """
    chrome_options = Options()
    
    # Базовые настройки
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.page_load_strategy = 'normal'
    
    # Настройки безопасности
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--disable-web-security')
    
    # Опция для сохранения открытого браузера после выполнения
    chrome_options.add_experimental_option("detach", True)
    
    # Раскомментировать для headless-режима
    # chrome_options.add_argument("--headless=new")
    
    return chrome_options


def get_start_lk(q) -> None:
    """
    Основная функция инициализации браузера и работы с ЛК
    """
    logger.debug("Инициализация сессии браузера")
    
    # Получение базового URL из конфигурации
    base_url = q.setup['base_url']
    logger.info(f"Работа с базовым URL: {base_url}")

    try:
        # Инициализация драйвера
        driver = webdriver.Chrome(
            service=Service(),
            options=initialize_webdriver()
        )

        # Загрузка данных в localStorage
        driver = load_local_storage(driver, base_url)

        # Основная навигация
        logger.debug("Переход на целевую страницу")
        driver.get(f"https://{base_url}/cabinet/news/all")
        
        # Принудительное обновление страницы
        driver.refresh()
        logger.info("Страница успешно обновлена")

    except Exception as error:
        logger.error(f"Критическая ошибка инициализации: {str(error)}")
        raise

    finally:
        # Сохранение драйвера в контекст
        q.setup['driver'] = driver
        logger.info("Драйвер успешно сохранен в setup")

        # Дополнительные действия при необходимости
        # driver.delete_all_cookies()
        # driver.execute_script("window.localStorage.clear();")


if __name__ == "__main__":
    # Пример использования (для тестирования)
    class MockQ:
        setup = {'base_url': 'example.com'}
    
    get_start_lk(MockQ())