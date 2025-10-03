from src.tokenization import tokenize_fsm
from src.calculator import calculator
from src.brackets_processing import brackets_summator


def main() -> None:
    """
    Запускает ввод арифметичсекого выражения в ОПН для пользователя, которое он хочет вычислить
    :return: Данная функция ничего не возвращает
    """

    expr = input("Введите арифметичсекое выражение в ОПН: ")
    tokens_with_brackets = tokenize_fsm(expr=expr)
    tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
    result = calculator(tokens=tokens_after_brackets)
    print(result)


if __name__ == "__main__":
    main()
