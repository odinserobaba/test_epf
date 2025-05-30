from func import *
from func_erul_license import *
from models import *
from RequestQueue import *
import sel_test
from test_utils import *
from datetime import *
from sel_test import *
from func_delo import *
from func_kafka import *
from func_ais import *
from func_selenium import *


def permit_number_erul_request():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 231039
    q.add_to_queue(get_token, q)
    q.add_to_queue(get_info_to_redmine, q)
    q.add_to_queue(get_ERUL_permit_number_erul_request, q)
    q.add_to_queue(get_kafka_erul_license, q)
    q.process_queue()

def set_aisn_from_request():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    # if request_id != '':
    #     q.setup['request_id'] = request_id
    # else:
    #
    q.setup['request_id'] = 230567
    q.add_to_queue(get_token, q)
    q.add_to_queue(get_info_to_redmine, q)
    q.add_to_queue(set_aisn, q)
    q.process_queue()

def get_topic_smev_leveler_in_request():
    q = QueueLicense()
    setup_logger(q)
    q.add_to_queue(get_kafka_in_request, q)
    q.process_queue()

def get_json_number():
    q = QueueLicense()
    setup_logger(q)
    q.add_to_queue(get_sed_files, q)
    q.process_queue()

def get_sed_files_list_tests():
    q = QueueLicense()
    setup_logger(q)
    q.add_to_queue(get_sed_files_list, q)
    q.process_queue()

def copy_logs_to_downloads():
    q = QueueLicense()
    setup_logger(q)
    q.add_to_queue(copy_logs_to_folder, q)
    q.process_queue()

def test_2038():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 230528
    q.add_to_queue(get_token, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_check_order2038, q)
    q.add_to_queue(set_order, q)
    q.process_queue()

def add_akt():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 230528
    q.add_to_queue(get_token, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_exercise2037, q)
    q.add_to_queue(set_akt, q)
    q.add_to_queue(info_q, q)
    q.process_queue()

def add_ul_license():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['inn'] = '7841051711'
    q.setup['licenseTypeCode'] = '3'
    q.setup['orgBriefName'] = 'АО «ЦентрИнформ» '
    q.setup['orgFullName'] = 'АО «ЦентрИнформ» '
    q.setup['requestTypeCode'] = '7'
    q.add_to_queue(get_token, q)
    q.add_to_queue(add_ip, q)
    q.process_queue()

def add_ip_license():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['inn'] = '231294740516'
    q.setup['licenseTypeCode'] = '3'
    q.setup['orgBriefName'] = 'ИП Тест'
    q.setup['orgFullName'] = 'ИП Тест'
    q.setup['requestTypeCode'] = '7'
    q.add_to_queue(get_token, q)
    q.add_to_queue(add_ip, q)
    q.process_queue()

def test_checks():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227739
    q.add_to_queue(get_token, q)
    q.add_to_queue(set_cheks, q)
    q.process_queue()

def test_erul_license():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 231801
    q.add_to_queue(get_token, q)
    q.add_to_queue(get_kafka_erul_license, q)
    q.process_queue()

def test_kafka():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227934
    q.add_to_queue(get_token, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_kafka_erul_license, q)
    q.process_queue()
# Все проверки кроме 2002
def test_todo_2002positive():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 232004
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    # Выставляем все проверки в положительное решение
    q.add_to_queue(set_cheks, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(set_check2023, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(set_check2002, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    # Задание
    q.add_to_queue(set_check2037, q)
    q.add_to_queue(get_extended, q)
    q.process_queue()
# Все проверки кроме 2002
def test_todo_2002_negative():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 230977
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(set_info, q)

    q.add_to_queue(set_cheks, q)
    # q.add_to_queue(set_cheks,q)
    q.add_to_queue(set_check2023, q)
    q.add_to_queue(set_check2002_negative, q)
    # q.add_to_queue(get_extended,q)
    # q.add_to_queue(get_info,q)
    q.add_to_queue(get_exam_info, q)
    q.add_to_queue(set_exam, q)
    # q.add_to_queue(get_kafka_erul_license,q)
    q.process_queue()

def test_set_status():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227313
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(set_status_license_2001, q)
    q.process_queue()

def test_info():

    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227365
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.process_queue()

def test_get_outside_request():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 231998
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_outside_request, q)
    q.process_queue()

def test_set_outside_request():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 232060
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_outside_request, q)
    q.add_to_queue(get_outside_order, q)
    q.add_to_queue(set_outside_request, q)
    q.process_queue()

def test_set_outside_exec():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 232060
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_outside_request, q)
    q.add_to_queue(set_outside_exec, q)
    q.process_queue()

