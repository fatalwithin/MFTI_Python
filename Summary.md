## Базовые типы

### Целые числа (int)

In [12]:

```python
num = 13
print(num)

num = 0
print(num)

num = -10
print(num)
13
0
-10
```

In [9]:

```python
num = 100_000_000
print(num)
100000000
```

Встроенная функция **type**

In [6]:

```python
num = 13
print(type(num))
<class 'int'>
```

### Вещественные числа (float)

In [8]:

```python
num = 13.4
print(num)

num = 0.0
print(num)

num = -10.2
print(num)
13.4
0.0
-10.2
```

In [9]:

```python
num = 100_000.000_001
print(num)
100000.000001
```

In [5]:

```python
# 1.5 умножить на 10 в степени 2
num = 1.5e2
print(num)
150.0
```

Конвертация типов:

In [1]:

```python
num = 150.2
print(type(num))
<class 'float'>
```

In [2]:

```python
num = int(num)
print(num, type(num))

num = float(num)
print(num, type(num))
150 <class 'int'>
150.0 <class 'float'>
```

### Комплексные числа (complex)

In [4]:

```python
num = 14 + 1j

print(type(num))
print(num.real)
print(num.imag)
<class 'complex'>
14.0
1.0
```

Модуль **decimal** для работы с вещественными числами с фиксированной точностью

Модуль **fractions** для работы с рациональными числами

### Основные операции с числами

Сложение:

In [7]:

```python
1 + 1
```

Out[7]:

```python
2
```

In [8]:

```python
1 + 2.0
```

Out[8]:

```python
3.0
```

Вычитание:

In [19]:

```python
10 - 1
```

Out[19]:

```python
9
```

In [20]:

```python
4.2 - 1
```

Out[20]:

```python
3.2
```

Деление:

In [10]:

```python
10 / 2
```

Out[10]:

```python
5.0
```

Делить на 0 нельзя:

In [11]:

```python
2 / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-11-ae0c5d243292> in <module>()
----> 1 2 / 0

ZeroDivisionError: division by zero
```

Умножение:

In [12]:

```python
4 * 5.25
```

Out[12]:

```python
21.0
```

Возведение числа в степень:

In [21]:

```python
2 ** 4
```

Out[21]:

```python
16
```

Целочисленное деление:

In [14]:

```python
10 // 3
```

Out[14]:

```python
3
```

Остаток от деления:

In [15]:

```python
10 % 3
```

Out[15]:

```python
1
```

Порядок операций в выражениях с числами:

In [7]:

```python
print(10 * 3 + 3)
print(10 * (3 + 3))
33
60
```

Побитовые операции:

In [18]:

```python
x = 4
y = 3

print("Побитовое или:", x | y)
print("Побитовое исключающее или:", x ^ y)
print("Побитовое и:", x & y)
print("Битовый сдвиг влево:", x << 3)
print("Битовый сдвиг вправо:", x >> 1)
print("Инверсия битов:", ~x)
Побитовое или: 7
Побитовое исключающее или: 7
Побитовое и: 0
Битовый сдвиг влево: 32
Битовый сдвиг вправо: 2
Инверсия битов: -5
```

Задача: найти расстояние между двумя точками в декартовых координатах.

Решение:

In [8]:

```python
x1, y1 = 0, 0
x2 = 3
y2 = 4

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)
5.0
```

Меняем местами значения 2-х переменных:

In [22]:

```python
a = 100
b = 200
print(a, b)

a, b = b, a
print(a, b)
100 200
200 100
```

Вместо `x, y = 0, 0`

In [25]:

```python
x = y = 0
x += 1

print(x)
print(y)
1
0
```

Но нужно помнить об отличии изменяемых (mutable) и неизменяемых (immutable) типов:

In [26]:

```python
x = y = []
x.append(1)
x.append(2)

print(x)
print(y)
[1, 2]
[1, 2]
```

В этом видео:

- Поговорили о базовых численных типах в Python
- Рассмотрели математические операции с численными типами
- Узнали о конвертации типов
- Затронули тему изменяемых и неизменяемых объектов в Python

In [ ]:



### Логические типы (bool)

In [16]:

```python
True
```

Out[16]:

```python
True
```

In [32]:

```python
False
```

Out[32]:

```python
False
```

In [21]:

```python
result = True
print(type(result))
<class 'bool'>
```

Оператор "равно":

In [14]:

```python
13 == 13
```

Out[14]:

```python
True
```

Оператор "не равно":

In [20]:

```python
1 != 2
```

Out[20]:

```python
True
```

Операторы сравнения:

In [10]:

```python
print(3 > 4)
print(3 <= 3)
print(6 >= 6)
print(6 < 5)
False
True
True
False
```

In [29]:

```python
x = 2
print(1 < x < 3)
True
```

Конвертация типов:

In [35]:

```python
bool(12)
```

Out[35]:

```python
True
```

In [36]:

```python
bool(0)
```

Out[36]:

```python
False
```

### Логические выражения

Логическое "и":

In [16]:

```python
x, y = True, False
print(x and y)
False
```

Логическое "или":

In [17]:

```python
x, y = True, False
print(x or y)
True
```

Логическое отрицание:

In [18]:

```python
y = False
print(not y)
True
```

Составные логические выражения:

In [20]:

```python
x, y, z = True, False, True
result = x and y or z
print(result)
True
```

In [9]:

```python
x = 12
y = False

print(x or y)
12
```

In [10]:

```python
x = 12
z = "boom"

print(x and z)
boom
```

Задача: определить високосный год или нет?

Год является високосным если он кратен 4, но при этом не кратен 100, либо кратен 400.

In [16]:

```python
year = 2017
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)
False
```

In [10]:

```python
import calendar

print(calendar.isleap(1980))
True
```

В этом видео:

- Поговорили о типе `bool` в Python
- Рассмотрели логические операторы
- Посмотрели на составные логические выражения



### Строки (str)

Строка – это неизменяемая последовательность юникодных символов

In [23]:

```python
example_string = "Курс про Python на Coursera"
print(example_string)
Курс про Python на Coursera
```

In [22]:

```python
print(type(example_string))
<class 'str'>
```

In [20]:

```python
example_string = 'Курс про "Python" на "Coursera"'
print(example_string)
Курс про "Python" на "Coursera"
```

In [21]:

```python
example_string = "Курс про \"Python\" на \"Coursera\""
print(example_string)
Курс про "Python" на "Coursera"
```

"Cырые" (r-строки):

In [27]:

```python
example_string = "Файл на диске c:\\\\"
print(example_string)

example_string = r"Файл на диске c:\\"
print(example_string)
Файл на диске c:\\
Файл на диске c:\\
```

Как разбить объявление длинной строки:

In [4]:

```python
example_string = "Perl — это тот язык, который одинаково " \
                 "выглядит как до, так и после RSA шифрования." \
                 "(Keith Bostic)"
print(example_string)
Perl — это тот язык, который одинаково выглядит как до, так и после RSA шифрования.(Keith Bostic)
```

In [23]:

```python
example_string = """
Есть всего два типа языков программирования: те, на которые 
люди всё время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""
print(example_string)
Есть всего два типа языков программирования: 
те, на которые люди всё время ругаются, и те, 
которые никто не использует.

Bjarne Stroustrup
```

Как объединить 2 строки в одну?

In [14]:

```python
"Можно" + " просто " + "складывать" + " строки"
```

Out[14]:

```python
'Можно просто складывать строки'
```

In [15]:

```python
"Даже умножать!" * 3
```

Out[15]:

```python
'Даже умножать!Даже умножать!Даже умножать!'
```

**Строки неизменяемые!**

In [15]:

```python
example_string = "Привет"
print(id(example_string))

example_string += ", Мир!"
print(id(example_string))
4379064296
4379064192
```

#### Срезы строк [start:stop:step]

In [61]:

```python
example_string = "Курс про Python на Coursera"
example_string[9:]
```

Out[61]:

```python
'Python на Coursera'
```

In [25]:

```python
example_string = "Курс про Python на Coursera"
example_string[9:15]
```

Out[25]:

```python
'Python'
```

In [26]:

```python
example_string = "Курс про Python на Coursera"
example_string[-8:]
```

Out[26]:

```python
'Coursera'
```

Использование step:

In [12]:

```python
example_string = "0123456789"
example_string[::2]
```

Out[12]:

```python
'02468'
```

In [13]:

```python
example_string = "Москва"
example_string[::-1]
```

Out[13]:

```python
'авксоМ'
```

У строк есть методы:

In [28]:

```python
quote = """Болтовня ничего не стоит. Покажите мне код.

Linus Torvalds
"""
quote.count("о")
```

Out[28]:

```python
6
```

In [25]:

```python
"москва".capitalize()
```

Out[25]:

```python
'Москва'
```

In [29]:

```python
"2017".isdigit()
```

Out[29]:

```python
True
```

Оператор **in** позволяет проверить наличие подстроки в строке:

In [30]:

```python
"3.14" in "Число Пи = 3.1415926"
```

Out[30]:

```python
True
```

In [18]:

```python
"Алексей" in "Александр Пушкин"
```

Out[18]:

```python
False
```

Выражение **for .. in** позволяет итерироваться по строке:

In [23]:

```python
example_string = "Привет"
for letter in example_string:
    print("Буква", letter)
Буква П
Буква р
Буква и
Буква в
Буква е
Буква т
```

Конвертация типов:

In [18]:

```python
num = 999.01

num_string = str(num)

print(type(num_string))
num_string
<class 'str'>
```

Out[18]:

```python
'999.01'
```

In [19]:

```python
bool("Непустая строка")
```

Out[19]:

```python
True
```

In [20]:

```python
bool("")
```

Out[20]:

```python
False
```

In [22]:

```python
name = ""

if not name:
    print("Имя не заполнено!")
Имя не заполнено!
```

#### Форматирование строк

1-ый способ форматирования:

In [55]:

```python
template = "%s — главное достоинство программиста. (%s)"
template % ("Лень", "Larry Wall")
```

Out[55]:

```python
'Лень — главное достоинство программиста. (Larry Wall)'
```

https://docs.python.org/3/library/string.html#format-specification-mini-language

2-ой способ:

In [56]:

```python
"{} не лгут, но {} пользуются формулами. ({})".format(
    "Цифры", "лжецы", "Robert A. Heinlein"
)
```

Out[56]:

