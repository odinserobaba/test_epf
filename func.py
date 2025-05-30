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
def cat_print_best_cat(q):
    cat = '''
           _
       \`*-.
        )  _`-.
       .  : `. .
       : _   '  \
       ; *` _.   `*-._
       `-.-'          `-.
         ;       `       `.
         :.       .        \
         . \  .   :   .-'   .
         '  `+.;  ;  '      :
         :  '  |    ;       ;-.
         ; '   : :`-:     _.`* ;
      .*' /  .*' ; .*`- +'  `*'
      `*-*   `*-*  `*-*'
    '''
# Функция настройки логгера
def setup_logger(q):
    """
    Настраивает логгер для записи сообщений в файл и вывода их в консоль.

    :param log_file_path: Путь к файлу журнала
    :return: Логгер
    """
    logger = logging.getLogger()  # Получаем корневой логгер
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования DEBUG

    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler(q.logs_folder+'log.log')
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')  # Формат сообщения
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Создаем обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

def cat_print(q):
    cat = """
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
    """
    return cat
# Функция получения токена
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
#
#     resp = json.loads(response[2])
#     outside_request_id = [x['id'] for x in resp]
#     q.setup['outside_request_id']= outside_request_id
#
#
#     logger.info(f'[get_outside_request] Задания номера: {[f"{x} " for x in outside_request_id]} \n')
#     # logger.info(f'Первое задание {test_utils.print_pretty_json(list(response[2])[0])}')
#     mess = f'''
# * Шаг№{q.setup['current_method_index']} получаем  Задания
# {{{{collapse(Получение Получение Заданий)
#     <pre>
#     {q.setup["base_url"]}
#     {response[0]}
#     {response[1]}
#     {response[2]}
#     </pre>
# }}}}
#     '''
#     q.write_to_file(mess, q.file_name)
#     if response[0]==200:
#         mess = '%{color:green}Успешно!%'
#     else:
#         mess = '%{color:red}Ошибка!%'
#     q.write_to_file(mess, q.file_name)
#     return response[2]  # Возвращаем токен

def get_outside_request_checks(q):
    """
    Выполняет запрос для Получение Заданий.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """
    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('[get_outside_request_checks] ------------------------Получение Заданий')
    # Формируем HTTP-запрос для получения токена
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        url=f"/api-lc-license/dashboard/license/request/check/outside_request/checks/{q.setup['2037']}",  # URL для получения токена
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


    logger.info(f'[get_outside_request_checks] Задания номера: {outside_request_id} \n')
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

