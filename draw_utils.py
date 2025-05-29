import logging
from HttpRequest import *  # Импортируем класс HttpRequest
import time
import json  # Для обработки JSON данных
from datetime import date
from test_utils import *
from logs import *
import uuid


class DrawUtil():
    @staticmethod
    def print_json_collapse(title, message):
        f = open("template_draw/json_draw.md", "r")
        f = f.read()
        f = f.replace('%title%', title)
        f = f.replace('%message%', message)
        return f


print(DrawUtil.print_json_collapse('test', 'test\n tesasdasdasdasdt\n'))
