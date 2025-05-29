import logging
import os
from datetime import datetime
import uuid

# Assuming `cat_print` and other necessary functions are imported from `func`
from func import cat_print

class QueueLicense:
    def __init__(self, name_tests=''):
        """
        Initialize the QueueLicense with a test name and setup default configurations.
        """
        self.stop_flag = False
        self.sleep_time = 0
        self.folder_path = ''
        self.name_tests = name_tests if name_tests else f'unnamed_{uuid.uuid4()}'
        self.logger = logging.getLogger(__name__)
        self.setup = {
            'base_url': "",
            'token': "",
            'request_id': "",
            'current_method_index': 0
        }
        self.queue = []
        self.file_name = 'test.md'
        self.checks = []

        # Initialize folder and file
        self.create_folder_and_file()
        self.write_to_file("", self.file_name)
        self.logger.debug(f'{cat_print("")}')

    def create_folder_and_file(self):
        """
        Create necessary folders and files based on the current date and test name.
        """
        now = datetime.now()
        folder_name = now.strftime("%Y-%m-%d")
        file_name = now.strftime("%Y-%m-%d_%H-%M-%S.md")

        # Path to the date folder
        folder_path = os.path.join("out", folder_name)
        self.logger.info(f'Folder with date: {folder_path}')

        # Create date folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Full path to the file
        file_path = os.path.join(folder_path, file_name)

        # Create test folder if it doesn't exist
        test_folder_path = os.path.join(file_path, self.name_tests)
        if not os.path.exists(test_folder_path):
            os.makedirs(test_folder_path)

        # Folder for logs
        self.logs_folder = test_folder_path

        # Full path to the result file
        result_file_path = os.path.join(test_folder_path, 'res.md')

        # Create result file if it doesn't exist
        with open(result_file_path, 'w'):
            pass

        self.folder_path = result_file_path
        self.file_name = self.folder_path
        return result_file_path

    def write_to_file(self, message, file_path=None):
        """
        Write a message to the specified file. If no file path is provided, use the default file.
        """
        if file_path is None:
            file_path = self.create_folder_and_file()

        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
        except Exception as e:
            self.logger.error(f'Error writing to file: {e}')

    def add_to_queue(self, func, arg=None):
        """
        Add a function and its argument to the queue.
        """
        self.queue.append((func, arg))
        self.logger.debug(f'Request added to queue: {self.queue[-1]}')

    def process_queue(self):
        """
        Process all elements in the queue sequentially.
        """
        while self.queue:
            if self.stop_flag:
                break

            current_method_index = self.setup['current_method_index']
            if current_method_index >= len(self.queue):
                self.logger.warning(f'Cannot continue processing queue, end reached. current_method_index {current_method_index} len(self.queue) {len(self.queue)}')
                break

            try:
                self.logger.debug(f'Executing request: {self.queue[current_method_index]}')
                func, arg = self.queue[current_method_index]
                result = func(arg)  # Call the function with the argument
                if result:
                    print(result)
                self.logger.debug(f'Request completed: {self.queue[current_method_index]}')
                self.setup['current_method_index'] += 1  # Move to the next method
            except Exception as e:
                self.logger.error(f'Error executing request: {self.setup} {e}')
                break
