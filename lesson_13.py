# import codecs
# import re
#
# ДЗ 13.1 Очистити текст від html-тегів

# import codecs


# def delete_html_tags(html_file, result_file="cleaned.txt"):
#     with codecs.open(html_file, "r", "utf-8") as file:
#         html = file.read()
#         new = ""
#         flag = True
#         for i in html:
#             if i == "<":
#                 flag = False
#             elif i == ">":
#                 flag = True
#                 continue
#             if flag:
#                 new += i
#         print(new)
#     with codecs.open(result_file, mode="w", encoding="utf-8") as g:
#         g.write(new)


# delete_html_tags("draft.html")

#ДЗ 13.2 Корзина для покупок

# class Item:

#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name

#     def __str__(self):
#         return f"Item:\n Name: {self.name},\n Price: {self.price},\n Describe: {self.description}"


# class User:

#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone

#     def __str__(self):
#         return f"User name: {self.name},\n User surname: {self.surname},\n User phone: {self.numberphone}"


# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0

#     def add_item(self, item, cnt):
#         self.products[item] = cnt

#     def __str__(self):
#         result = f"User name :{self.user.name},\n User surname: {self.user.surname}\n"
#         result += "Items: \n"
#         for key, val in self.products.items():
#             result += f"{key.name}: {val}pcs.\n"
#         return result

#     def get_total(self):
#         total = 0
#         for key, val in self.products.items():
#             total += val * key.price
#         return total


# lemon = Item(
#     "lemon",
#     5,
#     "yellow",
#     "small",
# )
# apple = Item(
#     "apple",
#     2,
#     "red",
#     "middle",
# )
# print(lemon)  # lemon, price: 5

# buyer = User("Ivan", "Ursatii", "02628162")
# print(buyer)  # Ivan Ursatii

# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# """
# User: Ivan Ursatii
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, "Екземпляр класу User"
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, "Повинно залишатися 60!"
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ursatii
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """

# assert cart.get_total() == 40

# ДЗ 14.1. Група студентів

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human: Gender: {self.gender}, age - {self.age} name: {self.first_name} last name: {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record_book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.discard(student)

    def find_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return i
        return None

    def __str__(self):
        all_students = ""
        for www in self.group:
            all_students += str(www) + "\n"
        return f"Number:{self.number}\n {all_students} "


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод пошуку повинен повертати екземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!





##############################
# Обробка винятків

# v1
# n1, n2 = 10, 0 # множинне привласнення
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

# v2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
#
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:  # Exception -> базовий тип виключення пишемо останнім з except
#     print(f"Exception occurred: {error}")
# finally:  # Відпрацьовує завжди. Писати по потребі
#     print("End of calculation")
#
# print("some text")

# MAX_USERNAME_LEN = 20
# MIN_USERNAME_LEN = 1


####
# def hello_user(username):
#     username_length = len(username)
#
#     if username_length > MAX_USERNAME_LEN:
#         raise Exception(f"Incorrect name length provided ({username_length})\n"
#                         f"Should be less than {MAX_USERNAME_LEN}\n"
#                         "Please enter a valid name!")
#     elif username_length <= MIN_USERNAME_LEN:
#         raise Exception(f"Incorrect name length provided ({username_length})\n"
#                         f"Should be more than {MIN_USERNAME_LEN}\n"
#                         "Please enter a valid name!")
#
#     print(f"Hello, {username}")
#
#
# while True:
#     try:
#         name = input("Enter you name: ")
#         hello_user(name)
#         should_continue = input("Do you want to continue? (y/n): ")
#         if should_continue.lower() == "n":
#             break
#     except Exception as e:
#         print(f"Error: {e}")


# v2
# try:
#     name = input("Enter you name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")  # raise -> згенерувати виняток (кинути виняток)
# except Exception as e:
#     print(f"Error: {e}")


# У Python є такі базові типи винятків:
#
# BaseException: базовий тип для всіх вбудованих винятків
#
# Exception: базовий тип, який зазвичай застосовується для створення своїх типів винятків
#
# ArithmeticError: базовий тип для винятків, пов'язаних з арифметичними операціями
# (OverflowError, ZeroDivisionError, FloatingPointError).
#
# BufferError: Виняток, який виникає при неможливості виконати операцію з буфером
#
# LookupError: базовий тип для винятків, які виникають під час звернення до колекцій
# за некоректним ключем або індексом (наприклад, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: виняток виникає, якщо індекс при зверненні до елемента колекції знаходиться поза допустимим діапазоном
#
# KeyError: виникає, якщо у словнику немає ключа, за яким відбувається звернення до елемента словника.
#
# OverflowError: виникає, якщо результат арифметичної операції не може бути представлений поточним
# Чисельним типом (зазвичай типом float).
#
# RecursionError: виникає, якщо перевищено допустиму глибину рекурсії.
#
# TypeError: якщо операція або функція застосовується до значення неприпустимого типу.
# result = float(object())
# print(result)
# ValueError: виникає, якщо операція або функція одержують об'єкт коректного типу з некоректним значенням.
#
# ZeroDivisionError: виникає при розподілі на нуль.
#
# NotImplementedError: тип виключення для вказівки, що якісь методи класу не реалізовані
#
# ModuleNotFoundError: виникає при неможливості знайти модуль при його імпорті директивою import
#
# OSError: тип винятків, які генеруються при виникненні помилок системи (наприклад, неможливо знайти файл,
# пам'ять диска заповнена і т.д.)

# from datetime import datetime
#
#
# #####
# class InvalidNameException(Exception):
#
#     def __init__(self, *args):
#         # print(self.args)
#         self.log_error_data()
#
#     def log_error_data(self):
#         with open("log.txt", "a") as file:
#             error_message = f"{str(datetime.today())}: " + f"\n".join(self.args) + "\n"
#             file.write(error_message)
#
#
# try:
#     name = input("Enter you name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise InvalidNameException(f"Please enter a valid name! You entered: {name}")
# # raise -> згенерувати виняток (кинути виняток)
# except Exception as e:
#     print(f"Error: {e}")

####################
# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.

# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації

######################
# успадкування
# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     pass
#
#     # self -> используется, чтоб указать что поле/метод относится к экземпляру класса
#     def __init__(self, name, age):
#         self.name = name  # self.name -> поле класса (переменная класса)
#         self.age = age
#
#     def show_info(self):  # show_info -> метод класса (функция класса)
#         print(f"Name: {self.name}, Age: {self.age}")


# # v1
# class Employee(Person):  # успадковуємося від класу Person
#     def work(self):
#         print(f"{self.name} works!")
#
#
# class Company:
#     def __init__(self, employees: list[Employee]):
#         self.employees = employees
#
#
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()


# # v2
# class Employee(Person):
#     def __init__(self, name, age, company):
#         # v1
#         super().__init__(name, age)  # виклик конструктора базового класу Person
#         # super() -> посилання на базовий клас, отримуємо доступ до елементів базового класу
#         # v2
#         # Person.__init__(self, name, age)
#         self.company = company
#
#     # перевизначення методу
#     def show_info(self):
#         super().show_info()  # виклик методу базового класу
#         print(f"Works in {self.company} company")  # розширили своєю логікою
#
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()

# Створити ієрархію класів для опису академії.
#
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):  # show_info -> метод класса (функция класса)
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# class Subject(object):
#     def __init__(self, name):
#         self.name = name
#
#
# class MathTopicSubject(Subject):
#     def __init__(self, name, test):
#         super().__init__(name)
#         self.test = test
#
#
# class Teacher(Person):
#     def __init__(self, name, age, subjects: list[Subject], experience: int):
#         super().__init__(name, age)
#         self.subjects = subjects
#         self.experience = experience
#
#
# class Student(Person):
#     def __init__(self, name, age, subject: Subject):
#         super().__init__(name, age)
#         self.subject = subject
#
#
# class Academy(object):
#     def __init__(self, name, subjects: list[Subject], teachers: list[Teacher], students: list[Student]):
#         self.name = name
#         self.subjects: list[Subject] = subjects
#         self.teachers: list[Teacher] = teachers
#         self.students: list[Student] = students
#
#
# current_subjects = [Subject("math"), Subject("english"), Subject("history")]
# current_teachers = [Teacher("Vasya", 33, current_subjects, 20),
#                     Teacher("Petya", 33, current_subjects, 10)]
# current_student = [Student("Vasya", 22, current_subjects[0]), Student("Alex", 44, current_subjects[2])]
# acad = Academy("Super academy", current_subjects, current_teachers, current_student)
#
# for teacher in acad.teachers:
#     teacher.show_info()

#####################
# v3
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def show_info(self):
#         print(f"Name: {self.name}")
#
#
# class Employee(Person):
#     def __init__(self, name, workplace=None):
#         super().__init__(name)
#         self.workplace = workplace
#
#     def work(self):
#         print(f"{self.name} works!")
#
#     def show_information(self):
#         print(f"Info from {Employee} with name {self.name}")
#
#
# class Student(Person):
#     def __init__(self, name, university=None):
#         super().__init__(name)
#         self.university = university
#
#     def study(self):
#         print(f"{self.name} studies!")
#
#     def show_information(self):
#         print(f"Info from {Student} with name {self.name}")
#
#
# class WorkingStudent(Student, Employee):  # множинне спадкування
#     def __init__(self, name, workplace, university):
#         Student.__init__(self, name, university)
#         Employee.__init__(self, name, workplace)
#
#     def show_information(self):
#         Student.show_information(self)
#         Employee.show_information(self)
#         Person.show_info(self)
#
#
# vasya = WorkingStudent("Vasya", "Google", "California")
# vasya.work()
# vasya.study()
# vasya.show_information()
# print(WorkingStudent.mro())

# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]

# class ParserBase:
#     def map_data(self):
#         pass
#
#     def parse_nested_json_string(self):
#         pass
#
#
# class SoapParser(ParserBase):
#     def convert_xml_to_json(self):
#         pass
#
#
# class RestParser(ParserBase):
#     def sanitize_json(self):
#         pass
