# Функции всех поддерживаемых операций


def addition(x1, x2):
    return x1 + x2


def subtraction(x1, x2):
    return x1 - x2


def multiplication(x1, x2):
    return x1 * x2


def division_int(x1, x2):
    if int(x1) == x1 and int(x2) == x2: # Проверка, что два числа - целые
        return x1 // x2
    if x2 == 0: # Проверка деления на zero
        raise ZeroDivisionError
    raise ArithmeticError("целочисленное деление только для целых")


def division_float(x1, x2):
    if x2 == 0:
        raise ZeroDivisionError # Проверка деления на zero
    return x1 / x2


def remainder(x1, x2):
    if int(x1) == x1 and int(x2) == x2: # Проверка, что два числа - целые
        return x1 % x2
    if x2 == 0:
        raise ZeroDivisionError
    raise ArithmeticError("деление по модулю только для целых")


def power(x1, x2):
    return x1 ** x2
