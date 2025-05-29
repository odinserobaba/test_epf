import logging
from queue import Queue


class RequestQueue:
    def __init__(self):
        self.queue = Queue()
        self.logger = logging.getLogger(__name__)
        self.data = []
        self.checks={}
        self.cursor = 0

    def add_request(self, request):
        """Добавить новый запрос в очередь."""
        self.queue.put(request)
        self.logger.debug(f'Запрос добавлен в очередь: {request.method} {request.url}')

    def remove_request(self):
        """Удалить первый запрос из очереди."""
        if not self.queue.empty():
            self.queue.get()
            self.logger.debug('Первый запрос удалён из очереди.')

    def process_queue(self):
        """Обработать все запросы в очереди."""
        while not self.queue.empty():
            request = self.queue.get()
            status_code, reason, data = request.execute()
            self.logger.info(f'Запрос обработан. Код ответа: {status_code}, Причина: {reason}. Данные: {data}')
            self.data.append(data)