```python
'Цифры не лгут, но лжецы пользуются формулами. (Robert A. Heinlein)'
```

Еще способ:

In [57]:

```python
"{num} Кб должно хватить для любых задач. ({author})".format(
    num=640, author="Bill Gates"
)
```

Out[57]:

```python
'640 Кб должно хватить для любых задач. (Bill Gates)'
```

И еще f-строки, Python >= 3.6:

In [58]:

```python
subject = "оптимизация"
author = "Donald Knuth"

f"Преждевременная {subject} — корень всех зол. ({author})"
```

Out[58]:

```python
'Преждевременная оптимизация — корень всех зол. (Donald Knuth)'
```

Модификаторы форматирования:

In [59]:

```python
num = 8
f"Binary: {num:#b}"
```

Out[59]:

```python
'Binary: 0b1000'
```

In [4]:

```python
num = 2 / 3
print(num)

print(f"{num:.3f}")
0.6666666666666666
0.667
```

Больше описания и примеров в документации:

https://docs.python.org/3/library/string.html

#### Встроенная функция input()

Позволяет получить ввод пользователя в виде строки

In [60]:

```python
name = input("Введи свое имя: ")

f"Привет, {name}!"
Введи свое имя: Александр
```

Out[60]:

```python
'Привет, Александр!'
```

### Байтовые строки (bytes)

Байт - минимальная единица хранения и обработки цифровой информации. Последовательность байт представляет собой какую-либо информацию (текст, картинку, мелодию...)

Байтовая строка – это неизменяемая последовательность чисел от 0 до 255.

b-литерал для объявления байтовой строки:

In [17]:

```python
example_bytes = b"hello"
print(type(example_bytes))
<class 'bytes'>
```

In [47]:

```python
for element in example_bytes:
    print(element)
104
101
108
108
111
```

In [48]:

```python
example_bytes = b"привет"
  File "<ipython-input-48-f10cf569d599>", line 1
    example_bytes = b"привет"
                   ^
SyntaxError: bytes can only contain ASCII literal characters.
```

Bytes literals are always prefixed with 'b' or 'B'; they produce an instance of the bytes type instead of the str type. They may only contain ASCII characters; bytes with a numeric value of 128 or greater must be expressed with escapes.

In [41]:

```python
example_string = "привет"
print(type(example_string))
print(example_string)
<class 'str'>
привет
```

In [42]:

```python
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))
b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
<class 'bytes'>
```

| Буква | Кодировка | hex   | dec (bytes) | dec   | binary            |
| :---- | :-------- | :---- | :---------- | :---- | :---------------- |
| п     | UTF-8     | D0 BF | 208 191     | 53439 | 11010000 10111111 |

буква п - https://unicode-table.com/ru/043F/

Декодируем байты обратно в строку:

In [45]:

```python
decoded_string = encoded_string.decode()
print(decoded_string)
привет
```

В этом видео:

- Поговорили о строковых типах в Python
- Рассмотрели способы форматирования строк
- Узнали как получить ввод пользователя в виде строки
- Посмотрели как работать с последовательностями - срезы, итерация



### None

In [1]:

```python
answer = None
```

По сути None это значение специального типа NoneType, используемое на практике для обозначения отсутствия значения. Если вы знаете C можете рассматривать его как нулевой указатель.

In [25]:

```python
print(type(None))
<class 'NoneType'>
```

In [26]:

```python
bool(None)
```

Out[26]:

```python
False
```

In [2]:

```python
answer = None

if not answer:
    print("Ответ не получен")
Ответ не получен
```

In [28]:

```python
income = 0

if not income:
    print("Ничего не заработали")
Ничего не заработали
```

In [30]:

```python
income = None

if income is None:
    print("Еще не начинали продавать")
elif not income:
    print("Ничего не заработали")
Еще не начинали продавать
```

Вы часто увидите None в именованных аргументах функций или методах классов как значение по умолчанию - это обычно применяется тогда, когда аргумент является не обязательным - то есть функция или метод могут работать и тогда когда аргумент явным образом не передали при вызове. Также часто этим значением инициализируют атрибуты экземпляров классов, чтобы потом в нужный момент переопределить каким-то значением. Про функции и классы мы вам расскажем на слежующих неделях курса.



## Конструкции управления потоком

### if - проверка условия

Оператор **if** используется для выполнения каких-либо действий при выполнении условия:

In [1]:

```python
company = "my.com"

if "my" in company:
    print("Условие выполнено!")
Условие выполнено!
```

In [2]:

```python
company = "example.net"

if "my" in company or company.endswith(".net"):
    print("Условие выполнено!")
Условие выполнено!
```

### if - else

Оператор **else** позволяет выполнить какой-либо код, если условие в блоке if не выполнилось:

In [1]:

```python
company = "google.com"

if "my" in company:
    print("Условие выполнено!")
else:
    print("Условие не выполнено!")
Условие не выполнено!
```

### if - elif - else

Оператор **elif** используется, когда нужно проверить несколько разных условий друг за другом:

In [2]:

```python
company = "google.com"

if "my" in company:
    print("Подстрока my найдена")
elif "google" in company:
    print("Подстрока google найдена")
else:
    print("Подстрока не найдена")
Подстрока google найдена
```

### Аналог тернарного оператора

In [3]:

```python
score_1 = 5
score_2 = 0

winner = "Argentina" if score_1 > score_2  else "Jamaica"

print(winner)
Argentina
```

### while

Оператор **while** позволяет выполнять блок кода до тех пор пока выполняется условие:

In [4]:

```python
i = 0

while i < 100:
    i += 1

print(i)
100
```

### Цикл for, объект range

Выражение **for .. in** это еще один способ выполнить блок кода - но оно позволяет выполнить блок кода для каждого из элементов из последовательности:

In [5]:

```python
name = "Alex"

for letter in name:
    print(letter)
A
l
e
x
```

Встроенный объект **range** позволяет итерироваться по целым числам:

In [9]:

```python
for i in range(3):
    print(i)
0
1
2
```

In [6]:

```python
result = 0

for i in range(101):
    result += i

print(result)
5050
```

In [8]:

```python
for i in range(5, 8):
    print(i)
5
6
7
```

In [9]:

```python
for i in range(1, 10, 2):
    print(i)
1
3
5
7
9
```

In [10]:

```python
for i in range(10, 5, -1):
    print(i)
10
9
8
7
6
```

### pass

Определяет пустой блок, который ничего не делает

In [11]:

```python
for i in range(100):
    pass
```

### break

Оператор **break** позволяет выйти из цикла досрочно:

In [15]:

```python
result = 0

while True:
    result += 1
    if result >= 100:
        break

print(result)
100
```

In [16]:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
0
1
2
3
4
```

### continue

Оператор **continue** используется, когда в блоке цикла нужно перейти к следующей итерации цикла без выполнения оставшихся инструкций в блоке:

In [17]:

```python
result = 0

for i in range(10):
    if i % 2 != 0:
        continue
    result += i

print(result)
20
```

### Применим на практике

In [16]:

```python
import random

number = random.randint(0, 101)

while True:
    answer = input('Угадайте число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdigit():
        print("Введите правильное число")
        continue
        
    answer = int(answer)
    
    if answer == number:
        print('Совершенно верно!')
        break

    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
Угадайте число: exit
Выход из программы
```



## Requests

```python
import requests
import pprint

def get_location_info():
    return requests.get("http://ip-api.com/json/").json()

if __name__ == "__main__":
    pprint.pprint(get_location_info())
{'city': 'Moscow',
 'country_code': 'RU',
 'country_name': 'Russia',
 'ip': '46.39.229.63',
 'latitude': 55.7485,
 'longitude': 37.6184,
 'metro_code': 0,
 'region_code': 'MOW',
 'region_name': 'Moscow',
 'time_zone': 'Europe/Moscow',
 'zip_code': '101194'}
```



## Объектная структура в Python

```python
num = 13
```

In [4]:

```python
num.__add__(2)
```

Out[4]:

```python
15
```

In [13]:

```python
print(dir(num))
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

In [2]:

```python
print(dir("строка"))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;         // Счетчик ссылок
    struct _typeobject *ob_type;  // Указатель на тип объекта
} PyObject;
typedef struct {
    PyObject ob_base;
    Py_ssize_t ob_size;  // Кол-во элементов в переменной части
} PyVarObject;
typedef struct {
    PyObject ob_base;
    Py_ssize_t ob_size; // Кол-во элементов в переменной части
} PyVarObject;
#define PyObject_HEAD  PyObject ob_base;

#define PyObject_VAR_HEAD  PyVarObject ob_base;
typedef struct PyMyObject {
   PyObject_HEAD
   ...
}
```

или

```python
typedef struct PyMyObject {
   PyObject_VAR_HEAD
   ...
}
```

Практически все в Python наследуется от PyObject, является объектом и может быть присвоено переменной и быть передано в качестве аргумента в функцию! Не только базовые типы, такие как int, float, bool, str и т.д., но также и функции и даже модули, содержащие наш код на Python.

Теперь вы знаете, что почти все в Python имплементировано как объект, у каждого такого объекта есть счетчик ссылок и описание типа, и в конечном итоге у объекта определенного типа есть масса методов и атрибутов, которые мы с вами видели, например, вызывая функцию dir с целочисленным объектом в качестве аргумента. Также раскрыта тайна почему я постоянно произносил что мы связываем имя переменной с объектом, а не просто что мы присваиваем переменной значение. Я хотел подчеркнуть особенность объектной структуры Python, о которой мы только что поговорили.



## Коллекции

### Списки

Список — это упорядоченный набор объектов, хранящихся в одной переменной. В отличие от массивов в других языках, у списков нет никаких ограничений на тип переменных, поэтому в них могут храниться разные объекты, в том числе и другие коллекции.

In [1]:

```python
empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]
```

В питоне не нужно явно указывать размер списка или вручную выделять на него память. Длину списка можно узнать с помощью встроенной функции len. Размер списка хранится в структуре, с помощью которой реализован тип список, поэтому длина вычисляется за константное время.

In [2]:

```python
len(collections)
```

Out[2]:

```python
4
```

#### Индексы и срезы

Чтобы обратиться к конкретному элементу списка, мы используем тот же механизм, что и для строк. Нумерация элементов начинается с нуля.

In [3]:

```python
print(collections)

print(collections[0])
print(collections[-1])
['list', 'tuple', 'dict', 'set']
list
set
```

Мы можем использовать доступ по индексу для присваивания.

In [4]:

```python
collections[3] = 'frozenset'
print(collections)
['list', 'tuple', 'dict', 'frozenset']
```

Если попробовать обратиться к несуществующему индексу, то возникнет ошибка

In [5]:

```python
collections[10]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-5-218b950f302f> in <module>()
----> 1 collections[10]

IndexError: list index out of range
```

Проверить, содержит ли список некоторый объект, можно с помощью ключевого слова "in"

In [6]:

```python
'tuple' in collections
```

Out[6]:

```python
True
```

Срезы в списках работают точно так же, как и в строках. Создадим список из 10 элементов с помощью встроенной функции range.

In [7]:

```python
range_list = list(range(10))
print(range_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In [8]:

```python
range_list[1:3]
```

Out[8]:

```python
[1, 2]
```

In [9]:

```python
range_list[3:]
```

Out[9]:

```python
[3, 4, 5, 6, 7, 8, 9]
```

In [10]:

```python
range_list[:5]
```

Out[10]:

```python
[0, 1, 2, 3, 4]
```

In [11]:

```python
print(range_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In [12]:

```python
range_list[::2]
```

Out[12]:

```python
[0, 2, 4, 6, 8]
```

In [13]:

```python
range_list[::-1]
```

Out[13]:

```python
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

In [14]:

```python
range_list[1::2]
```

Out[14]:

```python
[1, 3, 5, 7, 9]
```

In [15]:

```python
range_list[5:1:-1]
```

Out[15]:

```python
[5, 4, 3, 2]
```

In [16]:

```python
range_list[:] is range_list
```

Out[16]:

```python
False
```

#### Итерация

Списки как и строки поддерживают протокол итерации

In [17]:

```python
collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}...'.format(collection))
Learning list...
Learning tuple...
Learning dict...
Learning set...
```

Часто бывает нужно получить индекс текущего элемента при итерации. Для этого можно использовать встроенную функцию enumerate

In [18]:

```python
for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))
#0 list
#1 tuple
#2 dict
#3 set
```

#### Добавление и удаление элементов

Списки, в отличие от строк, являются изменяемой структурой данных, а значит мы можем добавлять элементы в существующий список.

In [19]:

```python
collections.append('OrderedDict')

