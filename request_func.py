import logging
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

def get_outside_request(q):
    """
    Выполняет запрос для Получение Заданий.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f"[get_outside_request]------------------------Получение Заданий {q.setup['2037']}")

    # Формируем HTTP-запрос для получения токена
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        url=f"/api-lc-license/dashboard/license/request/check/outside_request/{q.setup['2037']}",  # URL для получения токена
        headers={  # Заголовки запроса
            'accept': '*/*',  # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    # Сохраняем полученный токен в настройках очереди запросов

    resp = json.loads(response[2])
    outside_request_id = [x['id'] for x in resp]
    q.setup['outside_request_id']= outside_request_id


    logger.info(f'[get_outside_request] Задания номера: {[f"{x} " for x in outside_request_id]} \n')
    # logger.info(f'Первое задание {test_utils.print_pretty_json(list(response[2])[0])}')
    mess = f'''
* Шаг№{q.setup['current_method_index']} получаем  Задания
{{{{collapse(Получение Получение Заданий)
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    {response[2]}
    </pre>
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
    q.write_to_file(mess, q.file_name)
    return response[2]  # Возвращаем токен