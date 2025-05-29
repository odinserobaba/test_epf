
import logging
from HttpRequest import *  # Импортируем класс HttpRequest
import time
import json  # Для обработки JSON данных
from datetime import date
from test_utils import *
from logs import *
from func import *
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

def set_aisn(q):
    """Выставляет проверку 2023 в положительное решение

    :param q: Экземпляр класса RequestQueue
    :return: Ответ сервера в формате JSON
    """

    logger = logging.getLogger(__name__)
    logger.debug(
        f'------------------------Установка АИС проверки для {q.setup["request_id"]}'
    )

    func_url = f"/api-lc-license/dashboard/license/request/{q.setup['request_id']}/register"

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
* Шаг№{q.setup['current_method_index']} Установка АИС в положительное решение
{{{{collapse(PATCH Установка АИС в положительное решение{func_url})
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
    # get_logs_lic_integrator(logs_uuid,logs_folder=q.logs_folder)
    # Возвращаем ответ сервера
    return response[2]
