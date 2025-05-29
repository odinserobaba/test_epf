import os
import shutil
import subprocess
import time
import signal
import paramiko
import logging
import json


def save_custom_format_to_file(data, filename):
    """
    Saves data to a file in a custom format without quotes around keys and string values.

    Parameters:
    - data: The data (usually a dictionary) to save.
    - filename: The name of the file to save the data to.
    """
    try:
        logger = logging.getLogger(__name__)
        with open(filename, 'w', encoding='utf-8') as file:
            # Start the custom format string
            file.write("{\n")
            # Iterate over the list of dictionaries
            for i, item in enumerate(data["result"]):
                file.write("  {\n")
                # Iterate over each key-value pair in the dictionary
                for j, (key, value) in enumerate(item.items()):
                    # Write the key without quotes
                    file.write(f"    {key}: ")
                    # Write the value
                    if isinstance(value, str):
                        # Write string values without quotes
                        file.write(f"{value}")
                    else:
                        # Write other types normally
                        file.write(f"{value}")
                    # Add a comma after each item except the last one
                    if j < len(item) - 1:
                        file.write(",")
                    file.write("\n")
                file.write("  }")
                # Add a comma after each dictionary except the last one
                if i < len(data["result"]) - 1:
                    file.write(",")
                file.write("\n")
            # End the custom format string
            file.write("}")
        logger.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logger.error(f"An error occurred while saving the data: {e}")


def save_json_like_to_file(data, filename):
    """
    Saves data to a file in a JSON-like format without quotes around keys and string values.

    Parameters:
    - data: The data (usually a dictionary) to save.
    - filename: The name of the file to save the data to.
    """
    try:
        logger = logging.getLogger(__name__)
        with open(filename, 'w', encoding='utf-8') as file:
            # Start the JSON-like string
            file.write("{\n")
            # Iterate over the dictionary items
            for i, (key, value) in enumerate(data.items()):
                # Write the key without quotes
                file.write(f"  {key}: ")
                # Write the value
                if isinstance(value, str):
                    # Write string values without quotes
                    file.write(f"{value}")
                else:
                    # Write other types normally
                    file.write(f"{value}")
                # Add a comma after each item except the last one
                if i < len(data) - 1:
                    file.write(",")
                file.write("\n")
            # End the JSON-like string
            file.write("}")
        logger.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logger.error(f"An error occurred while saving the data: {e}")

def save_json_to_file(data, filename):
    """
    Saves a JSON object to a file with the specified filename.

    Parameters:
    - data: The JSON object (usually a dictionary) to save.
    - filename: The name of the file to save the JSON object to.
    """
    try:
        logger = logging.getLogger(__name__)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        logger.info(f"JSON data successfully saved to {filename}")
    except Exception as e:
        logger.error(f"An error occurred while saving the JSON data: {e}")

def run_bash_command(command):
    """
    Выполняет указанную команду Bash и возвращает ее вывод.
    
    Args:
        command (str): Команда Bash, которую нужно выполнить.
    
    Returns:
        str: Вывод выполненной команды.
    """
    logger = logging.getLogger(__name__)
    logger.debug(
        f'run_bash_command start ')
    try:
        output = subprocess.check_output(
            command, shell=True, universal_newlines=True)
        logger.info(f'{output.strip()}')
        return output.strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка при выполнении команды: {e}")
        return None

def load_json_from_file(file_path):
    """
    Загружает данные JSON из файла с обработкой исключений.

    :param file_path: Путь к файлу JSON.
    :return: Данные в формате Python (например, словарь или список) или None в случае ошибки.
    """
    logger = logging.getLogger(__name__)
    logger.debug(f'Загрузка json из файла {file_path}')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.info(data)
        return data
    except FileNotFoundError:
        logger.error(f"Ошибка: файл '{file_path}' не найден.")
    except json.JSONDecodeError:
        logger.error(f"Ошибка: файл '{file_path}' содержит некорректные данные JSON.")
    except Exception as e:
        logger.error(f"Произошла ошибка при загрузке файла '{file_path}': {e}")
    return None

