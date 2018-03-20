# -*- coding: utf-8 -*-

import re
import os


roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

pattern = r'^(M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})|[IDCXMLV])$'

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def check_roman(numeral):
    """
    Проверка являются ли все символы Римскими цифрами.
    При несовпадении хотя бы 1го - вернуть False, выйти из цикла
    """
    valid = True
    for letters in numeral:
        if letters not in roman_number:
            valid = False
            break
    return valid


def validate_roman(roman):
    """
    Проверка с помощью регулярного выражения на правильность следования цифр.
    Запрет повторов при следовании символов подряд для ['I' > 3, 'X' > 3, 'C' > 3, 'M' > 4],
    для остальных - повторы запрещены(не более 1го символа подряд).
    Допустимый порядок следования: MCM - корректно, CMM - нет и т.д.
    """
    if re.search(pattern, roman):
        return True


def convert_to_arabic(roman):
    """
    Вычисляем полученное на входе число.
    С помощью генератора списка values получаем список значений по ключам roman_number[r]
    Получаем сумму полученных эл-в списка. Если зн-е следующего по индексу эл-та больше
    предыдущего - предыдущий передается со знаком "-" -> I, X  = -1 + 10= 9
    """
    values = [roman_number[r] for r in roman]
    return sum(
        val if val >= next_val else -val
        for val, next_val in zip(values[:-1], values[1:])
        ) + values[-1]


def convert_to_roman(num):
    """
    Вычисляем Римское число. Заполняем строку путем вычитания тысяч, сотен, десятков, единиц поочередно.
    """
    roman = ''
    num = int(num)
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman


def greeting():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Данная программа выполняет конвертацию только целых положительных чисел из арабских в римские и наоборот')


def main():
    greeting()
    text = ''

    # Пока пользователь не ввел 'q'
    while text != 'Q':
        # Приводим к верхнему регистру, на строковые значения цифр не окажет воздействия
        text = input().upper()

        if text == '0':
            print('Википедия говорит, что римляне с нуля не считали')
        # Выполняем проверку Римское ли число,
        # если да - делаем валидацию на правильность синтаксиса(поочередность символов)
        elif check_roman(text):
            # Выполняем валидацию числа
            if validate_roman(text) is True:
                print(str(convert_to_arabic(text)))
            else:
                print("Некорректное число")

        # Проводим проверку Арабское ли число
        elif str.isdigit(text):
            print(convert_to_roman(text))
        # Если оба условия не выполнены, возвращаем сообщение
        else:
            print('Не является ни римским ни положительным арабским числом. Попробуйте ввести другое значение')


if __name__ == '__main__':
    main()