print(collections)
['list', 'tuple', 'dict', 'set', 'OrderedDict']
```

In [20]:

```python
collections.extend(['ponyset', 'unicorndict'])

print(collections)
['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict']
```

In [21]:

```python
collections += [None]

print(collections)
['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict', None]
```

Для удаление элемента из списка можно использовать ключевое слово del.

In [22]:

```python
del collections[4]

print(collections)
['list', 'tuple', 'dict', 'set', 'ponyset', 'unicorndict', None]
```

#### min, max, sum

Часто нам нужно найти минимальный, максимальный элемент в массиве или посчитать сумму всех элементов, сделать это можно с помощью встроенных функций min/max/sum.

In [23]:

```python
numbers = [4, 17, 19, 9, 2, 6, 10, 13]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
2
19
80
```

#### str.join

Часто бывает полезно преобразовать список в строку, для этого можно использовать метод str.join()

In [24]:

```python
tag_list = ['python', 'course', 'coursera']

print(', '.join(tag_list))
python, course, coursera
```

#### Сортировка

In [25]:

```python
import random


numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 20))
    
print(numbers)
[13, 9, 10, 1, 1, 13, 14, 1, 16, 4]
```

Для сортировки списка в питоне есть два способа: стандартная функция sorted, которая возвращает новый список, полученный сортировкой исходного, и метод списка .sort(), который сортирует in-place. Для сортирвоки используется алгоритм TimSort.

In [26]:

```python
print(sorted(numbers))
print(numbers)
[1, 1, 1, 4, 9, 10, 13, 13, 14, 16]
[13, 9, 10, 1, 1, 13, 14, 1, 16, 4]
```

In [27]:

```python
numbers.sort()
print(numbers)
[1, 1, 1, 4, 9, 10, 13, 13, 14, 16]
```

Часто бывает нужно отсортировать список в обратном порядке

In [28]:

```python
print(sorted(numbers, reverse=True))
[16, 14, 13, 13, 10, 9, 4, 1, 1, 1]
```

In [29]:

```python
numbers.sort(reverse=True)
print(numbers)
[16, 14, 13, 13, 10, 9, 4, 1, 1, 1]
```

In [30]:

```python
print(reversed(numbers))
<list_reverseiterator object at 0x107067e10>
```

In [31]:

```python
print(list(reversed(numbers)))
[1, 1, 1, 4, 9, 10, 13, 13, 14, 16]
```

#### Методы

Кроме рассмотренных выше методов у списка есть и другие. Об этих методах вы можете почитать в документации или help(list).

- append
- clear
- copy
- count
- extend
- index
- insert
- pop
- remove
- reverse
- sort

### Кортежи

Кортеж — по сути это неизменяемый список, который мы можем хэшировать, а значит использовать в качестве ключа в словарях, о которых мы поговорим позже.

In [32]:

```python
empty_tuple = ()
empty_tuple = tuple()
```

In [33]:

```python
immutables = (int, str, tuple)
```

In [34]:

```python
immutables[0] = float
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-70298ebdccb5> in <module>()
----> 1 immutables[0] = float

TypeError: 'tuple' object does not support item assignment
```

In [35]:

```python
blink = ([], [])
blink[0].append(0)

print(blink)
([0], [])
```

In [36]:

```python
hash(tuple())
```

Out[36]:

```python
3527539
```

In [37]:

```python
one_element_tuple = (1,)
guess_what = (1)

type(guess_what)
```

Out[37]:

```python
int
```

**Списки**

- Упорядоченный **изменяемый** набор объектов
- Поддерживают индексы и срезы
- Поддерживают итерацию
- Встроенные функции и методы

**Кортежи**

- Упорядоченный **неизменяемый** набор объектов
- Похожи на списки с поправкой на неизменяемость
- Хэшируемы

### Словари

Словари в питоне хранят данные в виде пары ключ-значение. Ключи должны быть хэшируемы и в обычном словаре хранятся без гарантии порядка.

In [38]:

```python
empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}
```

Доступ к значению по ключу осуществляется за константное время, то есть не зависит от размера словаря.

In [39]:

```python
print(collections_map['immutable'])
['tuple', 'frozenset']
```

In [40]:

```python
print(collections_map['irresistible'])
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-40-fae0f6f2a221> in <module>()
----> 1 print(collections_map['irresistible'])

KeyError: 'irresistible'
```

Часто бывает полезно попытаться достать значение по ключу из словаря, а в случае отсутствия ключа вернуть какое-то стандартное значение.

In [41]:

```python
print(collections_map.get('irresistible', 'not found'))
not found
```

Проверка на вхождения ключа в словарь так же осуществляется за константное время и выполняется с помощью ключевого слова in

In [42]:

```python
'mutable' in collections_map
```

Out[42]:

```python
True
```

#### Добавление и удаление элементов

Словари в питоне являются изменяемой структурой данных, а значит мы можем добавлять новые значения и удалять не нужные.

In [43]:

```python
beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar',
}

print(beatles_map)
{'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
```

In [44]:

```python
beatles_map['Ringo'] = 'Drums'

print(beatles_map)
{'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar', 'Ringo': 'Drums'}
```

In [45]:

```python
del beatles_map['John']

print(beatles_map)
{'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums'}
```

In [46]:

```python
beatles_map.update({
    'John': 'Guitar'
})

print(beatles_map)
{'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums', 'John': 'Guitar'}
```

In [47]:

```python
print(beatles_map.pop('Ringo'))

print(beatles_map)
Drums
{'Paul': 'Bass', 'George': 'Guitar', 'John': 'Guitar'}
```

In [48]:

```python
unknown_dict = {}

print(unknown_dict.setdefault('key', 'default'))
default
```

In [49]:

```python
print(unknown_dict)
{'key': 'default'}
```

In [50]:

```python
print(unknown_dict.setdefault('key', 'new_default'))
default
```

#### Итерация

Словари как и другие коллекции поддерживает протокол итерации и по умолчанию итерация идет по ключам.

In [51]:

```python
print(collections_map)

for key in collections_map:
    print(key)
{'mutable': ['list', 'set', 'dict'], 'immutable': ['tuple', 'frozenset']}
mutable
immutable
```

Для итерации по ключам и значениям одновременно используется метод словаря .items().

In [52]:

```python
for key, value in collections_map.items():
    print('{} — {}'.format(key, value))
mutable — ['list', 'set', 'dict']
immutable — ['tuple', 'frozenset']
```

In [53]:

```python
for value in collections_map.values():
    print(value)
['list', 'set', 'dict']
['tuple', 'frozenset']
```

#### OrderedDict

In [54]:

```python
from collections import OrderedDict


ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)
    
for key in ordered:
    print(key)
0
1
2
3
4
5
6
7
8
9
```

**Словари**

- Изменяемый неупорядоченный набор пар ключ-значение
- Быстрый доступ к значению по ключу
- Быстрая проверка на вхождение ключа в словарь

### Множества

Множество в питоне — это неупорядоченный набор уникальных объектов. Множества изменяемы и чаще всего используются для удаление дубликатов и всевозможных проверок на вхождение.

In [55]:

```python
empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}

print(number_set)
{1, 2, 3, 4, 5}
```

Чтобы проверить, содержится ли объект в множестве, используется уже знакомое нам ключевое слово in. Проверка выполняется за константное время, время выполнения операции не зависит от размера множества. Это достигается засчет хэширования каждого элемента структуры по аналогии со словарями. По полученному от хэш-функции ключу и происходит поиск объекта. Таким образом во множествах могут содержаться только хэшируемые объекты.

In [56]:

```python
print(2 in number_set)
True
```

Чтобы добавить элемент в множество, используется метод add. Так же множества в питоне поддерживают стандартные операции на множествами, такие как объединение, разность, пересечение и симметрическая разность.

In [57]:

```python
odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)
        
print(odd_set)
print(even_set)
{1, 3, 5, 7, 9}
{0, 2, 4, 6, 8}
```

In [58]:

```python
union_set = odd_set | even_set
union_set = odd_set.union(even_set)

print(union_set)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

In [59]:

```python
intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)

print(intersection_set)
set()
```

In [60]:

```python
difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)

print(difference_set)
{1, 3, 5, 7, 9}
```

