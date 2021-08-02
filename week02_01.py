import os
import tempfile
import argparse
import json

"""
На этой неделе мы с вами реализуем собственное key-values хранилище. 
Данные будут сохраняться в файле storage.data. 
Добавление новых данных в хранилище и получение текущих значений 
осуществляется с помощью утилиты командной строки storage.py. 
Пример работы утилиты:  

Сохранение значения value по ключу key_name:  
$ storage.py --key key_name --val value

Получение значения по ключу key_name:  
$ storage.py --key key_name
"""

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Key for storing of getting values")
    parser.add_argument("--value", help="Value related to the given key")
    return parser.parse_args()


def read_data(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except:
        data = {}
    return data

data = read_data(storage_path)
args = parse()

if (args.key and args.value):
    with open(storage_path, 'w') as f:
        value = data.get(args.key)

        if not value: 
            data[args.key] = []
        
        #if args.value not in data[args.key]:
        data[args.key].append(args.value)

        json_string = json.dumps(data)
        f.write(json_string)
    f.close()

elif (args.key and not args.value):
    value = data.get(args.key)
    result = data[args.key] if value else ['None']
    print(', '.join(map(str,result)))

else:
    print("Error: Invalid params")