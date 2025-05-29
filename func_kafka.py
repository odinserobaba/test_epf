import logging
from HttpRequest import *  # Импортируем класс HttpRequest
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


def get_kafka_in_request(q):
    """
    Читаем топик erul_licens
    """
    logger = logging.getLogger(__name__)
    topic_name = 'test-smev-leveler-in-request'
    logger.info(f'Читаем топик {topic_name}')
    read_topic = f"ssh Serobaba@DockerHub '/opt/kafka/kafka/bin/kafka-console-consumer.sh --bootstrap-server test-kafka1.fsrar.ru:9092 --topic {topic_name} --from-beginning  --max-messages -1 --timeout-ms 1000'"
    # Формируем сообщение для записи в файл
    
    res= run_bash_command(read_topic)
    logger.info(f'Пишем в файл содержимое топика {topic_name} в файл {q.file_name}')
    # Записываем сообщение в файл
    q.write_to_file(res, q.file_name)   
    