In [61]:

```python
symmetric_difference_set = odd_set ^ even_set
symmetric_difference_set = odd_set.symmetric_difference(even_set)

print(symmetric_difference_set)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

Для удаления конкретного элемента существует метод remove, для удаления любого можно использовать pop. Остальные методы можно посмотреть в help или документации.

In [62]:

```python
even_set.remove(2)
print(even_set)
{0, 4, 6, 8}
```

In [63]:

```python
even_set.pop()
```

Out[63]:

```python
0
```

Также в питоне существует тип frozenset, который является неизменяемым множеством.

In [64]:

```python
frozen = frozenset(['Anna', 'Elsa', 'Kristoff'])

frozen.add('Olaf')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-64-962f221e1321> in <module>()
      1 frozen = frozenset(['Anna', 'Elsa', 'Kristoff'])
      2 
----> 3 frozen.add('Olaf')

AttributeError: 'frozenset' object has no attribute 'add'
```

**Множества**

- Изменяемый неупорядоченный набор уникальных объектов
- Быстрая проверка на вхождение
- Математические операции над множествами



### Найти медиану случайного списка

In [1]:

```python
import random


numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))
    
print(numbers)
[16, 10, 12, 16, 16, 10, 11, 18, 14, 10]
```

In [2]:

```python
numbers.sort()

half_size = len(numbers) // 2
median = None

if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2
    
print(median)
13.0
```

In [3]:

```python
import statistics

statistics.median(numbers)
```

Out[3]:

```python
13.0
```



### Найти 3 самых часто встречающихся слова в Zen of Python

In [1]:

```python
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

In [2]:

```python
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
```

In [3]:

```python
zen_map = dict()

for word in zen.split():
    cleaned_word = word.strip('.,!-*').lower()
    if cleaned_word not in zen_map:
        zen_map[cleaned_word] = 0
        
    zen_map[cleaned_word] += 1
    
print(zen_map)
{'beautiful': 1, 'is': 10, 'better': 8, 'than': 8, 'ugly': 1, 'explicit': 1, 'implicit': 1, 'simple': 1, 'complex': 2, 'complicated': 1, 'flat': 1, 'nested': 1, 'sparse': 1, 'dense': 1, 'readability': 1, 'counts': 1, 'special': 2, 'cases': 1, "aren't": 1, 'enough': 1, 'to': 5, 'break': 1, 'the': 5, 'rules': 1, 'although': 3, 'practicality': 1, 'beats': 1, 'purity': 1, 'errors': 1, 'should': 2, 'never': 3, 'pass': 1, 'silently': 1, 'unless': 2, 'explicitly': 1, 'silenced': 1, 'in': 1, 'face': 1, 'of': 2, 'ambiguity': 1, 'refuse': 1, 'temptation': 1, 'guess': 1, 'there': 1, 'be': 3, 'one': 3, 'and': 1, 'preferably': 1, 'only': 1, 'obvious': 2, 'way': 2, 'do': 2, 'it': 2, 'that': 1, 'may': 2, 'not': 1, 'at': 1, 'first': 1, "you're": 1, 'dutch': 1, 'now': 2, 'often': 1, 'right': 1, 'if': 2, 'implementation': 2, 'hard': 1, 'explain': 2, "it's": 1, 'a': 2, 'bad': 1, 'idea': 3, 'easy': 1, 'good': 1, 'namespaces': 1, 'are': 1, 'honking': 1, 'great': 1, '': 1, "let's": 1, 'more': 1, 'those': 1}
```

In [4]:

```python
import operator

zen_items = zen_map.items()
word_count_items = sorted(
    zen_items, key=operator.itemgetter(1), reverse=True
)

print(word_count_items[:3])
[('is', 10), ('better', 8), ('than', 8)]
```

In [5]:

```python
from collections import Counter


cleaned_list = []
for word in zen.split():
    cleaned_list.append(word.strip('.,-!').lower())
    
    
print(Counter(cleaned_list).most_common(3))
[('is', 10), ('better', 8), ('than', 8)]
```



### Через сколько итераций функция random.randint(1, 10) выдаст повтор?

In [1]:

```python
import random


random_set = set()

while True:
    new_number = random.randint(1, 10)
    if new_number in random_set:
        break
        
    random_set.add(new_number)
    

print(len(random_set) + 1)
6
```



## Функции

In [1]:

```python
from datetime import datetime


def get_seconds():
    """Return current seconds"""
    return datetime.now().second


get_seconds()
```

Out[1]:

```python
24
```

In [2]:

```python
get_seconds.__doc__
```

Out[2]:

```python
'Return current seconds'
```

In [3]:

```python
get_seconds.__name__
```

Out[3]:

```python
'get_seconds'
```

In [4]:

```python
def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())
    
    return tag_list


split_tags('python, coursera, mooc')
```

Out[4]:

```python
['python', 'coursera', 'mooc']
```

In [5]:

```python
split_tags()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-866c00aba286> in <module>()
----> 1 split_tags()

TypeError: split_tags() missing 1 required positional argument: 'tag_string'
```

### Аннотация типов

In [6]:

```python
def add(x: int, y: int) -> int:
    return x + y


print(add(10, 11))
print(add('still ', 'works'))
21
still works
```

### По ссылке или по значению?

In [7]:

```python
def extender(source_list, extend_list):
    source_list.extend(extend_list)
    

values = [1, 2, 3]
extender(values, [4, 5, 6])

print(values)
[1, 2, 3, 4, 5, 6]
```

In [8]:

```python
def replacer(source_tuple, replace_with):
    source_tuple = replace_with
    

user_info = ('Guido', '31/01')
replacer(user_info, ('Larry', '27/09'))

print(user_info)
('Guido', '31/01')
```

### Именованные аргументы

In [9]:

```python
def say(greeting, name):
    print('{} {}!'.format(greeting, name))
    

say('Hello', 'Kitty')
say(name='Kitty', greeting='Hello')
Hello Kitty!
Hello Kitty!
```

### Область видимости

In [10]:

```python
result = 0

def increment():
    result += 1
    return result

print(increment())
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-10-da69e363a112> in <module>()
      5     return result
      6 
----> 7 print(increment())

<ipython-input-10-da69e363a112> in increment()
      2 
      3 def increment():
----> 4     result += 1
      5     return result
      6 

UnboundLocalError: local variable 'result' referenced before assignment
```

### global & nonlocal

### Аргументы по умолчанию

In [11]:

```python
def greeting(name='it\'s me...'):
    print('Hello, {}'.format(name))
    
    
greeting()
Hello, it's me...
```

In [12]:

```python
def append_one(iterable=[]):
    iterable.append(1)
    
    return iterable


print(append_one([1]))
[1, 1]
```

In [13]:

```python
print(append_one())
print(append_one())
[1]
[1, 1]
```

In [14]:

```python
print(append_one.__defaults__)
([1, 1],)
```

In [15]:

```python
def function(iterable=None):
    if iterable is None:
        iterable = []
    

def function(iterable=None):
    iterable = iterable or []
```

### Звездочки

In [16]:

```python
def printer(*args):
    print(type(args))
    
    for argument in args:
        print(argument)


printer(1, 2, 3, 4, 5)
<class 'tuple'>
1
2
3
4
5
```

In [17]:

```python
name_list = ['John', 'Bill', 'Amy']
printer(*name_list)
<class 'tuple'>
John
Bill
Amy
```

In [18]:

```python
def printer(**kwargs):
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))
        
        
printer(a=10, b=11)
<class 'dict'>
a: 10
b: 11
```

In [19]:

```python
payload = {
    'user_id': 117,
    'feedback': {
        'subject': 'Registration fields',
        'message': 'There is no country for old men'
    }
}

printer(**payload)
<class 'dict'>
user_id: 117
feedback: {'subject': 'Registration fields', 'message': 'There is no country for old men'}
```



## Файлы

In [71]:

```python
f = open('filename')
```

In [72]:

```python
text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']
```

In [73]:

```python
f = open('filename', 'w')
```

In [74]:

```python
f.write('The world is changed.\nI taste it in the water.\n')
```

Out[74]:

```python
47
```

In [75]:

```python
f.close()
```

In [76]:

```python
f = open('filename', 'r+')
f.read()
```

Out[76]:

```python
'The world is changed.\nI taste it in the water.\n'
```

In [77]:

```python
f.tell()
```

Out[77]:

```python
47
```

In [78]:

```python
f.read()
```

Out[78]:

```python
''
```

In [79]:

```python
f.seek(0)
f.tell()
```

Out[79]:

```python
0
```

In [80]:

```python
print(f.read())
f.close()
The world is changed.
I taste it in the water.
```

In [81]:

```python
f = open('filename', 'r+')
f.readline()
f.close()
```

Out[81]:

```python
'The world is changed.\n'
```

In [82]:

```python
f = open('filename', 'r+')
f.readlines()
```

Out[82]:

```python
['The world is changed.\n', 'I taste it in the water.\n']
```

In [83]:

```python
f.close()
f.read()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-83-94b03372b7c6> in <module>()
      1 f.close()
----> 2 f.read()

ValueError: I/O operation on closed file.
```

In [ ]:

```python
with open('filename') as f:
    print(f.read())
```



## Функциональное программирование

In [1]:

```python
def caller(func, params):
    return func(*params)


def printer(name, origin):
    print('I\'m {} of {}!'.format(name, origin))
    
    
caller(printer, ['Moana', 'Motunui'])
I'm Moana of Motunui!
```

In [2]:

```python
def get_multiplier():
    def inner(a, b):
        return a * b
    return inner
    
    
multiplier = get_multiplier()
multiplier(10, 11)
```

Out[2]:

```python
110
```

In [3]:

```python
print(multiplier.__name__)
inner
```

In [4]:

```python
def get_multiplier(number):
    def inner(a):
        return a * number
    return inner


multiplier_by_2 = get_multiplier(2)
multiplier_by_2(10)
```

Out[4]:

```python
20
```

### map, filter, lambda

In [5]:

```python
def squarify(a):
    return a ** 2


list(map(squarify, range(5)))
```

Out[5]:

```python
[0, 1, 4, 9, 16]
```

In [6]:

```python
squared_list = []

for number in range(5):
    squared_list.append(squarify(number))
    
print(squared_list)
[0, 1, 4, 9, 16]
```

In [7]:

```python
def is_positive(a):
    return a > 0


list(filter(is_positive, range(-2, 3)))
```

