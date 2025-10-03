

from src.operations import addition, subtraction, multiplication,\
    division_int, division_float, remainder, power


def calculator(tokens: list) -> float:
    """
    Функция вычисляет выражение в обратной польской записи без скобок
    :param tokens: список операндов и операций с токенами
    :return: значение выражения в ОПЗ
    """
    cstack = [] # Создаём стек для формирвоания очереди операций с числами
    res = 0 # Переменная для промежуточных вычислений (можно без неё)
    for val in tokens: # Проходим по токенам
        if val[0] == "NUMBER":
            cstack.append(val[1]) # встретили число, добавляем в конец стека
        if val[0] == 'OPERATOR':
            if  len(cstack) >= 2: # Операция применима, если есть как минимум два числа в стеке
                first_op = float(cstack[-2])
                second_op = float(cstack[-1])
                cstack.pop()
                cstack.pop() # Убираем числа из стека, т.к. мы их посчитаем
                if val[1] == '+':
                    res = addition(first_op, second_op)
                if val[1] == '-':
                    res = subtraction(first_op, second_op)
                if val[1] == '*':
                    res = multiplication(first_op, second_op)
                if val[1] == '//':
                    res = division_int(first_op, second_op)
                if val[1] == '/':
                    res = division_float(first_op, second_op)
                if val[1] == '%':
                    res = remainder(first_op, second_op)
                if val[1] == '**':
                    res = power(first_op, second_op)
                cstack.append(res)
            else:
                raise ArithmeticError("Переизбыток операций, возможно в скобках")
    if len(cstack) > 1: # Остались числа, непоучавствующие в операциях:
        raise ArithmeticError("Переизбыток операндов, возможно в скобках")
    if len(cstack) < 1: # Остались неприменённые операции
        raise KeyboardInterrupt("Нет операндов и операций, возможно в скобках")
    if cstack[-1] == int(cstack[-1]): # Проверка на целое число
        return int(cstack[-1])
    else:
        return cstack[-1]