def print_pretty_json(json_string):
    logger = logging.getLogger(__name__)
    try:
        # Преобразование строки в объект Python
        logger.error(f'[print_pretty_json]  Преобразуем \n {json_string}\n в json')
        data = json.loads(json_string)

        # Красивая печать JSON
        jsons = json.dumps(data, indent=4, ensure_ascii=False)
        # logger.info(jsons)
        return jsons
    except json.JSONDecodeError:
        logger.error("[print_pretty_json]  Ошибка: Некорректный формат JSON")

def run_bash_command_and_emulate_ctrl_c(command, delay=5):
    """
    Выполняет указанную команду Bash и через некоторое время отправляет ей сигнал SIGINT,
    имитируя нажатие Ctrl+C.
    
    Args:
        command (str): Команда Bash, которую нужно выполнить.
        delay (int): Задержка в секундах перед отправкой сигнала SIGINT.
    
    Returns:
        str: Вывод выполненной команды.
    """
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            universal_newlines=True
        )

        # Ждем определенное количество времени
        time.sleep(delay)

        # Отправляем сигнал SIGINT, имитирующий нажатие Ctrl+C
        process.send_signal(signal.SIGINT)

        # Ожидаем завершения процесса
        stdout, stderr = process.communicate()

        # Проверяем наличие ошибок
        if process.returncode != 0:
            raise Exception(stderr)

        return stdout.strip()
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        return None

def execute_ssh_commands(commands):
    try:
        vm = paramiko.SSHClient()
        vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vm.connect('10.0.50.208', username='Serobaba', password='nuanred')
        #
        vmtransport = vm.get_transport()
        dest_addr = ('10.10.4.32', 22)
        local_addr = ('10.0.50.208', 22)
        vmchannel = vmtransport.open_channel(
            "direct-tcpip", dest_addr, local_addr)
        #
        jhost = paramiko.SSHClient()
        jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jhost.load_host_keys('/home/osmanl/.ssh/known_hosts')  # disabled#
        jhost.connect('10.10.4.32', username='Serobaba',
                      password='nuanred', sock=vmchannel)
        res = []
        print('run ssh')
        for c in commands:
            stdin, stdout, stderr = jhost.exec_command(c+'\n')
            res.append(stdout.read().decode())
            print(stdout.read().decode())
        print(stderr.read().decode())
        jhost.close()
        vm.close()
        return res
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def execute_ssh_commands_to_file(commands, vm_details, jhost_details, log_file_path=''):
    try:
        logger = logging.getLogger(__name__)
        vm = paramiko.SSHClient()
        vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vm.connect(vm_details['hostname'], username=vm_details['username'],
                   password=vm_details['password'])

        vm_transport = vm.get_transport()
        dest_addr = (jhost_details['hostname'], 22)
        local_addr = (vm_details['hostname'], 22)
        vm_channel = vm_transport.open_channel(
            "direct-tcpip", dest_addr, local_addr)

        jhost = paramiko.SSHClient()
        jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jhost.connect(jhost_details['hostname'], username=jhost_details['username'],
                      password=jhost_details['password'], sock=vm_channel)

        for c in commands:
            stdin, stdout, stderr = jhost.exec_command(c, get_pty=True)
            logger.info(stdin, stdout, stderr)
            while True:
                line = stdout.readline()
                if not line:
                    break
                print(line)
                logger.info(line)

        jhost.close()
        vm.close()
        return True
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

def process_json_files(directory_path, output_file):
    # List to store the results
    results = []
    logger = logging.getLogger(__name__)
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)

            # Open and parse the JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Iterate over the entries in the "result" list
                for entry in data.get("result", []):
                    if 'ОСНОВНОЙ' in entry.get("description") and 'Комплект' not in entry.get("description"):
                        # Append the filename and refFile to the results list
                        results.append((filename, entry.get("refFile")))
                        logger.info(
                            f'filename {filename} refFile  {entry.get("refFile")}')

    # Write the results to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        for filename, refFile in results:
            output.write(f"{filename[:-5]}, {refFile}\n")

    logger.info(f"Results successfully saved to {output_file}")
