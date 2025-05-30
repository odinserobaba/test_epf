import csv
import json
import logging
import os
from datetime import datetime, timezone, timedelta

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('logfile.log'),  # Запись логов в файл logfile.log
        logging.StreamHandler()             # Дополнительно выводить логи в консоль
    ]
)
logger = logging.getLogger(__name__)

def get_kafka(file_path='/home/nuanred/PycharmProjects/license_enf/in/jsons_license_epgu8.json'):
    def convert_date_from_utc_to_local(date_str):
        """
        Функция для конвертации даты из формата UTC в локальное время (в данном случае Московское).

        :param date_str: Строка с датой в формате '%Y-%m-%d %H:%M:%S.%f'.
        :return: Локальная дата в формате '%Y-%m-%dT%H:%M:%S.%f+0300'.
        """
        logger.info("Конвертирование даты из UTC в локальное время")
        # Парсим строку в объект datetime
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        # Преобразуем дату в UTC
        utc_dt = dt.replace(tzinfo=timezone.utc)

        # Конвертируем дату в местное время (например, московское +03:00)
        local_tz = timezone(timedelta(hours=3))
        local_dt = utc_dt.astimezone(local_tz)

        # Форматируем результат
        result = local_dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0300'
        return result


    # Чтение CSV-файла
    with open('in/license_out26.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Перебор всех строк и создание JSON-файлов
        for index, row in enumerate(reader, start=1):
            logger.info(f"Обработка строки {index}")
            # print(row)
            # Преобразование значений в нужные типы
            try:
                if row['xslt_id']:
                    row['xslt_id'] = int(row['xslt_id'])
                else:
                    row['xslt_id'] = None
                row['kafka_partition'] = int(row['kafka_partition'])
                row['kafka_offset'] = int(row['kafka_offset'])
                # Убедимся, что значение является числом перед приведением к булеву типу
                row['is_archived_status'] = bool((row['is_archived_status']))
                # Аналогично для is_queued_status
                row['is_queued_status'] = bool((row['is_queued_status']))
            except ValueError as e:
                logger.error(f"Ошибка преобразования типов в строке {index}: {e}")
                continue

            # Парсим requestContent и responseContent из строкового представления в JSON
            try:
                # print(row['request_content'])
                print('---------------------------------------------------------------')
                # print(row['response_content'])
                request_content = json.loads(row['request_content'])
                response_content = None #json.loads(row['response_content'])
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка парсинга JSON в строке {index}: {e}")
                continue

            # Приводим даты к нужному формату
            row['request_timestamp'] = convert_date_from_utc_to_local(
                row['request_timestamp'])
            row['update_timestamp'] = convert_date_from_utc_to_local(
                row['update_timestamp'])

            # Форматируем данные в нужный JSON
            formatted_data = {
                "id": row['id'],
                "serviceId": row['service_id'],
                "requestId": row['request_id'],
                "requestType": row['request_type'],
                "xsltId": row['xslt_id'],
                "clientInternalNumber": row['client_internal_number'],
                "additionalDetails": row['additional_details'],
                "responseId": row['response_id'],
                "messageId": row['message_id'],
                "requestContent": request_content,
                "requestTimestamp": row['request_timestamp'],
                "updateTimestamp": row['update_timestamp'],
                "responseContent": response_content,
                "kafkaPartition": row['kafka_partition'],
                "kafkaOffset": row['kafka_offset'],
                "route": row['route'],
                "state": row['state'],
                "archivedStatus": row['is_archived_status'],
                "queuedStatus": row['is_queued_status']
            }
            current_datetime = datetime.now()
            folder_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

            # Путь к новой папке внутри папки "out"
            base_folder = "out"
            folder_path = os.path.join(base_folder, folder_name)

            # Проверяем, существует ли папка, и создаём её, если она не существует
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                #print(f"Папка {folder_name} создана в папке {base_folder}.")
            #else:
            #    print(f"Папка {folder_name} уже существует в папке {base_folder}.")
            # Сохранение строки в файл с расширением '.json'
            with open(file_path, 'w', encoding='utf-8') as outfile:
                json.dump(formatted_data, outfile, ensure_ascii=False, separators=(',', ':'))
                logger.info(f"Сохранен файл 'row_{index}.json'")
            print(formatted_data)


get_kafka()