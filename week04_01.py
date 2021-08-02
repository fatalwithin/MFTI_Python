"""
В этом задании вам нужно создать интерфейс для работы с файлами. Интерфейс должен предоставлять следующие возможности по работе с файлами:

- чтение из файла, метод read возвращает строку с текущим содержанием файла

- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла

- сложение объектов типа File, результатом сложения является объект класса File, при этом создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

- возвращать в качестве строкового представления объекта класса File полный путь до файла

- поддерживать протокол итерации, причем итерация проходит по строкам файла

При создании экземпляра класса File в конструктор передается полный путь до файла на файловой системе. Если файла с таким путем не существует, он должен быть создан при инициализации.
"""

import os
import tempfile

class File:

    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(filepath):
            self.f = open(filepath, 'w')
            self.f.write('')
            self.f.close()
        
        self.current = 0
        self.f = open(self.filepath, 'r')
        self.end = len(self.f.readlines())
        self.f.close()

    def __str__(self) -> str:
        return self.filepath

    def __add__(self, obj):
        """
        generates random file in temp dir with concatenated content of 1st and second files
        """
        tmpdir = tempfile.gettempdir()
        #print(f"Temp dir: {tmpdir}")
        tmpfilename = str(self.__hash__()) + str(obj.__hash__())
        #print(f"Temp file: {tmpfilename}")
        tmpfile = File(os.path.join(tmpdir,tmpfilename))

        f = open(str(tmpfile), 'w') 
        f.writelines(self.read() + obj.read())
        f.close()

        # update current iter data for the new file
        f = open(str(tmpfile), 'r')
        tmpfile.end = len(f.readlines())
        #print(f"New data: {tmpfile.read()}")
        f.close()
        
        return tmpfile

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            self.current = 0 # enabling iteration again - get cursor back to 0
            raise StopIteration

        # read again for iteration
        f = open(self.filepath, 'r')
        content = f.readlines()[self.current]
        self.current += 1
        return content


    def __hash__(self) -> int:
        return hash(self.filepath)

    def read(self):
        self.f = open(self.filepath, 'r')
        return ''.join(self.f.readlines())

    def write(self, content):
        self.f = open(self.filepath, 'w')
        self.f.write(content)
        print(len(content))
        self.f.close()

    