Out[7]:

```python
[1, 2]
```

In [8]:

```python
positive_list = []

for number in range(-2, 3):
    if is_positive(number):
        positive_list.append(number)
        
print(positive_list)
[1, 2]
```

In [9]:

```python
list(map(lambda x: x ** 2, range(5)))
```

Out[9]:

```python
[0, 1, 4, 9, 16]
```

In [10]:

```python
type(lambda x: x ** 2)
```

Out[10]:

```python
function
```

In [11]:

```python
list(filter(lambda x: x > 0, range(-2, 3)))
```

Out[11]:

```python
[1, 2]
```

### Написать функцию, которая превращает список чисел в список строк

In [12]:

```python
def stringify_list(num_list):
    return list(map(str, num_list))


stringify_list(range(10))
```

Out[12]:

```python
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

### functools

In [13]:

```python
from functools import reduce


def multiply(a, b):
    return a * b


reduce(multiply, [1, 2, 3, 4, 5])
```

Out[13]:

```python
120
```

In [14]:

```python
reduce(lambda x, y: x * y, range(1, 5))
```

Out[14]:

```python
24
```

In [15]:

```python
from functools import partial


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)


hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')


print(hier('brother'))
print(helloer('sir'))
Hi, brother!
Hello, sir!
```

### Списочные выражения (list comprehension)

До этого момента мы с вами определяли списки стандартным способом, однако в питоне существует более красивая и лаконичная конструкция для создания списков и других коллекций.

In [16]:

```python
square_list = []
for number in range(10):
    square_list.append(number ** 2)
    
print(square_list)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

In [17]:

```python
square_list = [number ** 2 for number in range(10)]
print(square_list)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

In [18]:

```python
even_list = []
for number in range(10):
    if number % 2 == 0:
        even_list.append(number)
        
print(even_list)
[0, 2, 4, 6, 8]
```

In [19]:

```python
even_list = [num for num in range(10) if num % 2 == 0]

print(even_list)
[0, 2, 4, 6, 8]
```

In [20]:

```python
square_map = {number: number ** 2 for number in range(5)}

print(square_map)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

In [21]:

```python
reminders_set = {num % 10 for num in range(100)}

print(reminders_set)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

In [22]:

```python
print(type(number ** 2 for number in range(5)))
<class 'generator'>
```

In [23]:

```python
num_list = range(7)
squared_list = [x ** 2 for x in num_list]

list(zip(num_list, squared_list))
```

Out[23]:

```python
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
```

**Функциональное программирование**

- Функции — объекты первого класса
- map, filter, reduce, partial
- lambda — анонимные функции
- Списочные выражения



## Декораторы

In [1]:

```python
def decorator(func):
    return func


@decorator
def decorated():
    print('Hello!')
```

In [2]:

```python
decorated = decorator(decorated)
```

In [3]:

```python
def decorator(func):
    def new_func():
        pass
    return new_func


@decorator
def decorated():
    print('Hello!')
    
    
decorated()
```

In [4]:

```python
print(decorated.__name__)
new_func
```

### Написать декоратор, который записывает в лог результат декорируемой функции

In [5]:

```python
import functools


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result    
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


print('Summator: {}'.format(summator([1, 2, 3, 4])))

print(summator.__name__)
Summator: 10
summator
```

### Написать декоратор с параметром, который записывает лог в указанный файл

In [7]:

```python
def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator


@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)


# summator = logger('log.txt')(summator)


summator([1, 2, 3, 4, 5, 6])

with open('new_log.txt', 'r') as f:
    print(f.read())
21
```

In [8]:

```python
def first_decorator(func):
    def wrapped():
        print('Inside first_decorator product')
        return func()
    return wrapped


def second_decorator(func):
    def wrapped():
        print('Inside second_decorator product')
        return func()
    return wrapped
```

In [9]:

```python
@first_decorator
@second_decorator
def decorated():
    print('Finally called...')
    
    
# decorated = first_decorator(second_decorator(decorated))
    

decorated()
Inside first_decorator product
Inside second_decorator product
Finally called...
```

In [10]:

```python
def bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped


def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped


@bold
@italic
def hello():
    return "hello world"


# hello = bold(italic(hello))


print(hello())
<b><i>hello world</i></b>
```



## Генераторы

In [1]:

```python
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2
```

In [2]:

```python
for number in even_range(0, 10):
    print(number)
0
2
4
6
8
```

In [3]:

```python
ranger = even_range(0, 4)
```

In [4]:

```python
next(ranger)
```

Out[4]:

```python
0
```

In [5]:

```python
next(ranger)
```

Out[5]:

```python
2
```

In [6]:

```python
next(ranger)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-6-9065b0f81b55> in <module>()
----> 1 next(ranger)

StopIteration: 
```

In [7]:

```python
def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))


generator = list_generator([1, 2])
```

In [8]:

```python
next(generator)
```

Out[8]:

```python
1
```

In [9]:

```python
next(generator)
After yielding 1
```

Out[9]:

```python
2
```

In [10]:

```python
next(generator)
After yielding 2
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-10-1d0a8ea12077> in <module>()
----> 1 next(generator)

StopIteration: 
```

In [11]:

```python
def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b
```

In [12]:

```python
for num in fibonacci(10):
    print(num)
1
1
2
3
5
8
13
21
34
55
```

In [13]:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()
```

In [14]:

```python
next(generator)
```

Out[14]:

```python
0
```

In [15]:

```python
print('Accumulated: {}'.format(generator.send(1)))
Got: 1
Accumulated: 1
```

In [16]:

```python
print('Accumulated: {}'.format(generator.send(1)))
Got: 1
Accumulated: 2
```

In [17]:

```python
print('Accumulated: {}'.format(generator.send(1)))
Got: 1
Accumulated: 3
```

In [18]:

```python
next(generator)
Got: None
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-18-1d0a8ea12077> in <module>()
----> 1 next(generator)

StopIteration: 
```



## ООП

```python
print(dict)
<class 'dict'>
```

In [7]:

```python
print(int)
<class 'int'>
```

In [9]:

```python
print(int)
<class 'int'>
```

In [12]:

```python
num = 13.0
print(type(num))
<class 'float'>
```

### isinstance

In [15]:

```python
num = 13
isinstance(num, int)
```

Out[15]:

```python
True
```

In [16]:

```python
numbers = {}
isinstance(numbers, dict)
```

Out[16]:

```python
True
```

### Объявление класса

In [2]:

```python
class Human:
    pass
```

In [3]:

```python
class Robot:
    """Данный класс позволяет создавать роботов"""
```

In [4]:

```python
print(Robot)
<class '__main__.Robot'>
```

In [6]:

```python
print(dir(Robot))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

### Создание экземпляра (объекта) класса

In [8]:

```python
class Planet:
    pass
```

In [9]:

```python
planet = Planet()
```

In [10]:

```python
print(planet)
<__main__.Planet object at 0x10e8722b0>
```

In [11]:

```python
solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print(solar_system) 
[<__main__.Planet object at 0x10e872780>, <__main__.Planet object at 0x10e8722b0>, <__main__.Planet object at 0x10e8727f0>, <__main__.Planet object at 0x10e872828>, <__main__.Planet object at 0x10e872860>, <__main__.Planet object at 0x10e872898>, <__main__.Planet object at 0x10e8728d0>, <__main__.Planet object at 0x10e872908>]
```

In [14]:

```python
solar_system = {}
for i in range(8):
    planet = Planet()
    solar_system[planet] = True

print(solar_system)
{<__main__.Planet object at 0x10e872978>: True, <__main__.Planet object at 0x10e872908>: True, <__main__.Planet object at 0x10e8727f0>: True, <__main__.Planet object at 0x10e872828>: True, <__main__.Planet object at 0x10e872860>: True, <__main__.Planet object at 0x10e872898>: True, <__main__.Planet object at 0x10e8729e8>: True, <__main__.Planet object at 0x10e872940>: True}
```

### Инициализация экземпляра

In [16]:

```python
class Planet:
    
    def __init__(self, name):
        self.name = name
```

In [17]:

```python
earth = Planet("Earth")
print(earth.name)
print(earth)
Earth
<__main__.Planet object at 0x10e8796d8>
```

In [10]:

```python
class Planet:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


earth = Planet("Earth")
print(earth)
Earth
```

In [11]:

```python
solar_system = []

planet_names = [
    "Mercury", "Venus", "Earth", "Mars", 
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
[<__main__.Planet object at 0x10477f160>, <__main__.Planet object at 0x10477f278>, <__main__.Planet object at 0x10477f198>, <__main__.Planet object at 0x10477f1d0>, <__main__.Planet object at 0x10477f208>, <__main__.Planet object at 0x10477f240>, <__main__.Planet object at 0x1048637b8>, <__main__.Planet object at 0x1048637f0>]
```

In [2]:

```python
class Planet:
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Planet {self.name}"
```

In [3]:

```python
solar_system = []

planet_names = [
    "Mercury", "Venus", "Earth", "Mars", 
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
[Planet Mercury, Planet Venus, Planet Earth, Planet Mars, Planet Jupiter, Planet Saturn, Planet Uranus, Planet Neptune]
```

### Работа с атрибутами экземпляра

In [4]:

```python
mars = Planet("Mars")
print(mars)
Planet Mars
```

In [5]:

```python
mars.name
```

Out[5]:

```python
'Mars'
```

In [6]:

```python
mars.name = "Second Earth?"
mars.name
```

Out[6]:

```python
'Second Earth?'
```

In [7]:

```python
mars.mass
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-7-3c1085af8f48> in <module>()
----> 1 mars.mass

AttributeError: 'Planet' object has no attribute 'mass'
```

In [8]:

```python
del mars.name
```

In [9]:

```python
mars.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-9-202092835a22> in <module>()
----> 1 mars.name

AttributeError: 'Planet' object has no attribute 'name'
```

Мы с вами:

- Посмотрели как объявлять классы
- Научились создавать экземпляры (объекты) классов
- Рассмотрели как инициализировать экземпляр класса
- Научились работать с атрибутами экземпляра класса



### Атрибуты класса

In [18]:

```python
class Planet:
 
    count = 0
 
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1
```

In [13]:

```python
earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)
2
```

In [14]:

```python
mars.count
```

Out[14]:

```python
2
```

### Деструктор экземпляра класса

In [162]:

```python
class Human:

    def __del__(self):
        print("Goodbye!")
```

In [163]:

```python
human = Human()
# в данном случае деструктор отработает - но все же 
# лучше создать метод и вызывать его явно
del human
Goodbye!
```

### Словарь экземпляра и класса

In [1]:

```python
class Planet:
    """This class describes planets"""
    
    count = 1
    
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []


planet = Planet("Earth")
```

In [2]:

```python
planet.__dict__
```

Out[2]:

```python
{'name': 'Earth', 'population': []}
```

In [3]:

```python
planet.mass = 5.97e24
```

In [4]:

```python
planet.__dict__
```

Out[4]:

```python
{'mass': 5.97e+24, 'name': 'Earth', 'population': []}
```

In [5]:

```python
Planet.__dict__
```

Out[5]:

```python
mappingproxy({'__dict__': <attribute '__dict__' of 'Planet' objects>,
              '__doc__': 'This class describes planets',
              '__init__': <function __main__.Planet.__init__>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Planet' objects>,
              'count': 1})
```

In [6]:

```python
Planet.__doc__
```

Out[6]:

```python
'This class describes planets'
```

In [7]:

```python
planet.__doc__
```

Out[7]:

```python
'This class describes planets'
```

In [8]:

```python
print(dir(planet))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'count', 'mass', 'name', 'population']
```

In [9]:

```python
planet.__class__
```

Out[9]:

```python
__main__.Planet
```

### Конструктор экземпляра класса

In [10]:

```python
class Planet:

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name
```

In [11]:

```python
earth = Planet("Earth")
__new__ called
__init__ called
```

То есть при вызове `Planet("Earth")` произошло примерно следующее:

```python
planet = Planet.__new__(Planet, "Earth")

