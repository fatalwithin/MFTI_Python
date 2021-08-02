"""
Часто при зачислении каких-то средств на счет с нас берут комиссию. Давайте реализуем похожий механизм с помощью дескрипторов. Напишите дескриптор Value, который будет использоваться в нашем классе Account.
У аккаунта будет атрибут commission. Именно эту коммиссию и нужно вычитать при присваивании значений в amount.
Опишите дескриптор в файле и загрузите его на платформу.
"""


class Value:
    def __init__(self):
        self.value = None
        self.commission = None
        
    @staticmethod
    def _prepare_value(value, commission):
        return value*(1 - commission) if 0 <= commission <= 1 else value
    
    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.commission = obj.commission
        self.value = self._prepare_value(value, self.commission)
