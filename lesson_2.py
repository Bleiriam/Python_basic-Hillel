# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних: True False
# str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативної пам'яті значення можна змінювати
# number: int = 10 + 1
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

# let num = 10;
# num = 30;

# my_site.com?param1=123&param2=qwerty

#Task1 Квадрат числа
print("Task 1: Квадрат числа")
NUMBER = int(input("Введіть число: ")) 
print(NUMBER**2)

# pep

#Task2 Середнє трьох чисел
print("Task 2: Середнє тьох чисел")
first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))
third_number = int(input("Введіть третє число: "))
result = (first_number + second_number + third_number) / 3
print(result)
# #
# # ###
# userName1 = "Vasya"
# print(userName1)
# user_name = "Petya"
# print(user_name)

####
# number1 = 10
# print(number1)
# print(number := 10 + number1)  # моржовый оператор
# print(number)

# num2 = 3
# result = 2 + (num1 := 4) + num2
# print(result)
# print(num1)

######
# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3)  # основа ** показник (зведення в ступінь)
# print(2 // 3)  # ціла частина від розподілу
# print(2 % 3)  # залишок від ділення

#Task3 Перетворення хвилин у години
print("Task 3: Перетворення хвилин у години")
num1 = int(input("Введіть кількість хвилин: "))
print(f"{num1 // 60} години {num1 % 60} хвилин")
#
# print(-2)

############
# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %

# 274 => 2 + 7 + 4

#Task5 Остання цифра числа
print("Task 5: Остання цифра числа")
number = int(input("Введіть число: "))
n3 = number % 10 
print(f"Остання цифра: {n3}")
#
# print(n1)
# print(n2)
# print(n2_v2)
# print(n3)
# #
# # # v1
# print(n1, n2, n3, sep=" - ")
# # # # v2
# print(f"{n1}-{n2}-{n3}")
# phone = "123456"
# phone = f"+{phone}"
# #
# result = n1 + n2 + n3
# print("Result:", result)

###
# input -> буде очікувати на введення даних з клавіатури в
# консолі і поверне за замовчуванням значення типу даних str

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# result = first_number + second_number
# print(result)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # v1
# print("Hello,", name, "You are", age, "years old!")
# # v2 конкатенація - складання рядків. Рядок + рядок -> один великий рядок
# print("Hello, " + name + " You are " + str(age) + " years old!")
# # v3 інтерполяція рядка - вбудовування змінних у рядок завдяки функції format (вивчимо докладніше пізніше)
# print(f"Hello, {name}. You are {age} years old! {(test := 12)}")
# print(test)
#
# age_after_ten_years = age + 10
# print(age_after_ten_years)

######
# number = 10
# # v1
# number = number + 1
# print(number)
# # v2
# number += 1
# print(number)
#
# number -= 1  # number = number - 1
# number *= 1  # number = number * 1
# number /= 1  # number = number / 1
# number **= 1  # number = number ** 1
# number //= 1  # number = number // 1
# number %= 1  # number = number % 1

#Task7 Виведення числа в стовпчик
print("Task 7: Виведення числа в стовпчик")
number = int(input('Введіть число: ')) 

n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10

result = n1 * 1000 + n2 * 100 + n3 * 10 + n4 * 1
print(n1)
print(n2)
print(n3)
print(n4)

###
# result = divmod(9, 5)  # // and %
# print(result)
# print(type(result))
#
# first_part, second_part = divmod(9, 5)
# print(first_part)
# print(second_part)

####
# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.

#Task4 Розрахунок знижки
print("Task 4: Розрахунок знижки")
number1 = int(input("Введіть ціну: "))
number2 = int(input("Введіть знижку (%): "))
number3 = number1 - number1 * number2 / 100
print(f"Ціна зі знижкою: {number3}")
#
# numbers_sum = number1 + number2 + number3
# numbers_multiplication = number1 * number2 * number3
# print(f"The sum of the numbers: {numbers_sum}")
# print(f"The multiplication of the numbers: {numbers_multiplication}")

###
#  Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.

#Task6 Периметр прямокутника
print("Task 6: Пермиетр прямокутника")
first_diagonal = int(input("Введіть довжину: "))
second_diagonal = int(input("Введіть ширину: "))
# area = first_diagonal * second_diagonal / 2
print(f"Периметр: {2 * (first_diagonal + second_diagonal)}")

# merge vs rebase
# https://www.youtube.com/watch?v=d5rvy5XPyzk

# Git

# https://git-scm.com/downloads

# Windows: http://gitextensions.github.io/

# Windows/Mac: https://www.sourcetreeapp.com/ чи https://desktop.github.com/ чи https://www.gitkraken.com/jc

# Туторіали:

# https://www.w3schools.com/git/

# https://www.atlassian.com/git/tutorials

# https://githowto.com/setup

# https://www.tutorialspoint.com/git/index.htm

# https://opensource.com/article/18/1/step-step-guide-git

# https://github.com/git-guides/install-git

# https://www.atlassian.com/git/tutorials/install-git

# leetcode
# codewars
