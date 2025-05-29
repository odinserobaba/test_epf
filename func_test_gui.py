import logging
from HttpRequest import *  # Импортируем класс HttpRequest
import time
import json  # Для обработки JSON данных
from datetime import date
from test_utils import *
from logs import *
import uuid


def cat_print(q):
    cat = """
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
    """
    return cat

# Функция получения токена


def test_gui(q):
    """
    Выполняет запрос для получения токена авторизации.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f'{cat_print("")}')
    logger.debug('------------------------Получение токена')
    q.setup['steps']=['label','test_label']