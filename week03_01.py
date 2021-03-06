"""

Первое задание на этой неделе — не сложное, для разогрева. Ваша задача: написать python-модуль solution.py, внутрь которого необходимо поместить код класса FileReader. Конструктор этого класса принимает один параметр: путь до файла на диске. В классе FileReader должен быть реализован метод read, возвращающий строку - содержимое файла, путь к которому был указан при создании экземпляра класса. Python модуль должен быть написан таким образом, чтобы импорт класса FileReader из него не вызвал ошибок.

При написании реализации метода read, вам нужно учитывать случай, когда при инициализации был передан путь к несуществующему файлу. Требуется обработать возникающее при этом исключение FileNotFoundError и вернуть из метода read пустую строку.

"""

import os

class FileReader:

    def __init__(self, filepath):
        self.filepath = filepath

    def __str__(self):
        return self.filepath

    def read(self):
        try:
            with open(self.filepath, 'r') as f:
                return f.read()

        except FileNotFoundError:
            print(f"Error: File {self.filepath} not found!")
            return ""
        