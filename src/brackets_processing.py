from src.calculator import calculator


def brackets_summator(tokens_with_brackets: list) -> list:
    """
    Функция последовательно вычисляет значения арифметичсеких выражений ОПН по скобкам
    :param tokens_with_brackets: список скобок, операндов и операций с токенами
    :return: Возвращает список опернадов и операций с токенами, включая предварительно посчитанными значения в скобках (выражение ОПН без скобок)
    """
    while (')', ')') in tokens_with_brackets or ('(', '(') in tokens_with_brackets: # Пока есть скобки в выражении
        stack = [] # Создаем стек для хранения информации о встреченных скобках
        flag = False # Флаг для отслежевания изменений токенов выражения с каждой итерацией while
        for i in range(len(tokens_with_brackets)): # Проходим по токенам
            if tokens_with_brackets[i][0] == '(':
                stack.append((tokens_with_brackets[i][0], i)) # Записываем местоположение открывающих скобок в стек
            elif tokens_with_brackets[i][0] == ')':
                if not stack: # Если закрывающая не встречает своей открывающей, то ошибка
                    raise ArithmeticError("Скобки расставлены неправильно")
                print(tokens_with_brackets[stack[-1][1]:i + 1])
                res_brackets = calculator(tokens_with_brackets[stack[-1][1]:i + 1]) # Подсчитываем выражение в скобках
                print(res_brackets)
                # Заменяем выражение в скобках на результат её вычисления
                tokens_with_brackets = tokens_with_brackets[:stack[-1][1]] + [('NUMBER', res_brackets)] + tokens_with_brackets[i + 1:]
                flag = True # Поднимаем флаг, т.к. посчитали одно выражение в скобках
                stack.pop()  # Снимаем соответствующую открывающую скобку
                print(len(tokens_with_brackets), tokens_with_brackets)
                break # Выходим из цикла for, т.к. наш список токенов изменил размерность
        if not flag: # Если скобки были, но ничего не поменялось, значит, это ошибка в их расстановке
            raise ArithmeticError("Скобки расставлены неправильно")
    return tokens_with_brackets
