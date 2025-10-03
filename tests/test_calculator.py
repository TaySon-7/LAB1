from src.calculator import calculator
import pytest


def test_division_by_zero_error_1(): # Проверка для '//'
    with pytest.raises(ZeroDivisionError):
        calculator([('NUMBER', 3.0), ('NUMBER', 4.0), ('OPERATOR', '-'), ('NUMBER', 0.0), ('OPERATOR', '//')])


def test_division_by_zero_error_2(): # Проверка для '/'
    with pytest.raises(ZeroDivisionError):
        calculator([('(', '('), ('NUMBER', 0.0), ('NUMBER', 4.0), ('NUMBER', 4.0), (')', ')'), ('OPERATOR', '-'), ('OPERATOR', '/')])


def test_division_by_zero_error_3(): # Проверка для '%'
    with pytest.raises(ZeroDivisionError):
        calculator([('(', '('), ('NUMBER', 20.0), ('NUMBER', 5.0), ('NUMBER', 5.0), (')', ')'), ('OPERATOR', '%'), ('OPERATOR', '%')])


def test_int_division():
    with pytest.raises(ArithmeticError, match='целочисленное деление только для целых'):
        calculator([('NUMBER', 1.0), ('NUMBER', 3.0), ('OPERATOR', '/'), ('NUMBER', 100.0), ('OPERATOR', '//')])


def test_int_remainder():
    with pytest.raises(ArithmeticError, match='деление по модулю только для целых'):
        calculator([('NUMBER', 5.5), ('NUMBER', -100.0), ('OPERATOR', '-'), ('NUMBER', 10.0), ('OPERATOR', '%')])


def test_addition():
    assert calculator([('NUMBER', 1.0), ('NUMBER', 2.0), ('NUMBER', 3.0), ('NUMBER', 4.0), ('OPERATOR', '+'), ('OPERATOR', '+'), ('OPERATOR', '+')]) == 10


def test_subtraction():
    assert calculator([('NUMBER', 5.0), ('NUMBER', 5.0), ('OPERATOR', '-')]) == 0


def test_multiplication():
    assert calculator([('NUMBER', 5.5), ('NUMBER', 10.0), ('OPERATOR', '*')]) == 55


def test_division_int():
    assert calculator([('NUMBER', 12.0), ('NUMBER', 5.0), ('OPERATOR', '//')]) == 2


def test_division_float():
    assert calculator([('NUMBER', 14.0), ('NUMBER', 4.0), ('OPERATOR', '/')]) == 3.5


def test_remainder():
    assert calculator([('NUMBER', 14.0), ('NUMBER', 4.0), ('OPERATOR', '%')]) == 2


def test_pow():
    assert calculator([('NUMBER', 2.0), ('NUMBER', 2.0), ('OPERATOR', '**'), ('NUMBER', 5.0), ('OPERATOR', '**'), ('NUMBER', 10.0), ('OPERATOR', '**')]) == 1267650600228229401496703205376