if isinstance(planet, Planet):              
    Planet.__init__(planet, "Earth")
```

Мы с вами:

- узнали, что такое атрибут класса
- посмотрели на деструктор и конструктор экземпляра
- поговорили о поиске атрибутов в словаре экземпляра и класса



### Работа с методами экземпляра

In [15]:

```python
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
 
    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)
```

In [16]:

```python
mars = Planet("Mars")

bob = Human("Bob")

mars.add_human(bob)
Welcome to Mars, Bob!
```

In [17]:

```python
print(mars.population)
[<__main__.Human object at 0x10e416780>]
```

### Вызов методов из методов

In [9]:

```python
class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age
 
    def _say(self, text):
        print(text)
 
    def say_name(self):
        self._say(f"Hello, I am {self._name}")
 
    def say_how_old(self):
        self._say(f"I am {self._age} years old")
```

In [10]:

```python
bob = Human("Bob", age=29)
```

In [11]:

```python
bob.say_name()
bob.say_how_old()
Hello, I am Bob
I am 29 years old
```

In [14]:

```python
# не рекомендуется!
print(bob._name)

# не рекомендуется!
bob._say("Whatever we want")
Bob
Whatever we want
```

### Метод класса (@classmethod)

In [3]:

```python
class Event:
 
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"
```

In [5]:

```python
from datetime import date

event_description = "Рассказать, что такое @classmethod"
event_date = date.today()

event = Event(event_description, event_date)
print(event)
Event "Рассказать, что такое @classmethod" at 2017-07-09
```

In [ ]:

```python
def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)


class Event:
 
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date
    
    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)
```

In [8]:

```python
event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)
Event "открытие чемпионата мира по футболу" at 2018-06-14
```

In [56]:

```python
dict.fromkeys("12345")
```

Out[56]:

```python
{'1': None, '2': None, '3': None, '4': None, '5': None}
```

В этом видео:

- Научились объявлять и вызывать методы экземпляров
- Посмотрели на метод класса (@classmethod)



### Статический метод класса (@staticmethod)

In [62]:

```python
class Human:
 
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150
```

In [63]:

```python
# можно обращаться от имени класса
Human.is_age_valid(35)
```

Out[63]:

```python
True
```

In [67]:

```python
# или от экземпляра:
human = Human("Old Bobby")
human.is_age_valid(234)
```

Out[67]:

```python
False
```

### Вычисляемые свойства класса (property)

In [101]:

```python
class Robot:

    def __init__(self, power):
        self.power = power
```

In [102]:

```python
wall_e = Robot(100)
wall_e.power = 200
print(wall_e.power)
200
```

In [103]:

```python
wall_e.power = -20
```

In [ ]:

```python
class Robot:

    def __init__(self, power):
        self.power = power
    
    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power
```

In [109]:

```python
wall_e = Robot(100)
wall_e.set_power(-20)
print(wall_e.power)
0
```

In [142]:

```python
class Robot:
 
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power
    
    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power
```

In [143]:

```python
wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)
0
```

In [144]:

```python
del wall_e.power
make robot useless
```

In [148]:

```python
class Robot:
    def __init__(self, power):
        self._power = power
    
    @property
    def power(self):
        # здесь могут быть любые полезные вычисления
        return self._power
```

In [149]:

```python
wall_e = Robot(200)
wall_e.power
```

Out[149]:

```python
200
```

В этом видео:

- Узнали, что такое статический метод (@staticmethod)
- Узнали, что такое свойство класса (@property)



```python
import sys
import pprint
import requests
from dateutil.parser import parse


class YahooWeatherForecast:

    #def __init__(self):
    #    self._city_cache = {}

    def get(self, city):
        #if city in self._cached_data:
        #     return self._cached_data[city]
        url = f"https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%22)%20and%20u%3D%27c%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        data = requests.get(url).json()
        forecast = []
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": int(day_data["high"])
            })
        #self._cached_data[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city.lower()
        self._forecast_provider = forecast_provider or YahooWeatherForecast()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def _main():
    city = CityInfo(sys.argv[1])
    forecast = city.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    _main()
[{'date': datetime.datetime(2017, 9, 5, 0, 0), 'high_temp': 18},
 {'date': datetime.datetime(2017, 9, 6, 0, 0), 'high_temp': 28},
 {'date': datetime.datetime(2017, 9, 7, 0, 0), 'high_temp': 33},
 {'date': datetime.datetime(2017, 9, 8, 0, 0), 'high_temp': 33},
 {'date': datetime.datetime(2017, 9, 9, 0, 0), 'high_temp': 34},
 {'date': datetime.datetime(2017, 9, 10, 0, 0), 'high_temp': 30},
 {'date': datetime.datetime(2017, 9, 11, 0, 0), 'high_temp': 22},
 {'date': datetime.datetime(2017, 9, 12, 0, 0), 'high_temp': 18},
 {'date': datetime.datetime(2017, 9, 13, 0, 0), 'high_temp': 23},
 {'date': datetime.datetime(2017, 9, 14, 0, 0), 'high_temp': 26}]
```



### Наследование в Python

- наследование классов
- множественное наследование
- вызов super()
- name mangling
- композиция vs наследование

### Зачем нужно наследование классов?

- изменение поведения класса
- расширение функционала класса

### Класс Pet, домашний питомец

In [ ]:

```python
class Pet:
    def __init__(self, name=None):
        self.name = name
```

### Наследование, класс Dog

In [ ]:

```python
class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed
    
    def say(self):
        return "{0}: waw".format(self.name)

>>> dog = Dog("Шарик", "Доберман")
>>> print(dog.name)
Шарик
>>> print(dog.say())
Шарик: waw!
>>> 
```

### Множественное наследование

In [ ]:

```python
import json 

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })

class ExDog(Dog, ExportJSON):
    pass

>>> dog = ExDog("Белка", breed="Дворняжка")
>>> print(dog.to_json())
{"name": "\u0411\u0435\u043b\u043a\u0430", "breed": "\u0414\u0432\u043e\u0440\u043d\u044f\u0436\u043a\u0430"}
```

### Любой класс является потомком object

In [ ]:

```python
>>> issubclass(int, object)
True
>>> issubclass(Dog, object)
True
>>> issubclass(Dog, Pet)
True
>>> issubclass(Dog, int)
False
```

### Объект является экземляром класса?

In [ ]:

```python
>>> isinstance(dog, Dog)
True
>>> isinstance(dog, Pet)
True
>>> isinstance(dog, object)
True
```

### Поиск атрибутов и методов объекта, линеаризация класса

In [ ]:

```python
#     object
#     /   \
#    /     \
#  Pet    ExportJSON
#   |      /
#  Dog    /
#    \   /
#    ExDog

# Method Resolution Order
>>> ExDog.__mro__
(<class '__main__.ExDog'>, <class '__main__.Dog'>, 
 <class '__main__.Pet'>, <class '__main__.ExportJSON'>, 
 <class 'object'>)
>>> 
```

### Использование super()

In [ ]:

```python
>>> ExDog.__mro__
(<class '__main__.ExDog'>, <class '__main__.Dog'>, 
 <class '__main__.Pet'>, <class '__main__.ExportJSON'>, 
 <class 'object'>)

class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # вызов метода по MRO
        super().__init__(name, breed)
        # super(ExDog, self).__init__(name)
        
class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)

>>> dog = WoolenDog("Жучка", breed="Такса")
>>> print(dog.breed)
Шерстяная собака породы Такса
```

### Разрешение конфликта имен, name mangling

In [ ]:

```python
class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed
    
    def say(self):
        return "{0}: waw!".format(self.name)
    
    def get_breed(self):
        return self.__breed

class ExDog(Dog, ExportJSON):
    def get_breed(self):
        return "порода: {0} - {1}".format(self.name, self.__breed)

>>> dog = ExDog("Фокс", "Мопс")
>>> dog.__dict__
{'name': 'Фокс', '_Dog__breed': 'Мопс'}
>>> dog.get_breed()
```

### Композиция классов или наследование?

In [ ]:

```python
class Pet:
    pass

class Dog(Pet):
    pass

class ExportJSON(Pet):
    pass

class ExDog(Dog, ExportJSON)
    pass
```

### Композиция VS наследование

In [ ]:

```python
class ExportJSON:
    def to_json(self):
        pass
    
class ExportXML:
    def to_xml(self):
        pass

class ExDog(Dog, ExportJSON, ExportXML):
      pass

>>> dog = ExDog("Фокс", "мопс")
>>> dog.to_xml()
>>> dog.to_json()
```

In [ ]:

```python
### Композиция классов против наследования, пример буду вводить в онлайн

import json