def set_outside_request(q):
    """
    Выполняет запрос для установки Задания.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('[set_outside_request]------------------------Установка Задания')

    func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/checks/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения расширенных данных
    with open('json_epgu/outside_request.json', 'r', encoding='utf-8') as file:
        payload = json.load(file)


    payload['id'] = q.setup['outside_request_id']
    payload['checkId']= q.setup['2037']
    json_string = json.dumps(payload, ensure_ascii=False, indent=4)
    json_string_single_quotes = json_string.replace('"', "'")
    logger.debug(f'[set_outside_request] Payload POST \n {json_string}')
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='POST',                  # Метод GET
        # URL для получения расширенных данных
        url=func_url,
        body=json.dumps(payload),
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        })
    logger.info(f'[set_outside_request] Отправляем в Задания {request} \n')
    response = request.execute()  # Выполняем запрос
    # Сохраняем полученный токен в настройках очереди запросов
    logger.info(f'[set_outside_request] Ответ  {response} \n')

def get_outside_order(q):
    """
    Выполняет запрос для Получение Приказов.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('------------------------Получение Приказов')

    # Формируем HTTP-запрос для получения токена
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        url=f"/api-lc-license/dashboard/license/request/check/outside_order/all/{q.setup['2038']}",  # URL для получения токена
        headers={  # Заголовки запроса
            'accept': '*/*',  # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    # Сохраняем полученный токен в настройках очереди запросов

    resp = json.loads(response[2])
    outside_order_id = [x['id'] for x in resp]
    q.setup['outside_order_id']= outside_order_id


    logger.info(f'Приказы номера: {[f"{x}" for x in outside_order_id]} \n')
    # logger.info(f'Первое задание {test_utils.print_pretty_json(list(response[2])[0])}')
    mess = f'''
* Шаг№{q.setup['current_method_index']} получаем  номера Приказов
{{{{collapse(Получение Приказов)
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

def set_outside_order(q):
    """
    Выполняет запрос для установки Приказа.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('[set_outside_order]------------------------Установка Приказов')

    func_url = f"/api-lc-license/dashboard/license/request/check/outside_order/{q.setup['2038']}"
    # Формируем HTTP-запрос для получения расширенных данных
    with open('json_epgu/outside_request.json', 'r', encoding='utf-8') as file:
        payload = json.load(file)

    payload['id'] = q.setup['outside_order_id']
    payload['checkId']= q.setup['2038']
    payload['outsideRequestId']=q.setup['outside_request_id']
    logger.info(f'q.setup outside_order_id {q.setup["outside_order_id"]}')
    logger.info(f'payload id = {payload["id"]} checkId {payload["checkId"]}')
    json_string = json.dumps(payload, ensure_ascii=False, indent=4)
    json_string_single_quotes = json_string.replace('"', "'")
    logger.debug(f'[set_outside_order] Payload POST \n {payload}')
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='POST',                  # Метод GET
        # URL для получения расширенных данных
        url=func_url,
        body=json.dumps(payload),
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        })
    logger.info(f'[set_outside_order] Отправляем в Приказ {request} \n')
    response = request.execute()  # Выполняем запрос
    # Сохраняем полученный токен в настройках очереди запросов
    logger.info(f'[set_outside_order] Ответ  {response} \n')

def set_outside_exec(q):
    """
    Выполняет запрос для установки АКТА.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug('[set_outside_exec]------------------------Установка АКТА')

    func_url = f"/api-lc-license/dashboard/license/request/check/outside_exec/{q.setup['2039']}"
    # Формируем HTTP-запрос для получения расширенных данных
    with open('json_epgu/outside_exec.json', 'r', encoding='utf-8') as file:
        payload = json.load(file)


    payload['checkId']= q.setup['2039']
    payload['outsideRequestId']=q.setup['outside_request_id'][0]
    logger.info(f'q.setup outside_request_id {q.setup["outside_request_id"][0]}')
    logger.info(f'payload id = {payload["id"]} checkId {payload["checkId"]}')
    json_string = json.dumps(payload, ensure_ascii=False, indent=4)
    json_string_single_quotes = json_string.replace('"', "'")
    logger.debug(f'[set_outside_exec] Payload POST \n {payload}')
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='POST',                  # Метод GET
        # URL для получения расширенных данных
        url=func_url,
        body=json.dumps(payload),
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        })
    logger.info(f'[set_outside_exec] Отправляем в АКТ {request} \n')
    response = request.execute()  # Выполняем запрос
    # Сохраняем полученный токен в настройках очереди запросов
    logger.info(f'[set_outside_exec] Ответ  {response} \n')

def get_token(q):
    """
    Выполняет запрос для получения токена авторизации.

    :param q: Экземпляр класса RequestQueue
    :return: Токен авторизации
    """

    logger = logging.getLogger(__name__)  # Получаем логгер текущего модуля
    logger.debug(f'{cat_print("")}')
    logger.debug('------------------------Получение токена')

    # Формируем HTTP-запрос для получения токена
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        url="/api-lc-license/tools/token?role=developer",  # URL для получения токена
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Указываем, что принимаем любой формат ответа
            'Content-Type': 'application/json'  # Тип содержимого запроса
        }
    )

    response = request.execute()  # Выполняем запрос
    # Сохраняем полученный токен в настройках очереди запросов
    q.setup['token'] = response[2]
    mess = f'''
* Шаг№{q.setup['current_method_index']} получаем токен
{{{{collapse(Получение токена)
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
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    return response[2]  # Возвращаем токен
# Функция получения расширенных данных по запросу
def get_extended(q):
    """
    Выполняет запрос для получения расширенных данных по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Получение extended {q.setup["request_id"]}')
    func_url = f"/api-lc-license/dashboard/license/request/{q.setup['request_id']}/extended"
    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения расширенных данных
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    checks = json.loads(response[2])  # Преобразуем ответ в JSON объект
    logs_uuid = str(uuid.uuid4())
    # Логируем информацию о проверках
    logger.debug(checks)
    logger.debug(f'------------------------> Проверки по заявлению')
    logger.debug(f'------------------------')
    for item in checks['checks']:
        logger.debug(f'| {item["checkId"]} | {item["code"]} | {item["checkStatus"]["code"]} |')
        q.setup[str(item["code"])] = item["checkId"]
    json_load = json.loads(response[2])
    mess = f'''
* Шаг№{q.setup['current_method_index']} Получение расширенной информации по заявлению
{{{{collapse(GET Расширенной информации по заявлению {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>
    uuid логов -> {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    
        # Пишем логи
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    return response[2]  # Возвращаем ответ сервера
# Функция получения информации по запросу
def copy_logs_to_folder(q):
    logger = logging.getLogger(__name__)
    logger.debug(
        f'Копирование логов ')
    today = date.today()
    date_string = today.strftime('%Y-%m-%d')
    path_sefl = '/home/nuanred/Downloads/logs'
    path_dockerhub = f'Serobaba@DockerHub:/home/Serobaba/logs/{date_string}'
    try:
        run_bash_command(f'scp -r {path_dockerhub} {path_sefl}')
    except Exception as e:
            logger.error(f'Ошибка при выполнении запроса: "{e}" ')
    logger.info(f'Логи скопированны в {path_sefl} из {path_dockerhub}')

def get_info(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Получение info {q.setup["request_id"]}')
    func_url = f"/api-lc-license/dashboard/license/request/{q.setup['request_id']}/info"
    # Формируем HTTP-запрос для получения информации
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения информации
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    info = json.loads(response[2])  # Преобразуем ответ в JSON объект
    logs_uuid = str(uuid.uuid4())
    # Логируем основную информацию
    logger.debug(f'{info["requestId"]}')
    logger.debug(f'{info["inn"]}')
    logger.debug(f'{info["kpp"]}')
    logger.debug(f'{info["orgNameBrief"]}')
    logger.debug(f'{info["orgNameFull"]}')
    json_load = json.loads(response[2])
    mess = f'''
* Шаг№{q.setup['current_method_index']} Получение информации по заявлению
{{{{collapse(GET Получение информации по заявлению {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>
    uuid логов -> {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    return response[2]  # Возвращаем ответ сервера

def get_info_to_redmine(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Получение info {q.setup["request_id"]}')
    func_url = f"/api-lc-license/dashboard/license/request/{q.setup['request_id']}/info"
    # Формируем HTTP-запрос для получения информации
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения информации
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    info = json.loads(response[2])  # Преобразуем ответ в JSON объект
    logs_uuid = str(uuid.uuid4())
    # Логируем основную информацию
    logger.debug(f'{info["requestId"]}')
    logger.debug(f'{info["inn"]}')
    logger.debug(f'{info["kpp"]}')
    logger.debug(f'{info["orgNameBrief"]}')
    logger.debug(f'{info["orgNameFull"]}')
    json_load = json.loads(response[2])
    mess = f'''
* Шаг№{q.setup['current_method_index']} {info["requestId"]} {info["orgNameBrief"]} {info["orgNameFull"]} {info["licenseType"]["shortName"]} fromEpgu {info["fromEpgu"]}
{{{{collapse(Информации по заявлению {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>
    uuid логов -> {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    return response[2]  # Возвращаем ответ сервера

def set_info(q):
    """
    Выполняет запрос для получения расширенных данных по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """


    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Установка  допинфо {q.setup["request_id"]}')
    func_url = f"/api-lc-license/dashboard/license/request/{q.setup['request_id']}/info"
    # Формируем HTTP-запрос для получения расширенных данных
    with open('payloads/info.json', 'r') as file:
        payload = json.load(file)
    payload['requestId'] = q.setup['request_id']
    logger.debug(f'Payload POST {payload}')
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='POST',                  # Метод GET
        # URL для получения расширенных данных
        url=func_url,
        body=json.dumps(payload),
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }


    )

    response = request.execute()  # Выполняем запрос
    logs_uuid = str(uuid.uuid4())
    mess = f'''
* Шаг№{q.setup['current_method_index']} Установка допинфо
{{{{collapse(POST Установка допинфо {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(payload, indent=4, ensure_ascii=False)}
    </code></pre>
    uuid логов -> {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    # Пишем логи
    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    return response[2]  # Возвращаем ответ сервера

def set_check2023(q):
    """Выставляет проверку 2023 в положительное решение

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """

    logger = logging.getLogger(__name__)
    code = '2023'
    logger.debug(
        f'------------------------Установка {code} проверки для {q.setup["request_id"]} {q.setup[code]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/check_code.json', 'r') as file:
        payload = json.load(file)
    logs_uuid = str(uuid.uuid4())
    # Обновляем значение checkId в payload
    payload['checkId'] = q.setup[code]
    # logger.debug(f'Payload PATCH {json.dumps(payload, separators=(',', ': '))}')

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='PATCH',
        url=func_url,
        body=json.dumps(payload, separators=(',', ': ')),
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': q.setup["token"]
        }
    )
    logs_uuid = str(uuid.uuid4())
    # Выполняем запрос
    response = request.execute()

    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']} Установка 2023 в положительное решение
{{{{collapse(PATCH Установка 2023 в положительное решение{func_url})
<pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
<pre><code class=\'json\'>\n{json.dumps(
            response[2], indent=4, ensure_ascii=False)}\n
uuid логов -> {logs_uuid}
</code></pre>
}}}}'''
    

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)

    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    # Возвращаем ответ сервера
    return response[2]

def set_check2002(q):
    """Выставляет проверку 2002 экспертизу документов в положительное решение

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    code = '2002'
    logger.debug(
        f'------------------------Установка {code} проверки для {q.setup["request_id"]} {q.setup[code]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/check_code.json', 'r') as file:
        payload = json.load(file)
    logs_uuid = str(uuid.uuid4())
    # Обновляем значение checkId в payload
    payload['checkId'] = q.setup[code]
    # logger.debug(f'Payload PATCH {json.dumps(payload, separators=(',', ': '))}')
    try:
        # Формируем HTTP-запрос для получения расширенных данных
        request = HttpRequest(
            base_url=q.setup["base_url"],
            method='PATCH',
            url=func_url,
            body=json.dumps(payload, separators=(',', ': ')),
            headers={
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'Authorization': q.setup["token"]
            }
        )

        # Выполняем запрос
        response = request.execute()
    except Exception as e:
        logger.error(f'Ошибка при выполнении запроса: "{e}" ')
    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']} Установка экспертизы документов в положительное решение
{{{{collapse(PATCH Установка экспертизы документов в положительное решение {func_url})
    <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
    <pre><code class=\'json\'>\n{json.dumps(
                payload, indent=4, ensure_ascii=False)}\n
uuid логов -> {logs_uuid}
</code></pre>
}}}}'''
    

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)

    # Возвращаем ответ сервера
    return response[2]

def set_check2002_negative(q):
    """Выставляет проверку 2002 экспертизу документов в отрицательное решение

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    code = '2002'
    logger.debug(
        f'------------------------Установка set_check2002_negative {code} проверки для {q.setup["request_id"]} {q.setup[code]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/"
    try:
        # Читаем содержимое файла payloads/check_code.json
        with open('payloads/check_code2002_negative.json', 'r') as file:
            payload = json.load(file)
        logs_uuid = str(uuid.uuid4())
        # Обновляем значение checkId в payload
        payload['checkId'] = q.setup[code]
        # logger.debug(f'Payload PATCH {json.dumps(payload, separators=(',', ': '))}')

        # Формируем HTTP-запрос для получения расширенных данных
        request = HttpRequest(
            base_url=q.setup["base_url"],
            method='PATCH',
            url=func_url,
            body=json.dumps(payload, separators=(',', ': ')),
            headers={
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'Authorization': q.setup["token"]
            }
        )

        # Выполняем запрос
        response = request.execute()
    except Exception as e:
        logger.error(f'Ошибка при выполнении запроса set_check2002_negative: "{e}" ')
    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']} Установка экспертизы документов в отрицательное
{{{{collapse(PATCH Установка экспертизы документов в отрицательное {func_url})
    <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
    <pre><code class=\'json\'>\n{json.dumps(
                payload, indent=4, ensure_ascii=False)}\n
    {response[1]}\n 
uuid логов -> {logs_uuid}
</code></pre>
}}}}'''
    

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)

    # Возвращаем ответ сервера
    return response[2]

def set_check2037(q):
    """Добавляет проверку 2037 

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    code = 2037
    logger.debug(
        f'------------------------set_check2037 2037 проверки для {q.setup["request_id"]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/add_check.json', 'r') as file:
        payload = json.load(file)
    logger.debug(
        f'------------------------Добавление payload {payload}'
    )
    # Обновляем значение checkId в payload
    payload['requestId'] = q.setup["request_id"]
    # logger.debug(f'Payload POST {json.dumps(payload, separators=(',', ': '))}')

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='POST',
        url=func_url,
        body=json.dumps(payload, separators=(',', ': ')),
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': q.setup["token"]
        }
    )

    # Выполняем запрос
    response = request.execute()

    json_load = json.loads(response[2])

    logs_uuid = str(uuid.uuid4())
    q.setup['id2037'] = json_load['checkId']
    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']} Добавление проверки 2037 к заявлению
{{{{collapse(POST Добавление проверки 2037 к заявлению {func_url})
        <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
        <pre><code class=\'json\'>\n{json.dumps(
            payload, indent=4, ensure_ascii=False)}\n
uuid логов -> {logs_uuid}
</code></pre>
}}}}'''
    

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    # Возвращаем ответ сервера
    return response[2]

def get_exercise_applicant_info2037(q):
    """
    Возвращает список возможных сведений о заявителе

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2037' in q.setup.keys():
        logger.debug(
            f'------------------------def get_exercise_applicant_info2037(q): {q.setup["request_id"]} {q.setup["2037"]}')
        func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/applicant_info/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения информации
        request = HttpRequest(
            base_url=q.setup["base_url"],  # Базовый URL
            method='GET',                  # Метод GET
            # URL для получения информации
            url=func_url,
            headers={                      # Заголовки запроса
                'accept': '*/*',           # Принимаем любой формат ответа
                'Content-Type': 'application/json',  # Тип содержимого запроса
                'authorization': q.setup["token"]  # Передаем токен авторизации
            }
        )

        response = request.execute()  # Выполняем запрос

        json_load = json.loads(response[2])
        json_load = json_load
        # x = json_load[0]
        # q.setup['id2037'] = x['id']
        mess = f'''
{{{{collapse(GET {func_url})
        <pre>
        {q.setup["base_url"]}
        {response[0]}
        {response[1]}
        </pre>
        <pre><code class='json'>
        {json.dumps(json_load, indent=4, ensure_ascii=False)}
        </code></pre>

}}}}
 '''
        q.write_to_file(mess, q.file_name)
        if response[0]==200:
            mess = '%{color:green}Успешно!%'
        else:
            mess = '%{color:red}Ошибка!%'
        # q.stop_flag==True
        q.write_to_file(mess, q.file_name)
    
        return response[2]  # Возвращаем ответ сервера
    else:
        logger.debug('2037 проверки нет')
        q.stop_flag = True

def generate_assignment(q):
    """
    Создает задание

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2037' in q.setup.keys():
        logger.debug(
            f'------------------------def generate_assignment(q): {q.setup["request_id"]} {q.setup["2037"]}')
        func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения информации
        request = HttpRequest(
            base_url=q.setup["base_url"],  # Базовый URL
            method='GET',                  # Метод GET
            # URL для получения информации
            url=func_url,
            headers={                      # Заголовки запроса
                'accept': '*/*',           # Принимаем любой формат ответа
                'Content-Type': 'application/json',  # Тип содержимого запроса
                'authorization': q.setup["token"]  # Передаем токен авторизации
            }
        )

        response = request.execute()  # Выполняем запрос

        json_load = json.loads(response[2])
        json_load = json_load
        x = json_load[0]
        q.setup['id2037'] = x['id']
        mess = f'''
{{{{collapse(GET Создаем задание {func_url})
        <pre>
        {q.setup["base_url"]}
        {response[0]}
        {response[1]}
        </pre>
        <pre><code class='json'>
        {json.dumps(json_load, indent=4, ensure_ascii=False)}
        </code></pre>

}}}}
        '''
        q.write_to_file(mess, q.file_name)
        if response[0]==200:
            mess = '%{color:green}Успешно!%'
        else:
            mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
        q.write_to_file(mess, q.file_name)
    
        return response[2]  # Возвращаем ответ сервера
    else:
        logger.debug('2037 проверки нет')
        q.stop_flag = True

def get_exercise_request_doc2037(q):
    """
    Получает список документов по заданию 

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2037' in q.setup.keys():
        logger.debug(
            f'------------------------def get_exercise_request_doc2037(q): {q.setup["request_id"]} {q.setup["2037"]}')
        func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/request_doc/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения информации
        request = HttpRequest(
            base_url=q.setup["base_url"],  # Базовый URL
            method='GET',                  # Метод GET
            # URL для получения информации
            url=func_url,
            headers={                      # Заголовки запроса
                'accept': '*/*',           # Принимаем любой формат ответа
                'Content-Type': 'application/json',  # Тип содержимого запроса
                'authorization': q.setup["token"]  # Передаем токен авторизации
            }
        )

        response = request.execute()  # Выполняем запрос

        json_load = json.loads(response[2])
        json_load = json_load
        x = json_load[0]
        q.setup['id2037'] = x['id']
        mess = f'''
{{{{collapse(GET {func_url})
        <pre>
        {q.setup["base_url"]}
        {response[0]}
        {response[1]}
        </pre>
        <pre><code class='json'>
        {json.dumps(json_load, indent=4, ensure_ascii=False)}
        </code></pre>

}}}}
        '''
        q.write_to_file(mess, q.file_name)
        if response[0]==200:
            mess = '%{color:green}Успешно!%'
        else:
            mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
        q.write_to_file(mess, q.file_name)
    
        return response[2]  # Возвращаем ответ сервера
    else:
        logger.debug('2037 проверки нет')
        q.stop_flag = True

def get_license(q):
    pass

def get_exercise_request_addresses2037(q):
    """
    Получает список адресов по заданию 
    
    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2037' in q.setup.keys():
        logger.debug(
            f'------------------------def get_exercise_request_addresses2037(q): {q.setup["request_id"]} {q.setup["2037"]}')
        func_url = f"/api-lc-license/dashboard/license/request/check/form_approve/addresses/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения информации
        request = HttpRequest(
            base_url=q.setup["base_url"],  # Базовый URL
            method='GET',                  # Метод GET
            # URL для получения информации
            url=func_url,
            headers={                      # Заголовки запроса
                'accept': '*/*',           # Принимаем любой формат ответа
                'Content-Type': 'application/json',  # Тип содержимого запроса
                'authorization': q.setup["token"]  # Передаем токен авторизации
            }
        )

        response = request.execute()  # Выполняем запрос

        json_load = json.loads(response[2])
        json_load = json_load
        # x = json_load[0]
        # q.setup['id2037'] = x['id']
        mess = f'''
{{{{collapse(GET {func_url})
        <pre>
        {q.setup["base_url"]}
        {response[0]}
        {response[1]}
        </pre>
        <pre><code class='json'>
        {json.dumps(json_load, indent=4, ensure_ascii=False)}
        </code></pre>

}}}}
        '''
        q.write_to_file(mess, q.file_name)
        if response[0]==200:
            mess = '%{color:green}Успешно!%'
        else:
            mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
        q.write_to_file(mess, q.file_name)
    
        return response[2]  # Возвращаем ответ сервера
    else:
        logger.debug('2037 проверки нет')
        q.stop_flag = True

def create_exercise2037(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.
    
    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2037' in q.setup.keys():
        logger.debug(
            f'------------------------def create_exercise2037(q): {q.setup["request_id"]} {q.setup["2037"]}')
        func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения информации
        request = HttpRequest(
            base_url=q.setup["base_url"],  # Базовый URL
            method='GET',                  # Метод GET
            # URL для получения информации
            url=func_url,
            headers={                      # Заголовки запроса
                'accept': '*/*',           # Принимаем любой формат ответа
                'Content-Type': 'application/json',  # Тип содержимого запроса
                'authorization': q.setup["token"]  # Передаем токен авторизации
            }
        )

        response = request.execute()  # Выполняем запрос

        mess = f'''
* Шаг№{q.setup['current_method_index']}  Установка задания 
{{{{collapse(GET Установка задания {func_url})
        <pre>
        {q.setup["base_url"]}
        {response[0]}
        {response[1]}
        </pre>

}}}}
        '''
        q.write_to_file(mess, q.file_name)
        if response[0]==200:
            mess = '%{color:green}Успешно!%'
        else:
            mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
        q.write_to_file(mess, q.file_name)
    
        # return response[2]  # Возвращаем ответ сервера
    else:
        logger.debug('2037 проверки нет')
        q.stop_flag = True
        
def get_exercise2037(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.
    
    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2037' in q.setup.keys():
        logger.debug(
            f'------------------------def get_exercise2037(q): {q.setup["request_id"]} {q.setup["2037"]}')
        func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/checks/{q.setup['2037']}"
    # Формируем HTTP-запрос для получения информации
        request = HttpRequest(
            base_url=q.setup["base_url"],  # Базовый URL
            method='GET',                  # Метод GET
            # URL для получения информации
            url=func_url,
            headers={                      # Заголовки запроса
                'accept': '*/*',           # Принимаем любой формат ответа
                'Content-Type': 'application/json',  # Тип содержимого запроса
                'authorization': q.setup["token"]  # Передаем токен авторизации
            }
        )

        response = request.execute()  # Выполняем запрос
        logs_uuid = str(uuid.uuid4())
        json_load = json.loads(response[2])
        json_load = json_load
        # x = json_load[0]
        # q.setup['id2037'] = x['id']
        mess = f'''
{{{{collapse(GET {func_url})
<pre>
{q.setup["base_url"]}
{response[0]}
{response[1]}
</pre>
<pre><code class='json'>
{json.dumps(json_load, indent=4, ensure_ascii=False)}
</code></pre>
log uuid {logs_uuid}

}}}}
        '''
        q.write_to_file(mess, q.file_name)
        if response[0]==200:
            mess = '%{color:green}Успешно!%'
        else:
            mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
        q.write_to_file(mess, q.file_name)
        get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
        get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    
        return response[2]  # Возвращаем ответ сервера
    else:
        logger.debug('2037 проверки нет')
        q.stop_flag = True

def set_exercise(q):
    """Выполняет запрос для получения расширенных данных по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    code = '2037'
    logger.debug(
        f'------------------------ set_exercise 2037 установка задания для {q.setup["request_id"]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/outside_request/{q.setup['2037']}"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/exercise.json', 'r') as file:
        payload = json.load(file)

    # Обновляем значение checkId в payload
    try:
        payload['id'] = q.setup['id2037']
        payload['checkId'] = q.setup['2037']
        payload['primaryKey'] = q.setup["id2037"]
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        payload['sendMaxDate'] = date_string
    except Exception as e:
        logger.error(f'Ошибка при выполнении запроса: {e}')
    # logger.debug(f'Payload POST {json.dumps(payload, separators=(',', ': '))}')

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='POST',
        url=func_url,
        body=json.dumps(payload, separators=(',', ': ')),
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': q.setup["token"]
        }
    )

    # Выполняем запрос
    response = request.execute()
    logs_uuid = str(uuid.uuid4())
    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']}  Установка задания 
{{{{collapse(POST {func_url})
<pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
<pre><code class=\'json\'>\n{json.dumps(
payload, indent=4, ensure_ascii=False)}\n
log uuid {logs_uuid}
</code></pre>
}}}}'''
    

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0] in ('200',200):
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)

    # Возвращаем ответ сервера
    return response[2]

def get_check_order2038(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.
    
    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------ set_exercise 2038 установка задания для {q.setup["request_id"]}'
    )
    func_url = f"/api-lc-license/dashboard/license/request/check/outside_order/all/{q.setup['2038']}"
    # Формируем HTTP-запрос для получения информации
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения информации
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )
    logs_uuid = str(uuid.uuid4())
    response = request.execute()  # Выполняем запрос
    json_load = json.loads(response[2])
    logger.info(f'{json_load}')

    x = json_load[0]
    q.setup['outside_order']=x['id']

    mess = f'''
