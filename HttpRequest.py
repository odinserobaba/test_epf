import ssl
import http.client
import logging

class HttpRequest:
    def __init__(self, method, base_url, url, body=None, headers=None):
        self.method = method.upper()  # Метод GET/POST/PUT/DELETE и др.
        self.base_url = base_url
        self.url = url
        self.body = body or {}
        self.headers = headers or {}
        self.logger = logging.getLogger(__name__)
        self.data =""
        self.reason=""
        self.status_code=""

    def execute(self):
        try:
            # Отключение проверки SSL-сертификатов
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            # Устанавливаем соединение с указанным доменом
            conn = http.client.HTTPSConnection(self.base_url, context=ctx)
            full_url = f"{self.url}"
            conn.request(self.method, full_url, self.body, self.headers)
            response = conn.getresponse()
            status_code = response.status
            reason = response.reason
            data = response.read().decode('utf-8')
            self.logger.info(f'Запрос выполнен. Код ответа: "{status_code}", Причина: "{reason}". Данные: "{data}"')
            self.data=data
            self.status_code=status_code
            self.reason=reason
            return status_code, reason, data
        except Exception as e:
            self.logger.error(f'Ошибка при выполнении запроса: {self.base_url} {self.body} {self.data} {self.headers} {self.method} "{e}" ')
            self.logger.error(f'Ошибка при выполнении запроса: {self.data} {self.status_code} {self.reason}')
            return None, None, str(e)