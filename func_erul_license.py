import logging
from HttpRequest import HttpRequest  # Импортируем класс HttpRequest
import time
import json  # Для обработки JSON данных
from datetime import date
from test_utils import *
from logs import *
import uuid

def cat_print_best_cat(q):
    cat = '''
    _
    \`*-.
    ) _`-.
    . : `. .
    : _ ' \
    ; *` _. `*-._
    `-.-' `-.
    ; ` `.
    :. . \
    . \ . : .-' .
    ' `+.; ; ' :
    : ' | ; ;-.
    ; ' : :`-: _.`* ;
    .*' / .*' ; .*`- +' `*'
    `*-* `*-* `*-*'
    '''

def set_status_license_2001(q):
    """
    Выставляем все значения проверок в положительное решение
    """
    logger = logging.getLogger(__name__)
    input_query_update_status_2001 = f"""
    ssh Serobaba@DockerHub \\
    \"PGPASSWORD='VYgJBx6Eun}}W' psql -h test-pstgr-nd.fsrar.ru -U postgres -d license_api_testcircuit -c 'update lic_request
    set status_code = 2001
    where id = {q.setup['request_id']}'\"
    """
    # Формируем сообщение для записи в файл
    mess = f'''
    {{{{collapse(Выставляем статус лицензии 2001 На рассмотрении)
    <pre><code class='sql'>\nupdate lic_request
    set status_code = 2001
    where id = {q.setup['request_id']}\n
    }}}}
    '''
    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)

    logger.debug(f'Выполняем запрос {input_query_update_status_2001}')
    logger.debug(
        f'Ответ на запрос запрос {input_query_update_status_2001} \n{run_bash_command(input_query_update_status_2001)}')

def set_status_license_2003(q):
    """
    Выставляем все значения проверок в Отказ
    """
    logger = logging.getLogger(__name__)
    input_query_update_status_2003 = f"""
    ssh Serobaba@DockerHub \\
    \"PGPASSWORD='VYgJBx6Eun}}W' psql -h test-pstgr-nd.fsrar.ru -U postgres -d license_api_testcircuit -c 'update lic_request
    set status_code = 2003
    where id = {q.setup['request_id']}'\"
    """
    # Формируем сообщение для записи в файл
    mess = f'''
    {{{{collapse(Выставляем статус лицензии 2003 Отказ)
    <pre><code class='sql'>\nupdate lic_request
    set lic_request.status_code = 2003
    where lic_request.id = {q.setup['request_id']}\n
    }}}}
    '''
    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    logger.debug(f'Выполняем запрос {input_query_update_status_2003}')
    logger.debug(
        f'Ответ на запрос запрос {input_query_update_status_2003} \n{run_bash_command(input_query_update_status_2003)}')

def set_status_license_2004(q):
    """
    Выставляем все значения проверок в Предоставление государственной услуги прекращено
    """
    logger = logging.getLogger(__name__)
    input_query_update_status_2004 = f"""
    ssh Serobaba@DockerHub \\
    \"PGPASSWORD='VYgJBx6Eun}}W' psql -h test-pstgr-nd.fsrar.ru -U postgres -d license_api_testcircuit -c 'update lic_request
    set status_code = 2004
    where id = {q.setup['request_id']}'\"
    """
    # Формируем сообщение для записи в файл
    mess = f'''
    {{{{collapse(Выставляем статус лицензии 2004 Предоставление государственной услуги прекращено)
    <pre><code class='sql'>\nupdate lic_request
    set lic_request.status_code = 2004
    where lic_request.id = {q.setup['request_id']}\n
    }}}}
    '''
    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    logger.debug(f'Выполняем запрос {input_query_update_status_2004}')
    logger.debug(
        f'Ответ на запрос запрос {input_query_update_status_2004} \n{run_bash_command(input_query_update_status_2004)}')

def get_kafka_erul_license(q):
    """
    Читаем топик erul_licens
    """
    logger = logging.getLogger(__name__)
    read_topic = "ssh Serobaba@DockerHub '/opt/kafka/kafka/bin/kafka-console-consumer.sh --bootstrap-server test-kafka1.fsrar.ru:9092 --topic erul-license --from-beginning --max-messages -1 --timeout-ms 1000'"
    res = run_bash_command(read_topic)
    res_mass = res.split('\n')
    res_mass_from_id = [
        str(x)+'\n' for x in res_mass if str(q.setup['request_id']) in x]
    mess = f'''
    * Шаг№{q.setup['current_method_index']} erul_license соджержит по заявлению {q.setup['request_id']}
    {{{{collapse(Читаем топик erul-license)\n
    <pre>
    {res_mass_from_id}
    </pre>
    }}}}
    '''
    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    [logger.debug(
        f'erul_license соджержит {x} па заявлению {q.setup["request_id"]}') for x in res_mass_from_id]

    logger.debug(f'Читаем топик erul_licens mass {res_mass}')

def sleep_5m(q):
    logger = logging.getLogger(__name__)
    for x in range(1, 6):
        logger.debug(f'Спим {5-x}')
        time.sleep(60)

def get_logs_erul_license(uuid_logs, logs_folder):
    """
    Пишем логи api_lk_license
    """
    logger = logging.getLogger(__name__)
    current_directory = logs_folder
    logger.debug(f'Папка для логов: {current_directory}')
    EGAISLogs.get_logs(namespace='domain', uuid_log=uuid_logs, path=current_directory,
                        services='domain-erul-license', context='test-kuber', message='test', logger=logger)

def get_ERUL_permit_number_erul_request(q):
    """Получение номера ЕРУЛ

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """
    logger = logging.getLogger(__name__)
    requestId = q.setup["request_id"]
    logger.debug(
        f'------------------------Получение номера ЕРУЛ для {q.setup["request_id"]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/{requestId}/permit_number_erul_request"

    # Формируем HTTP-запрос для получения расширенных данных
    request = HttpRequest(
        base_url=q.setup["base_url"],
        method='PATCH',
        url=func_url,
        body='',
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
    * Шаг№{q.setup['current_method_index']} Получение номера ЕРУЛ
    {{{{collapse(PATCH {func_url})
    <pre>\n{q.setup["base_url"]}\n{response[0]}\n{response[1]}\n</pre>
    <pre><code class='json'>\n{json.dumps(
        response[2], indent=4, ensure_ascii=False)}\n
    uuid логов -> {logs_uuid}
    </code></pre>
    }}}}
    '''

    # Записываем сообщение в файл
    q.write_to_file(mess, q.file_name)
    if response[0] == 200:
        mess = '%{color:green}Успешно!%'
    else:
        mess = '%{color:red}Ошибка!%'
    q.stop_flag = True
    q.write_to_file(mess, q.file_name)

    get_logs_erul_license(logs_uuid, logs_folder=q.logs_folder)

    # Возвращаем ответ сервера
    return response[2]
