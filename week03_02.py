"""
Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице. Классы должны называться CarBase (базовый класс для всех типов машин), Car (легковые автомобили), Truck (грузовые автомобили) и SpecMachine (спецтехника). Все объекты имеют обязательные атрибуты:

- car_type, значение типа объекта и может принимать одно из значений: «car», «truck», «spec_machine».

- photo_file_name, имя файла с изображением машины, допустимы названия файлов изображений с расширением из списка: «.jpg», «.jpeg», «.png», «.gif»

- brand, марка производителя машины

- carrying, грузоподъемность

В базовом классе CarBase нужно реализовать метод get_photo_file_ext для получения расширения файла изображения. Расширение файла можно получить при помощи os.path.splitext.

Для грузового автомобиля необходимо в конструкторе класса определить атрибуты: body_length, body_width, body_height, отвечающие соответственно за габариты кузова — длину, ширину и высоту. Габариты передаются в параметре body_whl (строка, в которой размеры разделены латинской буквой «x»). Обратите внимание на то, что характеристики кузова должны быть вещественными числами и характеристики кузова могут быть не валидными (например, пустая строка). В таком случае всем атрибутам, отвечающим за габариты кузова, присваивается значение равное нулю.

Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова.

В классе Car должен быть определен атрибут passenger_seats_count (количество пассажирских мест), а в классе SpecMachine — extra (дополнительное описание машины).

"""
import os
import csv

class CarBase:

    """
    Let's make 3 required parameters as properties
    """

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value != "":
            self.__brand = value
        else:
            raise ValueError("Wrong brand!")
    
    @property
    def photo_file_name(self):
        return self.__photo_file_name

    @photo_file_name.setter
    def photo_file_name(self, value):
        if (os.path.splitext(value)[1] in ['.jpg', '.jpeg', '.png', '.gif'] and os.path.splitext(value)[0] != ''):
            self.__photo_file_name = value
        else:
            raise ValueError("Wrong photo file name!")

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, value):
        try:
            self.__carrying = float(value)
        except Exception:
            raise ValueError(f"Invalid carrying value: {value}")
            
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        """ 
        Get extension of file with car photo.
        Only jpg, jpeg, png and gif are allowed
        """

        ext = os.path.splitext(self.photo_file_name)
        return ext[1]


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        
        try:
            self.passenger_seats_count = int(passenger_seats_count)

        except Exception:
            raise ValueError(f"Invalid value: {passenger_seats_count}")


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"

        try:
            self.body_length, self.body_width, self.body_height = (float(par) for par in (body_whl.replace('X', 'x').split('x')))

        except Exception:
            self.body_width = float(0)
            self.body_length = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length
    

class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        
        if (extra != ""):
            self.extra = extra

        else:
            raise ValueError(f"Invalid value: {extra}")


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == "car":
                    car_list.append(Car(brand=row[1], photo_file_name=row[3], carrying=row[5], passenger_seats_count=row[2]))
                elif row[0] == "truck":
                    car_list.append(Truck(brand=row[1], photo_file_name=row[3], carrying=row[5], body_whl=row[4]))
                elif row[0] == "spec_machine":
                    car_list.append(SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6]))
                else:
                    continue

            except Exception as err:
                print(f"Invalid row: {row}")
                print(err.__str__())

    return car_list