* Шаг№{q.setup['current_method_index']} Получение id приказа
{{{{collapse(GET {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>

}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)

    return response[2]  # Возвращаем ответ сервера

def get_order2038(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.
    
    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    if '2038' in q.setup.keys():
        logger.debug(
            f'------------------------Получение проверки 2038 def get_order2038(q): {q.setup["request_id"]} {q.setup["2038"]}')
    else:
        logger.debug('2038 проверки нет')
    func_url = f"/api-lc-license/dashboard/license/request/check/outside_order/all/{q.setup['2038']}"
    # Формируем HTTP-запрос для получения информации
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения информации
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )
    logs_uuid = str(uuid.uuid4())
    response = request.execute()  # Выполняем запрос
    logger.debug(response)
    json_load = json.loads(response[2])
    logger.debug(f'json_load {json_load}')
    x = json_load[0]
    q.setup['id2038'] = x['id']
    mess = f'''
* Шаг№{q.setup['current_method_index']} Получение id приказа
{{{{collapse(GET {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>
log uuid {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)

    return response[2]  # Возвращаем ответ сервера

def set_order(q):
    """Установка приказа

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    code = '2038'
    logger.debug(
        f'------------------------ set_order 2038 установка приказа для {q.setup["request_id"]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/outside_order/{q.setup['2038']}"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/order.json', 'r') as file:
        payload = json.load(file)

    # Обновляем значение checkId в payload
    try:
        payload['id'] = q.setup['outside_order']
        payload['checkId'] = q.setup['2038']
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        payload['dateStart'] = date_string
        payload['dateEnd'] = date_string
        payload['outsideRequestId']=q.setup['outside_order']
    except Exception as e:
        logger.error(f'Ошибка при выполнении запроса: {e} {payload}')
    # logger.debug(f'Payload POST {json.dumps(payload, separators=(',', ': '))}')

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='POST',
        url=func_url,
        body=json.dumps(payload, separators=(',', ': ')),
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': q.setup["token"]
        }
    )
    logs_uuid = str(uuid.uuid4())
    # Выполняем запрос
    response = request.execute()

    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']} Отправка приказа
{{{{collapse(POST {func_url})
        <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
        <pre><code class=\'json\'>\n{json.dumps(payload, indent=4, ensure_ascii=False)}\n
        log uuid {logs_uuid}</code></pre>
}}}}'''
    
    # if 'id' in json.loads(response[2]).keys():
    #     q.setup["order_id"]=json.loads(response[2])['id']

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)

    # Возвращаем ответ сервера
    logger.debug(f'send 2038 {response}')
    return response

def info_q(q):
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------ info Q {q.setup}'
    )

def set_akt(q):
    """Выполняет запрос для получения расширенных данных по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    code = '2039'
    logger.debug(
        f'------------------------ set_order 2039 установка акта для {q.setup["request_id"]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/check/outside_exec/{q.setup['2039']}"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/akt.json', 'r') as file:
        payload = json.load(file)

    # Обновляем значение checkId в payload
    try:
        payload['id'] = q.setup['id2038']
        today = date.today()
        date_string = today.strftime('%Y-%m-%d')
        payload['actDateTime'] = str(payload['actDateTime']).replace('AAAAAA',date_string)
        payload['letterDate'] = date_string
        payload['noticeTs'] = str(payload['noticeTs']).replace('AAAAAA',date_string)
        payload['licenseOutsideExecDateTimes'][0]['dtStart'] = str(payload['licenseOutsideExecDateTimes'][0]['dtStart'] ).replace('AAAAAA',date_string)
        payload['licenseOutsideExecDateTimes'][0]['dtEnd'] = str(payload['licenseOutsideExecDateTimes'][0]['dtEnd'] ).replace('AAAAAA',date_string)
        payload['checkId']=q.setup["2039"]
        payload['outsideRequestId']=q.setup["id2038"]
    except Exception as e:
        logger.error(f'Ошибка при выполнении запроса: {e} {q.setup}')
    # logger.debug(f'Payload POST {json.dumps(payload, separators=(',', ': '))}')

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='POST',
        url=func_url,
        body=json.dumps(payload, separators=(',', ': ')),
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': q.setup["token"]
        }
    )
    logs_uuid = str(uuid.uuid4())
    # Выполняем запрос
    response = request.execute()
    logger.debug(f'response AKT {response}')
    # Формируем сообщение для записи в файл
#     mess =f'''
# * Шаг№{q.setup['current_method_index']} Установка акта
#         <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
#         <pre><code class=\'json\'>\n{json.dumps(payload, indent=4, ensure_ascii=False)}\n
#         log uuid {logs_uuid}</code></pre>
# }}}}'''
    

#     # Записываем сообщение в файл
#     q.write_to_file(mess, q.file_name)
#     if response[0]==200:
#         mess = '%{color:green}Успешно!%'
#     else:
#         mess = '%{color:red}Ошибка!%'
#         q.stop_flag==True
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    # q.write_to_file(mess, q.file_name)

    # Возвращаем ответ сервера
        # Возвращаем ответ сервера
    logger.debug(f'send 2039 {response}')
    return response

def process_json_files_to_csv(q):
    logger = logging.getLogger(__name__)
    process_json_files('/media/nuanred/backup/license_eng/out/jsons','/media/nuanred/backup/license_eng/out/out.csv')

def get_sed_files(q):
    logger = logging.getLogger(__name__)
    df = pd.read_csv('out/out1.csv',sep=',')
    logger.info(df)
    for index, row in df.iterrows():
        logger.info(index,row)
        column1_value = row['file']  # Replace 'Column1' with the actual column name
        column2_value = row['data']  # Replace 'Column2' with the actual column name
        input_test_query = f"""ssh Serobaba@DockerHub 'curl -s -X GET "http://10.10.5.202:5012/api/File/getFile?refFileIsn={column2_value}" -H "accept: application/json"' > '/media/nuanred/backup/license_eng/out/pdf/{column1_value}.pdf'"""
        
        logger.info('>  '+run_bash_command(input_test_query))
        logger.info(f'Записали {column1_value} {column2_value} {index}')

def get_sed_files_list(q):
    logger = logging.getLogger(__name__)
    df = pd.read_csv('nls.csv',sep=',')
    it = 0
    for index, row in df.iterrows():
        # Access the values in each column
        column1_value = row['ISN_DOC']  # Replace 'Column1' with the actual column name
        column2_value = row['FREE_NUM_SEARCH']  # Replace 'Column2' with the actual column name
        input_test_query = f"""ssh Serobaba@DockerHub 'curl -s -X GET "http://10.10.5.202:5012/api/File/getRefFile?isn={column1_value}" -H "accept: application/json"'"""
        response =str(run_bash_command(input_test_query)).replace('\\\\','')
        x=json.loads(response)
        with open(f"/media/nuanred/backup/license_eng/out/jsons/{column2_value.replace('/','')}.json", 'w', encoding='utf-8') as f:
            json.dump(x, f, ensure_ascii=False, indent=4)
        logger.debug(f'Выполняем запрос {input_test_query}')
        logger.debug(f'Ответ на запрос запрос {input_test_query} \n{response}')
        # Perform operations with the values
        logger.info(f"Row {index}: ISN_DOC = {column1_value}, Column2 = {column2_value} iter {it} of 175")
        it+=1

def set_cheks203720382039(q):
    """
    Выставляем все значения проверок в положительное решение
    """
    logger = logging.getLogger(__name__)
    input_query_2011 = f"""
    ssh Serobaba@DockerHub \\
    \"PGPASSWORD=\'VYgJBx6Eun}}W\' psql -h test-pstgr-nd.fsrar.ru -U postgres -d license_api_testcircuit -c \'update lic_checks 
    set status = 2011, 
    datechange = CURRENT_TIMESTAMP 
    where request_id = {q.setup['request_id']} 
    and code_id in (2037,2038,2039)\'"
    """

    logger.debug(f'Выполняем запрос {input_query_2011}')
    logger.debug(f'Ответ на запрос запрос {input_query_2011} \n{run_bash_command(input_query_2011)}')

def set_cheks(q):
    """
    Выставляем все значения проверок в положительное решение
    """
    logger = logging.getLogger(__name__)
    input_query_2009 = f"""
    ssh Serobaba@DockerHub \\
    \"PGPASSWORD=\'VYgJBx6Eun}}W\' psql -h test-pstgr-nd.fsrar.ru -U postgres -d license_api_testcircuit -c \'update lic_checks 
    set status = 2009, 
    datechange = CURRENT_TIMESTAMP 
    where request_id = {q.setup['request_id']} 
    and code_id in (2054,2057,2058,2059,2063)\'"
    """
    input_query_2002 = f"""
    ssh Serobaba@DockerHub \\
    \"PGPASSWORD=\'VYgJBx6Eun}}W\' psql -h test-pstgr-nd.fsrar.ru -U postgres -d license_api_testcircuit -c \'update lic_checks 
    set status = 2002, 
    datechange = CURRENT_TIMESTAMP 
    where request_id = {q.setup['request_id']} 
    and code_id in (2021,1021,2022,2034,2035,2036, 2016, 2022,2017, 2020, 2025,  2018, 2019, 2060 ,2044)\'"
    """
    # logger.debug(f'Выставляем все значения проверок в положительное решение {run_bash_command(input_query)}')
    logger.debug(f'Выполняем запрос {input_query_2009}')
    logger.debug(f'Выполняем запрос {input_query_2002}')
    logger.debug(f'Ответ на запрос запрос {input_query_2009} \n{run_bash_command(input_query_2009)}')
    logger.debug(f'Ответ на запрос запрос {input_query_2002} \n{run_bash_command(input_query_2002)}')

def get_logs_lic_integrator(uuid_logs,logs_folder):
    """
    Пишем логи lic-integrator
    """
    logger= logging.getLogger(__name__)
    current_directory = logs_folder
    logger.debug(f'Папка для логов: {current_directory}')
    EGAISLogs.get_logs(namespace='integrators',uuid_log=uuid_logs,path=current_directory,services='lic-integrator',context='test-kuber',message='test',logger= logger)
    
def get_logs_erul_license(uuid_logs,logs_folder):
    """
    Пишем логи erul_license
    """
    logger= logging.getLogger(__name__)
    current_directory = logs_folder
    logger.debug(f'Папка для логов: {current_directory}')
    EGAISLogs.get_logs(namespace='domain',uuid_log=uuid_logs,path=current_directory,services='domain-erul-license',context='test-kuber',message='test',logger= logger)

def get_logs_api_lk_license(uuid_logs,logs_folder):
    """
    Пишем логи api_lk_license
    """
    logger= logging.getLogger(__name__)
    current_directory = logs_folder
    logger.debug(f'Папка для логов: {current_directory}')
    EGAISLogs.get_logs(namespace='api-lk',uuid_log=uuid_logs,path=current_directory,services='api-lk-license',context='test-kuber',message='test',logger= logger)

def get_exam_info(q):
    """
    Информация по проваленной экспертизе документов

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Получение info {q.setup["request_id"]}')
    func_url = f"/api-lc-license/dashboard/license/request/check/exam/{q.setup['2002']}"
    # Формируем HTTP-запрос для получения информации
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения информации
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    info = json.loads(response[2])  # Преобразуем ответ в JSON объект
    logs_uuid = str(uuid.uuid4())
    # Логируем основную информацию
    json_load = json.loads(response[2])
    mess = f'''
* Шаг№{q.setup['current_method_index']} Информация по проваленной экспертизе документов
{{{{collapse(GET Получение информации по заявлению {func_url})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>
    uuid логов -> {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    q.setup["examid2002"]=info['id']
    logger.debug(f'examid2002 {info["id"]}')
    return response[2]  # Возвращаем ответ сервера

def set_exam(q):
    """Проставляет Экспертизу

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------set_exam 2002 проверки для {q.setup["request_id"]}'
    )

    func_url = f"api-lc-license/dashboard/license/request/check/exam/{q.setup['2002']}"

    # Читаем содержимое файла payloads/check_code.json
    with open('payloads/exam.json', 'r') as file:
        payload = json.load(file)
    logger.debug(
        f'------------------------Добавление payload {payload}'
    )
    # Обновляем значение checkId в payload
    payload['checkId'] = q.setup["2002"]
    payload['id'] = q.setup["examid2002"]
    # logger.debug(f'Payload POST {json.dumps(payload, separators=(',', ': '))}')

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='POST',
        url=func_url,
        body=json.dumps(payload, separators=(',', ': ')),
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': q.setup["token"]
        }
    )

    # Выполняем запрос
    response = request.execute()

    json_load = json.loads(response[2])

    logs_uuid = str(uuid.uuid4())
    q.setup['id2037'] = json_load['checkId']
    # Формируем сообщение для записи в файл
    mess = f'''
* Шаг№{q.setup['current_method_index']} Проставляем экспертизу документов 
{{{{collapse(POST set_exam 2002 {func_url})
        <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
        <pre><code class=\'json\'>\n{json.dumps(
            payload, indent=4, ensure_ascii=False)}\n
uuid логов -> {logs_uuid}
</code></pre>
}}}}'''
    

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    # get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    # Возвращаем ответ сервера
    return response[2]

def get_akt_info(q):
    """
    Выполняет запрос для получения основной информации по конкретному идентификатору запроса.

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Получение info {q.setup["request_id"]}')
    func_url = f"/dashboard/license/request/check/outside_request/outside_addresses/{q.setup['request_id']}/info"
    # Формируем HTTP-запрос для получения информации
    request = HttpRequest(
        base_url=q.setup["base_url"],  # Базовый URL
        method='GET',                  # Метод GET
        # URL для получения информации
        url=func_url,
        headers={                      # Заголовки запроса
            'accept': '*/*',           # Принимаем любой формат ответа
            'Content-Type': 'application/json',  # Тип содержимого запроса
            'authorization': q.setup["token"]  # Передаем токен авторизации
        }
    )

    response = request.execute()  # Выполняем запрос
    info = json.loads(response[2])  # Преобразуем ответ в JSON объект
    logs_uuid = str(uuid.uuid4())
    # Логируем основную информацию
    logger.debug(f'{info["requestId"]}')
    logger.debug(f'{info["inn"]}')
    logger.debug(f'{info["kpp"]}')
    logger.debug(f'{info["orgNameBrief"]}')
    logger.debug(f'{info["orgNameFull"]}')
    json_load = json.loads(response[2])
    mess = f'''
