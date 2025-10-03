from src.tokenization import tokenize_fsm
from src.calculator import calculator
from src.brackets_processing import brackets_summator
import pytest


def test_main_1():
    expr = '(3 4 + ) ( 5 2 - ) *'
    tokens_with_brackets = tokenize_fsm(expr=expr)
    tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
    result = calculator(tokens=tokens_after_brackets)
    assert result == 21


def test_main_2():
    expr = '( 8 ( 3 2 + ) - ) 4 *'
    tokens_with_brackets = tokenize_fsm(expr=expr)
    tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
    result = calculator(tokens=tokens_after_brackets)
    assert result == 12


def test_main_3():
    expr = '( 3 ( 4 5 + ) - ) 2 ( 3 4 + ) * *'
    tokens_with_brackets = tokenize_fsm(expr=expr)
    tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
    result = calculator(tokens=tokens_after_brackets)
    assert result == -84


def test_main_4():
    expr = '( ( 52 3 * ) 3 -) ( 267 5 * ) +'
    tokens_with_brackets = tokenize_fsm(expr=expr)
    tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
    result = calculator(tokens=tokens_after_brackets)
    assert result == 1488


def test_main_errors_1():
    with pytest.raises(ArithmeticError, match='Переизбыток операций'):
        expr = '( 8 ( 3 2 + - ) ) 4 *'
        tokens_with_brackets = tokenize_fsm(expr=expr)
        tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
        calculator(tokens=tokens_after_brackets)


def test_main_errors_2():
    with pytest.raises(Exception):
        expr = '( 8 ( 3 2 + - ) ) 4 *'
        tokens_with_brackets = tokenize_fsm(expr=expr)
        tokens_after_brackets = brackets_summator(tokens_with_brackets=tokens_with_brackets)
        calculator(tokens=tokens_after_brackets)
