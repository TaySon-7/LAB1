def tokenize_fsm(expr: str) -> list[tuple[str, str]]:
    """
    :param expr: арифметичсекое выражение в виде строки, вводимое пользователем
    :return: Возвращает список разбиения операций и опернадов с токенами (скобки идут без токена)
    """
    if not expr.strip(): # Проверка на пустой ввод
        raise Exception("Пустой ввод")
    expr = expr.replace(',', '.') #  Предполагаем возможный ввод запятых
    tokens = []
    num = '' # Переменная для промежуточного хранения собираемого числа
    oper = '' # Переменная для хранения собираемой операции для '//' и '**' (можно просто было использовать replace)
    for char in expr: # Проходим по всем символам арифметичсекой строки
        if char not in '0123456789() ~.+-*/%': # Проверяем на наличие неккоректных символов
            raise ValueError("Присутствует некорректный символ")
        if oper: # Это выполняется, если до этого встретилось '//' или '**'
            if char == oper:
                tokens.append(('OPERATOR',char * 2)) # Если прошлый операнд совпадает с текущим, то добавим операцию из двух знаков
                oper = ''
                continue
            elif char == ' ' or char in '()': # Если нет, то один символ операции добавим
                tokens.append(('OPERATOR', oper))
                oper = ''
                if char == '(': # Здесь нужно проверить текущий ли символ скобка, так как далее 'continue'
                    tokens.append(('(', '('))
                if char == ')':
                    tokens.append((')', ')'))
                continue
        if char in '~.' or char.isdigit(): # Если текущий символ число или унарный минус, точка, то собираем число
            num += char
            continue
        if num == '.': # Проверка одиночной точки
            raise ValueError("Одиночная точка - это не операнд и не операция")
        if ('~' in num or ' ' in num) and num[-1] not in '.0123456789': # Позволяет писать унарный минус с пробелами
            continue
        if num:
            num = num.replace('~', '-')
            tokens.append(('NUMBER', num))
            num = ''
        if char == '(': # Добавляем скобки в токены
            tokens.append(('(', '('))
        if char == ')':
            tokens.append((')', ')'))
        if char in '+-%': # Добавляем операции в токены
            tokens.append(('OPERATOR',char))
        elif char in '/*': # Начинаем собирать двойную операцию
            oper = char
            continue
    # Завершающие проверки
    if num == '.':
        raise ValueError("Одиночная точка - это не операнд и не операция")
    if num:
        num = num.replace('~', '-')
        tokens.append(('NUMBER', num))
    elif oper:
        tokens.append(('OPERATOR', oper))
    if tokens[0][0] == 'OPERATOR': # Проверка на наличие операции в начале
        raise Exception("В ОПН нельзя использовать бинарный оператор в начале выражения. Помните, что унарный минус это '~'.")
    return tokens
