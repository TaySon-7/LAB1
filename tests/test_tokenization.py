from src.tokenization import tokenize_fsm
import pytest


def test_tokenization_invalid_symbol():
    with pytest.raises(ValueError, match='Присутствует некорректный символ'):
        tokenize_fsm('5 3 #')


def test_tokenization_space_input():
    with pytest.raises(Exception, match='Пустой ввод'):
        tokenize_fsm('')


def test_tokenization_dot_without_float():
    with pytest.raises(ValueError, match='Одиночная точка - это не операнд и не операция'):
        tokenize_fsm('5 3 + 5 . -')


def test_tokenization_two_operands_in_start():
    with pytest.raises(Exception, match="В ОПН нельзя использовать бинарный оператор в начале выражения. Помните, что унарный минус это '~'."):
        tokenize_fsm('-5 5 +')


def test_tokenization_right_tokens_1():
    assert tokenize_fsm('(~  5 9 *) 10 %') == [('(', '('), ('NUMBER', '-5'), ('NUMBER', '9'),
                                               ('OPERATOR', '*'), (')', ')'),('NUMBER', '10'), ('OPERATOR', '%')]


def test_tokenization_right_tokens_2():
    assert tokenize_fsm('( 3 ( 4 5 + ) - ) 2 ( 3 4 + ) ***') == [('(', '('), ('NUMBER', '3'), ('(', '('), ('NUMBER', '4'), ('NUMBER', '5'), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '-'), (')', ')'), ('NUMBER', '2'), ('(', '('), ('NUMBER', '3'), ('NUMBER', '4'), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '**'), ('OPERATOR', '*')]
