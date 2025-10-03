from src.brackets_processing import brackets_summator
import pytest


def test_brackets_error_1(): # Открвыающая не находит открывающую
    with pytest.raises(ArithmeticError, match='Скобки расставлены неправильно'):
        brackets_summator([('(', '('), ('NUMBER', 5.0), ('NUMBER', 3.0), ('OPERATOR', '+'), ('NUMBER', 4.0), ('OPERATOR', '-')])


def test_brackets_error_2(): # Закрывающая скобка в начале не пропадает
    with pytest.raises(ArithmeticError, match='Скобки расставлены неправильно'):
        brackets_summator([(')', ')'), ('NUMBER', 8.0), ('(', '('), ('NUMBER', 3.0), ('NUMBER', 2.0), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '-'), (')', ')'), ('NUMBER', 4.0), ('OPERATOR', '*')])


def test_brackets_operations_error(): # В скобках неверное выражение в ОПН с переизбытокм операций
    with pytest.raises(ArithmeticError, match='Переизбыток операций, возможно в скобках'):
        brackets_summator([('NUMBER', 5.0), ('(', '('), ('NUMBER', 10.0), ('OPERATOR', '+'), ('NUMBER', 3.0), ('OPERATOR', '%'), ('NUMBER', 5.0), (')', ')'), ('OPERATOR', '+')])


def test_brackets_operands_error():# В скобках неверное выражение в ОПН с переизбытокм операндов
    with pytest.raises(ArithmeticError, match='Переизбыток операндов, возможно в скобках'):
        brackets_summator([('(', '('), ('NUMBER', 5.0), ('NUMBER', 5.0), ('NUMBER', 5.0), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '+')])


def test_space_in_brackets():
    with pytest.raises(KeyboardInterrupt, match='Нет операндов и операций, возможно в скобках'):
        brackets_summator([('(', '('), ('NUMBER', 3.0), ('(', '('), (')', ')'), ('OPERATOR', '-'), (')', ')'), ('NUMBER', 2.0), ('(', '('), ('NUMBER', 3.0), ('NUMBER', 4.0), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '*'), ('OPERATOR', '*')])


def test_brackets_result_1():
    assert brackets_summator([('(', '('), ('(', '('), ('NUMBER', 52.0), ('NUMBER', 3.0), ('OPERATOR', '*'), (')', ')'), ('NUMBER', 3.0), ('OPERATOR', '-'), (')', ')'), ('(', '('), ('NUMBER', 267.0), ('NUMBER', 5.0), ('OPERATOR', '*'), (')', ')'), ('OPERATOR', '+')]) == [('NUMBER', 153), ('NUMBER', 1335), ('OPERATOR', '+')]


def test_brackets_result_2():
    assert brackets_summator([('(', '('), ('NUMBER', 3.0), ('(', '('), ('NUMBER', 4.0), ('NUMBER', 5.0), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '-'), (')', ')'), ('NUMBER', 2.0), ('(', '('), ('NUMBER', 3.0), ('NUMBER', 4.0), ('OPERATOR', '+'), (')', ')'), ('OPERATOR', '*'), ('OPERATOR', '*')]) == [('NUMBER', -6), ('NUMBER', 2.0), ('NUMBER', 7), ('OPERATOR', '*'), ('OPERATOR', '*')]