* Шаг№{q.setup['current_method_index']} Получение информации по заявлению
{{{{collapse(GET Получение информации по заявлению {q.setup["request_id"]})
    <pre>
    {q.setup["base_url"]}
    {response[0]}
    {response[1]}
    </pre>
    <pre><code class='json'>
    {json.dumps(json_load, indent=4, ensure_ascii=False)}
    </code></pre>
    uuid логов -> {logs_uuid}
}}}}
    '''
    q.write_to_file(mess, q.file_name)
    if response[0]==200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
        q.stop_flag==True
    q.write_to_file(mess, q.file_name)
    get_logs_api_lk_license(logs_uuid,logs_folder=q.logs_folder)
    get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    return response[2]  # Возвращаем ответ сервера

def add_ip(q):
    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------add IP  ')
    import requests

    headers = {
        'accept': '*/*',
        'Authorization': q.setup["token"],
        'type':'application/pdf',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'file': open('1.pdf', 'rb'),
        'inn': (None, '231294740516'),
        'licenseTypeCode': (None, '3'),
        'orgBriefName': (None, 'SDF'),
        'orgFullName': (None, 'SDF'),
        'requestTypeCode': (None, '7'),
    }

    response = requests.post('https://lk-test.egais.ru/api-lc-license/dashboard/license/request/', headers=headers, files=files,verify=False)
    
    
    logger.debug(f'{response}')


    