def test_set_outside_order():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 232060
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_outside_request, q)
    q.add_to_queue(get_outside_order, q)
    q.add_to_queue(set_outside_order, q)
    q.process_queue()

def test_get_outside_order():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 231998
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(get_outside_order, q)
    q.process_queue()

def test_positive():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 233782
    # logger = logging.getLogger(__name__)
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    # Выставляем все проверки в положительное решение
    q.add_to_queue(set_cheks, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(set_check2023, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(set_check2002, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    # q.add_to_queue(set_check2037,q)
    # q.add_to_queue(get_extended, q)
    # q.add_to_queue(get_info, q)
    # q.add_to_queue(get_exercise_request_doc2037, q)
    # q.add_to_queue(get_exercise2037, q)

    # q.add_to_queue(get_exercise_request_addresses2037, q)
    # q.add_to_queue(get_exercise_applicant_info2037, q)
    # q.add_to_queue(get_extended, q)
    # q.add_to_queue(get_info, q)
    # q.add_to_queue(get_exercise_request_doc2037, q)
    # q.add_to_queue(get_exercise2037, q)
    # q.add_to_queue(get_exercise_request_addresses2037, q)
    # q.add_to_queue(get_exercise_applicant_info2037, q)
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    # q.add_to_queue(get_exercise_request_doc2037, q)
    # q.add_to_queue(get_exercise2037, q)
    # q.add_to_queue(get_exercise_request_addresses2037, q)
    # q.add_to_queue(get_exercise_applicant_info2037, q)
    # q.add_to_queue(get_extended, q)
    # q.add_to_queue(get_info, q)

    q.add_to_queue(get_outside_request, q)
    q.add_to_queue(get_outside_request_checks, q)
    # q.add_to_queue(get_outside_request, q)
    q.add_to_queue(set_outside_request, q)
    q.add_to_queue(set_outside_request, q)
    q.add_to_queue(get_outside_order, q)
    q.add_to_queue(set_outside_order, q)
    q.add_to_queue(set_outside_exec, q)
    q.process_queue()

def set_2038():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 228303
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    # q.add_to_queue(get_check_order2038,q)
    q.add_to_queue(get_order2038, q)
    q.add_to_queue(set_order, q)
    q.add_to_queue(set_akt, q)
    q.process_queue()

def set_akt_test():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227258

    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)
    q.add_to_queue(set_akt, q)
    q.process_queue()

def test_db():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227258
    q.add_to_queue(set_cheks, q)
    q.process_queue()

def copy_logs():
    current_date = datetime.now()
    run_bash_command(
        f'''"scp -r Serobaba@DockerHub:/home/ldapusers/Serobaba/logs/{
            current_date.strftime("%d-%m-%Y")}/ /home/nuanred/Downloads/logs/"''')

def get_akts_info():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 227270
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_extended, q)
    q.add_to_queue(get_info, q)

def create_license_test():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH1.'
    q.add_to_queue(create_license_from_req, q)
    q.process_queue()

def extension_license_test():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH3.'
    q.add_to_queue(create_license_from_req, q)
    q.process_queue()

def re_registration_license_test():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH5.'
    q.add_to_queue(create_license_from_req, q)
    q.process_queue()

def termination_license_test():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH7.'
    q.add_to_queue(create_license_from_req, q)
    q.process_queue()

def create_license_test_ip():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH1.'
    q.add_to_queue(create_license_from_req_ip, q)
    q.process_queue()

def extension_license_test_ip():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH3.'
    q.add_to_queue(create_license_from_req_ip, q)
    q.process_queue()

def re_registration_license_test_ip():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH5.'
    q.add_to_queue(create_license_from_req_ip, q)
    q.process_queue()

def termination_license_test_ip():
    q = QueueLicense()
    setup_logger(q)
    q.setup['lic'] = '0.LLGJ.LLGZ.LLH7.'
    q.add_to_queue(create_license_from_req_ip, q)
    q.process_queue()

def get_info_redmine():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 231582
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    # q.add_to_queue(get_akt_info,q)
    q.add_to_queue(get_info_to_redmine, q)
    q.process_queue()

def set_checks_2011():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['request_id'] = 230986
    q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(set_cheks203720382039, q)
    q.process_queue()

def go_to_lk():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    q.setup['token'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiTVJVRlNSQVIiLCJyb2xlRGVzY3IiOiLQodC-0YLRgNGD0LTQvdC40Log0JzQoNCjINCg0L7RgdCw0LvQutC-0LPQvtC70YzRgtCw0LHQsNC60LrQvtC90YLRgNC-0LvRjCIsImZpcnN0TmFtZSI6ItCV0LLQs9C10L3QuNC5INCh0LXRgNCz0LXQtdCy0LjRhyIsImxhc3ROYW1lIjoi0KHQtdGA0L7QsdCw0LHQsCIsImxvY2FsaXR5Ijoi0JPQntCg0J7QlCDQnNCe0KHQmtCS0JAiLCJyZWdpb24iOiI3NyDQk9Ce0KDQntCUINCc0J7QodCa0JLQkCIsInJlZ2lvbkNvZGUiOiI3NyIsInVzZXJpZCI6IjQ5MyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkzIiwicm9sZWlkIjoiMzgiLCJwZXJtaXNzaW9ucyI6Ik5ld3MsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsIiwibGlzdFJlZ2lvbkNvZGVzIjoiMzEsMzIsMzMsMzYsMzcsNDAsNDQsNDYsNDgsNzcsNTAsNTcsNjIsNjcsNjgsNjksNzEsNzYsOTkiLCJleHAiOjE3NDMxNTM1NDAsImlzcyI6IkNBRWdhaXMiLCJhdWQiOiJVc2VycyJ9.uFzHqflb69ZR-F88FYpW0cAboAic3ssZzc904NTzTrc'
    # q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_start_lk, q)
    q.process_queue()

def go_to_federal():
    q = QueueLicense()
    setup_logger(q)
    q.setup['base_url'] = "lk-test.egais.ru"
    # q.setup['token'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiTVJVRlNSQVIiLCJyb2xlRGVzY3IiOiLQodC-0YLRgNGD0LTQvdC40Log0JzQoNCjINCg0L7RgdCw0LvQutC-0LPQvtC70YzRgtCw0LHQsNC60LrQvtC90YLRgNC-0LvRjCIsImZpcnN0TmFtZSI6ItCV0LLQs9C10L3QuNC5INCh0LXRgNCz0LXQtdCy0LjRhyIsImxhc3ROYW1lIjoi0KHQtdGA0L7QsdCw0LHQsCIsImxvY2FsaXR5Ijoi0JPQntCg0J7QlCDQnNCe0KHQmtCS0JAiLCJyZWdpb24iOiI3NyDQk9Ce0KDQntCUINCc0J7QodCa0JLQkCIsInJlZ2lvbkNvZGUiOiI3NyIsInVzZXJpZCI6IjQ5MyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkzIiwicm9sZWlkIjoiMzgiLCJwZXJtaXNzaW9ucyI6Ik5ld3MsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsIiwibGlzdFJlZ2lvbkNvZGVzIjoiMzEsMzIsMzMsMzYsMzcsNDAsNDQsNDYsNDgsNzcsNTAsNTcsNjIsNjcsNjgsNjksNzEsNzYsOTkiLCJleHAiOjE3NDMxNTM1NDAsImlzcyI6IkNBRWdhaXMiLCJhdWQiOiJVc2VycyJ9.uFzHqflb69ZR-F88FYpW0cAboAic3ssZzc904NTzTrc'
    # q.add_to_queue(get_token, q)  # Добавляем функцию в очередь
    q.add_to_queue(get_start_lk, q)
    # q.add_to_queue(get_federal, q)
    q.process_queue()
