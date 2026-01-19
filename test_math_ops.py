"""
Тесты для модуля math_ops.
"""
import pytest
from math_ops import add_numbers, multiply_numbers


def test_add_integers():
    """Проверяет сложение целых чисел."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_add_floats():
    """Проверяет сложение чисел с плавающей точкой."""
    assert add_numbers(2.5, 3.1) == pytest.approx(5.6)


def test_multiply_integers():
    """Проверяет умножение целых чисел."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-2, 3) == -6


def test_multiply_floats():
    """Проверяет умножение чисел с плавающей точкой."""
    assert multiply_numbers(2.5, 2) == pytest.approx(5.0)


def test_add_type_error():
    """Проверяет, что функция сложения не принимает строки."""
    with pytest.raises(TypeError):
        add_numbers("2", 3)  # type: ignore