class Pet:
    def __init__(self, name):
        self,name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed
    
    def say(self):
        return "{0}: waw".format(self.name)


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class ExportXML(PetExport):
    def export(self, dog):
        return """<xml version="1.0" encoding="utf-8">
<dog>
  <name>{0}</name>
  <breed>{1}</breed>
</dog>""".format(dog.name, dog.breed)


class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed,
        })


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        
        self._exporter = exporter or ExportJSON()

        if not isinstance(self._exporter, PetExport):
            raise ValueEror("bad export instance value", exporter)
    
    def export(self):
        return self._exporter.export(self)


>>> fox = ExDog("Фокс", "мопс", exporter=ExportXML())
>>> print(fox.export())
<xml version="1.0" encoding="utf-8">
<dog>
  <name>Фокс</name>
  <breed>мопс</breed>
</dog>
>>> 
>>> muhtar = ExDog("Мухтар", "питбуль")
>>> print(muhtar.export())
{"name": "\u0414\u0436\u0435\u043a", "breed": "\u043c\u043e\u043f\u0441"}
```



## Исключения в Python

- генерация исключений
- типы исключений
- обработка исключений

### Типы исключений

- исключения стандартной библиотеки Python
- пользовательские исключения

### Иерархия исключений

In [ ]:

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- AssertionError
      +-- AttributeError
      +-- LookupError
           +-- IndexError
           +-- KeyError
      +-- OSError
      +-- SystemError
      +-- TypeError
      +-- ValueError
```

### Обработка исключений

In [ ]:

```python
try:
    1 / 0
except:
    print("Ошибка")
```

### Обработка исключений

In [ ]:

```python
try:
    1 / 0
except Exception:
    print("Ошибка")
```

### Обработка ожидаемого исключения

In [ ]:

```python
while True:
    try:
        raw = input("введите число: ")
        number = int(raw)
        break
    except:
        print("некорректное значение")
```

### Обработка исключения ValueError

In [ ]:

```python
while True:
    try:
        raw = input("введите число: ")
        number = int(raw)
        break
    except ValueError:
        print("некорректное значение")
```

### Блок else

In [ ]:

```python
while True:
    try:
        raw = input("введите число: ")
        number = int(raw)
    except ValueError:
        print("некорректное значение!")
    else:
        break
```

### Обработка нескольких исключений

In [ ]:

```python
while True:
    try:
        raw = input("введите число: ")
        number = int(raw)
        break
    except ValueError:
        print("некорректное значение!")
    except KeyboardInterrupt:
        print("выход")
        break
```

### Обработка нескольких исключений

In [ ]:

```python
total_count = 100_000
while True:
    try:
        raw = input("введите число: ")
        number = int(raw)
        total_count = total_count / number
        break
    except (ValueError, ZeroDivisionError):
        print("некорректное значение!")
```

### Обработка нескольких исключений, наследование

In [ ]:

```python
# +-- LookupError
#      +-- IndexError
#      +-- KeyError

Python 3.6.1
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> issubclass(KeyError, LookupError)
True
>>> issubclass(IndexError, LookupError)
True
>>>
```

### Обработка нескольких исключений, наследование

In [ ]:

```python
database = {
    "red": ["fox", "flower"],
    "green": ["peace", "M", "python"]
}
 
try:
    color = input("введите цвет: ")
    number = input("введите номер по порядку: ")
    
    label = database[color][int(number)]
    print("вы выбрали:", label)
# except (IndexError, KeyError):
except LookupError:
   print("Объект не найден")
```

### Блок finally

In [ ]:

```python
f = open("/etc/hosts")
try:
    for line in f:
        print(line.rstrip("\n"))
        1 / 0
 
    f.close()
except OSError:
    print("ошибка")
```

### Блок finally

In [ ]:

```python
f = open("/etc/hosts")
try:
    for line in f:
        print(line.rstrip("\n"))
        1 / 0
except OSError:
    print("ошибка")
finally:
    f.close()
```

### Исключения, подводим итоги

- генерация исключений
- типы исключений
- обработка исключений

### Исключения в Python (Часть 2)

- доступ к объекту исключения
- генерация исключений, инструкция raise
- исключения типа AssertionError
- вопросы производительности
- работа с собственными исключениями

### Доступ к объекту исключения

In [ ]:

```python
try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)
```

### Доступ к объекту исключения, атрибут args

In [ ]:

```python
# атрибут args
import os.path

filename = "/file/not/found"
try:
    if not os.path.exists(filename):
        raise ValueError("файл не существует", filename)
except ValueError as err:
    message, filename = err.args[0], err.args[1]
    print(message, code)
```

### Доступ к стеку вызовов

In [ ]:

```python
import traceback
 
try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    trace = traceback.print_exc()
    print(trace)
```

### Генерация исключения, инструкция raise

In [ ]:

```python
try:
    raw = input("введите число: ")
    if not raw.isdigit():
        raise ValueError
except ValueError:
    print("некорректное значение!")
```

### Инструкция raise для экземпляра ValueError

In [ ]:

```python
try:
    raw = input("введите число: ")
    if not raw.isdigit():
        raise ValueError("плохое число", raw)
except ValueError as err:
    print("некорректное значение!", err)
```

### Проброс исключения "выше"

In [ ]:

```python
try:
    raw = input("введите число: ")
    if not raw.isdigit():
        raise ValueError("плохое число", raw)
except ValueError as err:
    print("некорректное значение!", err)
    # делегирование обработки исключения
    raise
```

### Исключение через raise from Exception

In [ ]:

```python
try:
    raw = input("введите число: ")
    
    if not raw.isdigit():
        raise ValueError("плохое число", raw)
except ValueError as err:
    print("ошибка:", err.args[0], err.args[1])
    
    raise TypeError("ошибка") from err
```

### Инструкция assert

In [ ]:

```python
Python 3.6.1
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> assert True
>>> assert 1 == 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> 
>>> assert 1 == 0, "1 не равен 0"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: 1 не равен 0
```

### Инструкция assert, флаг -O

In [ ]:

```python
def get_user_by_id(id):
    assert isinstance(id, int), "id должен быть целым числом"
    
    print("выполняем поиск")
 
if __name__ == "__main__":
    get_user_by_id("foo")
```

### Производительность исключений

In [1]:

```python
%%timeit
my_dict = {"foo": 1}
for _ in range(1000):
    try:
        my_dict["bar"]
    except KeyError:
        pass
1000 loops, best of 3: 511 µs per loop
```

In [2]:

```python
%%timeit
my_dict = {"foo": 1}
for _ in range(1000):
    if "bar" in my_dict:
        _ = my_dict["bar"]
10000 loops, best of 3: 78.3 µs per loop
```

### Работа с собственными исключениями, библиотека requests

In [ ]:

```python
response = requests.get("https://github-not-found.com")
```

In [ ]:

```python
try:
    response = requests.get("https://github-not-found.com")
except requests.RequestException as err:
    print(err)

>>> HTTPSConnectionPool(host='github-not-found.com', port=443): 
>>>     Max retries exceeded with url: / 
>>>         (Caused by NewConnectionError(
...    
>>>          Failed to establish a new connection: [Errno -2] 
>>>          Name or service not known',))
        
```

In [ ]:

```python
# requests.__file__
import requests
import time

timeout = 0.2
for _ in range(5): 
    try:
        response = requests.get("https://github.com/not_found",
                                timeout=timeout)
        
        response.raise_for_status()
        break
    except requests.Timeout:
        print("попробуйте позже timeout:", timeout)
        timeout *= 2
        time.sleep(timeout)
    except requests.HTTPError as err:
        print(err.response.status_code)
        raise
```



## Магические методы

In [1]:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }
    
jane = User('Jane Doe', 'janedoe@example.com')

print(jane.get_email_data())
{'name': 'Jane Doe', 'email': 'janedoe@example.com'}
```

In [2]:

```python
class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
    
        return cls.instance
    

a = Singleton()
b = Singleton()

a is b
```

Out[2]:

```python
True
```

### __str__

In [3]:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)


jane = User('Jane Doe', 'janedoe@example.com')

print(jane)
Jane Doe <janedoe@example.com>
```

### __hash__, __eq__

In [4]:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email

    
jane = User('Jane Doe', 'jdoe@example.com')
joe = User('Joe Doe', 'jdoe@example.com')


print(jane == joe)
True
```

In [5]:

```python
print(hash(jane))
print(hash(joe))
7885430882792781082
7885430882792781082
```

In [6]:

```python
user_email_map = {user: user.name for user in [jane, joe]}

print(user_email_map)
{<__main__.User object at 0x107415908>: 'Joe Doe'}
```

### __getattr__, __getattribute__, __setattr__, __delattr__

In [7]:

```python
class Researcher:
    def __getattr__(self, name):
        return 'Nothing found :('
    
    def __getattribute__(self, name):
        return 'nope'
    

obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.DFG2H3J00KLL)
nope
nope
nope
```

In [8]:

```python
class Researcher:
    def __getattr__(self, name):
        return 'Nothing found :()\n'
    
    def __getattribute__(self, name):
        print('Looking for {}'.format(name))
        return object.__getattribute__(self, name)
    

obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.DFG2H3J00KLL)
Looking for attr
Nothing found :()

Looking for method
Nothing found :()

Looking for DFG2H3J00KLL
Nothing found :()
```

In [9]:

```python
class Ignorant:
    def __setattr__(self, name, value):
        print('Not gonna set {}!'.format(name))
        

obj  = Ignorant()
obj.math = True
Not gonna set math!
```

In [10]:

```python
print(obj.math)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-10-677c3efbe80d> in <module>()
----> 1 print(obj.math)

AttributeError: 'Ignorant' object has no attribute 'math'
```

In [11]:

```python
class Polite:    
    def __delattr__(self, name):
        value = getattr(self, name)
        print(f'Goodbye {name}, you were {value}!')

        object.__delattr__(self, name)
        

obj = Polite()

obj.attr = 10
del obj.attr
Goodbye attr, you were 10!
```

### __call__

In [12]:

```python
class Logger:
    def __init__(self, filename):
        self.filename = filename
    
    def __call__(self, func):
        with open(self.filename, 'w') as f:
            f.write('Oh Danny boy...')
        return func
    
logger = Logger('log.txt')

@logger
def completely_useless_function():
    pass
```

In [13]:

```python
completely_useless_function()

with open('log.txt') as f:
    print(f.read())
Oh Danny boy...
```

### __add__

In [14]:

```python
import random


class NoisyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        noise = random.uniform(-1, 1)
        return self.value + obj.value + noise

    
a = NoisyInt(10)
b = NoisyInt(20)
```

In [15]:

```python
for _ in range(3):
    print(a + b)
30.605646527205856
30.170967742734117
29.071231797981817
```

### Написать свой контейнер с помощью __getitem__, __setitem__

In [16]:

```python
class PascalList:
    def __init__(self, original_list=None):
        self.container = original_list or []
        
    def __getitem__(self, index):
        return self.container[index - 1]
    
    def __setitem__(self, index, value):
        self.container[index - 1] = value
        
    def __str__(self):
        return self.container.__str__()
        
        
numbers = PascalList([1, 2, 3, 4, 5])

print(numbers[1])
1
```

In [17]:

```python
numbers[5] = 25

print(numbers)
[1, 2, 3, 4, 25]
```



## Итераторы

In [1]:

```python
for number in range(5):
    print(number & 1)
0
1
0
1
0
```

In [2]:

```python
for letter in 'python':
    print(ord(letter))
112
121
116
104
111
110
```

In [3]:

```python
iterator = iter([1, 2, 3])
```

In [4]:

```python
print(next(iterator))
1
```

In [5]:

```python
print(next(iterator))
2
```

In [6]:

```python
print(next(iterator))
3
```

In [7]:

```python
print(next(iterator))
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-7-369d18de2e56> in <module>()
----> 1 print(next(iterator))

StopIteration: 
```

In [8]:

```python
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result
    
    
for num in SquareIterator(1, 4):
    print(num)
1
4
9
```

In [9]:

```python
class IndexIterable:
    def __init__(self, obj):
        self.obj = obj
        
    def __getitem__(self, index):
        return self.obj[index]


for letter in IndexIterable('str'):
    print(letter)
s
t
r
```



## Контекстные менеджеры

In [1]:

```python
with open('access_log.log', 'a') as f:
    f.write('New Access')
```

In [2]:

```python
class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)
    
    def __enter__(self):
        return self.f
    
    def __exit__(self, *args):
        self.f.close()
```

In [3]:

```python
with open_file('test.log', 'w') as f:
    f.write('Inside `open_file` context manager')
```

In [4]:

```python
with open_file('test.log', 'r') as f:
    print(f.readlines())
['Inside `open_file` context manager']
```

In [5]:

```python
class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type
        
    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exc_type:
            print('Nothing happend.')
            return True
```

In [6]:

```python
with suppress_exception(ZeroDivisionError):
    really_big_number = 1 / 0
Nothing happend.
```

In [7]:

```python
import contextlib


with contextlib.suppress(ValueError):
    raise ValueError
```



```python
import time


class timer():
    def __init__(self):
        self.start = time.time()
        
    def current_time(self):
        return time.time() - self.start
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        print('Elapsed: {}'.format(self.current_time()))
    
    
with timer() as t:
    time.sleep(1)
    print('Current: {}'.format(t.current_time()))
    time.sleep(1)
    
Current: 1.0018980503082275
Elapsed: 2.006608009338379
```



## Дескрипторы

In [1]:

```python
class Descriptor:
    def __get__(self, obj, obj_type):
        print('get')
        
    def __set__(self, obj, value):
        print('set')
        
    def __delete__(self, obj):
        print('delete')


class Class:
    attr = Descriptor()
    

instance = Class()
```

In [2]:

```python
instance.attr
get
```

In [3]:

```python
instance.attr = 10
set
```

In [4]:

```python
del instance.attr
delete
```

In [5]:

```python
class Value:
    def __init__(self):
        self.value = None
    
    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.value = self._prepare_value(value)
```

In [6]:

```python
class Class:
    attr = Value()

    
instance = Class()
instance.attr = 10

print(instance.attr)
100
```

### Функции и методы

In [7]:

```python
class Class:
    def method(self):
        pass
    
    
obj = Class()    

print(obj.method)
print(Class.method)
<bound method Class.method of <__main__.Class object at 0x10ee77278>>
<function Class.method at 0x10ee3bea0>
```

In [8]:

```python
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

amy = User('Amy', 'Jones')

print(amy.full_name)
print(User.full_name)
Amy Jones
<property object at 0x10ee7b598>
```

In [9]:

```python
class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        return self.getter(obj)
```

In [10]:

```python
class Class:
    @property
    def original(self):
        return 'original'
    
    @Property
    def custom_sugar(self):
        return 'custom sugar'
    
    def custom_pure(self):
        return 'custom pure'
    
    custom_pure = Property(custom_pure)
```

In [11]:

```python
obj = Class()

print(obj.original)
print(obj.custom_sugar)
print(obj.custom_pure)
original
custom sugar
custom pure
```

In [12]:

```python
class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        return self.func
```

In [13]:

```python
class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        if obj_type is None:
            obj_type = type(obj)

        def new_func(*args, **kwargs):
            return self.func(obj_type, *args, **kwargs)

        return new_func
```

### __slots__

In [14]:

```python
class Class:
    __slots__ = ['anakin']
    
    def __init__(self):
        self.anakin = 'the chosen one'

        
obj = Class()

obj.luke = 'the chosen too'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-14-66c0c798df1f> in <module>()
      8 obj = Class()
      9 
---> 10 obj.luke = 'the chosen too'

AttributeError: 'Class' object has no attribute 'luke'
```



```python
class ImportantValue:
    def __init__(self, amount):
        self.amount = amount
    
    def __get__(self, obj, obj_type):
        return self.amount
    
    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:
            f.write(str(value))
            
        self.amount = value
    
    
class Account:
    amount = ImportantValue(100)
    
bobs_account = Account()
bobs_account.amount = 200

with open('log.txt', 'r') as f:
    print(f.read())
200
```



## Мета-классы

In [1]:

```python
class Class:
    ...
```

In [2]:

```python
obj = Class()
```

In [3]:

```python
type(obj)
```

Out[3]:

```python
__main__.Class
```

In [4]:

```python
type(Class)
```

Out[4]:

```python
type
```

In [5]:

```python
type(type)
```

Out[5]:

```python
type
```

In [6]:

```python
issubclass(Class, type)
```

Out[6]:

```python
False
```

In [7]:

```python
issubclass(Class, object)
```

Out[7]:

```python
True
```

In [8]:

```python
def dummy_factory():
    class Class:
        pass
    
    return Class


Dummy = dummy_factory()

print(Dummy() is Dummy())
False
```

In [9]:

```python
NewClass = type('NewClass', (), {})

print(NewClass)
print(NewClass())
<class '__main__.NewClass'>
<__main__.NewClass object at 0x110cd7438>
```

In [10]:

```python
class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass
Creating A
```

In [11]:

```python
print('A.class_id: "{}"'.format(A.class_id))
A.class_id: "a"
```

In [12]:

```python
class Meta(type):
    def __init__(cls, name, bases, attrs):
        print('Initializing — {}'.format(name))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls
            
        super().__init__(name, bases, attrs)
        
        
class Base(metaclass=Meta): pass

class A(Base): pass

class B(Base): pass
Initializing — Base
Initializing — A
Initializing — B
```

In [13]:

```python
print(Base.registry)
print(Base.__subclasses__())
{'a': <class '__main__.A'>, 'b': <class '__main__.B'>}
[<class '__main__.A'>, <class '__main__.B'>]
```

### Абстрактные методы

In [14]:

```python
from abc import ABCMeta, abstractmethod

class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do something"""
```

In [15]:

```python
class Child(Sender): pass

Child()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-5e10f1ccf1fd> in <module>()
      1 class Child(Sender): pass
      2 
----> 3 Child()

TypeError: Can't instantiate abstract class Child with abstract methods send
```

In [16]:

```python
class Child(Sender):
    def send(self):
        print('Sending')
        

Child()
```

Out[16]:

```python
<__main__.Child at 0x110cfa860>
```

In [17]:

```python
class PythonWay:

    def send(self):
        raise NotImplementedError
```



## Отладка

```python
import re
import requests

def main(site_url, substring):    
    site_code = get_site_code(site_url)
    matching_substrings = get_matching_substrings(site_code, substring)
    print('"{}" found {} times in {}'.format(
        substring, len(matching_substrings), site_url
    ))
    
def get_site_code(site_url):
    if not site_url.startswith('http'):
        site_url = 'http://' + site_url

    return requests.get(site_url).text

def get_matching_substrings(source, substring):
    return re.findall(substring, source)


main('mail.ru', 'script')
"script" found 272 times in mail.ru
```



## Тестирование

In [1]:

```python
# test_python.py

import unittest


class TestPython(unittest.TestCase):
    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))
        
    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))

    def test_trueness(self):
        self.assertTrue(bool(10))
```

project/tests $> python3 -m unittest test_python.py

In [2]:

```python
# test_division.py

import unittest


class TestDivision(unittest.TestCase):
    def test_integer_division(self):
        self.assertIs(10 / 5, 2)
```

```bash
project/tests $> python3 -m unittest test_division.py
```

In [7]:

```python
import requests


class Asteroid:
    BASE_API_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key=DEMO_KEY'

    def __init__(self, spk_id):
        self.api_url = self.BASE_API_URL.format(spk_id)

    def get_data(self):
        return requests.get(self.api_url).json()

    @property
    def name(self):
        return self.get_data()['name']

    @property
    def diameter(self):
        return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])
    
    @property
    def closest_approach(self):
        closest = {
            'date': None,
            'distance': float('inf')
        }
        for approach in self.get_data()['close_approach_data']:
            distance = float(approach['miss_distance']['lunar'])
            if distance < closest['distance']:
                closest.update({
                    'date': approach['close_approach_date'],
                    'distance': distance
                })
        return closest
```

In [9]:

```python
apophis = Asteroid(2099942)

print(f'Name: {apophis.name}')
print(f'Diameter: {apophis.diameter}m')
Name: 99942 Apophis (2004 MN4)
Diameter: 682m
```

In [ ]:

```python
import json
import unittest
from unittest.mock import patch

from asteroid import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid(2099942)

    def mocked_get_data(self):
        with open('apophis_fixture.txt') as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(
            self.asteroid.name, '99942 Apophis (2004 MN4)'
        )

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)
```

In [10]:

```python
print(f'Date: {apophis.closest_approach["date"]}')
print(f'Distance: {apophis.closest_approach["distance"]:.2} LD')
Date: 2029-04-13
Distance: 0.099 LD
```