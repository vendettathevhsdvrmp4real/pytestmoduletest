import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_multiplication():
    assert calculate(200, 6, '*') == 1200

def test_calculate_minus():
    assert calculate(600, 200, '-') == 400

def test_calculate_division2():
    assert calculate(50, 2, '/') == 25

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."