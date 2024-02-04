import pytest
from calc.calculator import calculate
from calc.ops import add
from calc.ops import subtract
from calc.ops import divide
from calc.ops import multiply
import math

# Точность (tolerance) для проверки чисел с плавающей точкой
TOLERANCE = 1E-9

# Функция для сравнения чисел с плавающей точкой с заданной точностью
def assert_float_equal(a, b, msg=None):
    assert math.isclose(a, b, rel_tol=TOLERANCE, abs_tol=TOLERANCE), msg

# Тесты для функции add()
def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5, f"Unexpected result: {result}"

def test_add_associative_property():
    a, b, c = 2, 3, 4
    result = add(add(a, b), c)
    assert result == add(a, add(b, c)), f"Unexpected result: {result}"

def test_add_mixed_numbers():
    result = add(2, -3)
    assert result == -1, f"Unexpected result: {result}"

def test_add_zero_numbers():
    result = add(1, 0)
    assert result == 1, f"Unexpected result: {result}"

def test_add_property():
    result = add(1, 2)
    assert result == add(2, 1), f"Unexpected result: {result}"

def test_add_integer_numbers():
    result = add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5, f"Expected -5, but got {result}"

def test_add_mixed_numbers():
    result = add(2, -3)
    assert result == -1, f"Expected -1, but got {result}"

def test_add_zero_numbers():
    result = add(1, 0)
    assert result == 1, f"Expected 1, but got {result}"

def test_add_float_numbers():
    result = add(0.1, 0.2)
    assert_float_equal(result, 0.3, f"Expected 0.3, but got {result}")

def test_add_float_numbers():
    result = add(0.1, 0.2)
    assert_float_equal(result, 0.3, f"Expected 0.3, but got {result}")

def test_add_large_numbers():
    result = add(1e20, 1e-10)
    assert_float_equal(result, 1e20, f"Expected 1e20, but got {result}")

# Тесты для функции divide()
def test_divide_positive_numbers():
    result = divide(6, 3)
    assert result == 2, f"Unexpected result: {result}"

def test_divide_negative_numbers():
    result = divide(-6, -3)
    assert result == 2, f"Unexpected result: {result}"

def test_divide_mixed_numbers():
    result = divide(6, -3)
    assert result == -2, f"Unexpected result: {result}"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)

def test_divide_zero():
    result = divide(0, 5)
    assert result == 0, f"Unexpected result: {result}"

def test_divide_positive_numbers():
    result = divide(6, 3)
    assert result == 2, f"Expected 2, but got {result}"

def test_divide_negative_numbers():
    result = divide(-6, -3)
    assert result == 2, f"Expected 2, but got {result}"

def test_divide_mixed_numbers():
    result = divide(6, -3)
    assert result == -2, f"Expected -2, but got {result}"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)

def test_divide_zero():
    result = divide(0, 5)
    assert result == 0, f"Expected 0, but got {result}"

def test_divide_float_numbers():
    result = divide(1.5, 0.5)
    assert_float_equal(result, 3.0, f"Expected 3.0, but got {result}")

def test_divide_large_numbers():
    result = divide(1e20, 1e-10)
    assert_float_equal(result, 1e30, f"Expected 1e30, but got {result}")

def test_divide_float_numbers():
    result = divide(1.0, 3.0)
    assert_float_equal(result, 0.333333333, f"Expected 0.333333333, but got {result}")

# Тесты для функции subtract()
def test_subtract_positive_numbers():
    result = subtract(5, 3)
    assert result == 2, f"Unexpected result: {result}"

def test_subtract_negative_numbers():
    result = subtract(-5, -3)
    assert result == -2, f"Unexpected result: {result}"

def test_subtract_mixed_numbers():
    result = subtract(5, -3)
    assert result == 8, f"Unexpected result: {result}"

def test_subtract_zero_numbers():
    result = subtract(0, -3)
    assert result == 3, f"Unexpected result: {result}"

def test_subtract_feature():
    result = subtract(1, 2)
    assert result == -1, f"Unexpected result: {result}"

def test_subtract_integer_numbers():
    result = subtract(5, 3)
    assert result == 2, f"Expected 2, but got {result}"

def test_subtract_negative_numbers():
    result = subtract(-5, -3)
    assert result == -2, f"Expected -2, but got {result}"

def test_subtract_mixed_numbers():
    result = subtract(5, -3)
    assert result == 8, f"Expected 8, but got {result}"

def test_subtract_zero_numbers():
    result = subtract(0, -3)
    assert result == 3, f"Expected 3, but got {result}"

def test_subtract_float_numbers():
    result = subtract(0.3, 0.1)
    assert_float_equal(result, 0.2, f"Expected 0.2, but got {result}")

def test_subtract_large_numbers():
    result = subtract(1e20, 1e-10)
    assert_float_equal(result, 1e20, f"Expected 1e20, but got {result}")

def test_subtract_float_numbers():
    result = subtract(0.3, 0.1)
    assert_float_equal(result, 0.2, f"Expected 0.2, but got {result}")


# Тесты для функции multiply()
def test_multiply_positive_numbers():
    result = multiply(2, 3)
    assert result == 6, f"Unexpected result: {result}"

def test_multiply_negative_numbers():
    result = multiply(-2, -3)
    assert result == 6, f"Unexpected result: {result}"

def test_multiply_mixed_numbers():
    result = multiply(2, -3)
    assert result == -6, f"Unexpected result: {result}"

def test_multiply_by_zero():
    result = multiply(0, 1)
    assert result == 0, f"Unexpected result: {result}"

def test_multiply_property():
    result = multiply(1, 2)
    assert result == multiply(2, 1), f"Unexpected result: {result}"

def test_multiply_identity_property():
    a = 5
    result = multiply(a, 1)
    assert result == a, f"Unexpected result: {result}"

def test_multiply_float_numbers():
    result = multiply(0.1, 0.2)
    assert_float_equal(result, 0.02, f"Expected 0.02, but got {result}")

def test_multiply_integer_numbers():
    result = multiply(2, 3)
    assert result == 6, f"Expected 6, but got {result}"

def test_multiply_float_numbers():
    result = multiply(0.1, 0.2)
    assert_float_equal(result, 0.02, f"Expected 0.02, but got {result}")

def test_multiply_zero():
    result = multiply(5, 0)
    assert result == 0, f"Expected 0, but got {result}"

def test_multiply_negative_numbers():
    result = multiply(-2, 3)
    assert result == -6, f"Expected -6, but got {result}"

def test_multiply_mixed_numbers():
    result = multiply(2, -3.5)
    assert_float_equal(result, -7.0, f"Expected -7.0, but got {result}")

def test_multiply_large_numbers():
    result = multiply(1e20, 1e-20)
    assert_float_equal(result, 1.0, f"Expected 1.0, but got {result}")
    
def test_multiply_large_float_numbers():
    result = multiply(1e20, 1e-10)
    assert_float_equal(result, 1e10, f"Expected 1e10, but got {result}")
    
def test_multiply_large_numbers():
    result = multiply(123456789, 987654321)
    assert result == 121932631112635269, f"Expected 121932631112635269, but got {result}"

def test_multiply_zero_numbers():
    result = multiply(123, 0)
    assert result == 0, f"Expected 0, but got {result}"

def test_multiply_large_and_small_float_numbers():
    result = multiply(1.2345e-5, 6.789e7)
    assert_float_equal(result, 838.10205, f"Expected 838.10205, but got {result}")
    
def test_multiply_very_small_numbers():
    result = multiply(1e-100, 1e-200)
    assert_float_equal(result, 1e-300, f"Expected 1e-300, but got {result}")
    
# Тесты для функции calculate()
def test_calculate_addition():
    result = calculate("3 + 2")
    assert result == 5, f"Expected 5, but got {result}"

def test_calculate_subtraction():
    result = calculate("3 - 2")
    assert result == 1, f"Expected 1, but got {result}"

def test_calculate_multiplication():
    result = calculate("3 * 2")
    assert result == 6, f"Expected 6, but got {result}"

def test_calculate_division():
    result = calculate("6 / 2")
    assert result == 3, f"Expected 3, but got {result}"

def test_calculate_complex_expression():
    result = calculate("3 + 2 * 3")
    assert result == 9, f"Expected 9, but got {result}"

def test_calculate_expression_with_parentheses():
    result = calculate("(3 + 2) * 3")
    assert result == 15, f"Expected 15, but got {result}"

def test_calculate_expression_with_negative_numbers():
    result = calculate("3 + (-2)")
    assert result == 1, f"Expected 1, but got {result}"

def test_calculate_expression_with_whitespace():
    result = calculate(" 3   +   2 ")
    assert result == 5, f"Expected 5, but got {result}"

def test_calculate_expression_with_invalid_operator():
    with pytest.raises(ValueError):
        calculate("3 ^ 2")

def test_calculate_expression_with_invalid_syntax():
    with pytest.raises(SyntaxError):
        calculate("3 + 2 *")

def test_calculate_expression_with_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("3 / 0")

def test_calculate_expression_with_float_result():
    result = calculate("5 / 2")
    assert result == 2.5, f"Expected 2.5, but got {result}"

def test_calculate_expression_with_rounded_result():
    result = calculate("5 // 2")
    assert result == 2, f"Expected 2, but got {result}"

def test_calculate_expression_with_exponentiation():
    result = calculate("2 ** 3")
    assert result == 8, f"Expected 8, but got {result}"

def test_calculate_expression_with_multiple_operators():
    result = calculate("2 + 3 * 4 - 5 / 2")
    assert result == 11.5, f"Expected 11.5, but got {result}"

def test_calculate_expression_with_invalid_character():
    with pytest.raises(ValueError):
        calculate("2 + a")

def test_calculate_float_result():
    result = calculate("1.5 + 2.3 * 0.7")
    assert_float_equal(result, 3.11, f"Expected 3.11, but got {result}")
    
def test_calculate_expression_with_negative_numbers():
    result = calculate("3 + (-2)")
    assert result == 1, f"Expected 1, but got {result}"

def test_calculate_expression_with_whitespace():
    result = calculate(" 3   +   2 ")
    assert result == 5, f"Expected 5, but got {result}"

def test_calculate_expression_with_invalid_operator():
    with pytest.raises(ValueError):
        calculate("3 ^ 2")

def test_calculate_expression_with_invalid_syntax():
    with pytest.raises(SyntaxError):
        calculate("3 + 2 *")

def test_calculate_expression_with_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("3 / 0")

def test_calculate_expression_with_float_result():
    result = calculate("5 / 2")
    assert result == 2.5, f"Expected 2.5, but got {result}"

def test_calculate_expression_with_rounded_result():
    result = calculate("5 // 2")
    assert result == 2, f"Expected 2, but got {result}"

def test_calculate_expression_with_exponentiation():
    result = calculate("2 ** 3")
    assert result == 8, f"Expected 8, but got {result}"

def test_calculate_expression_with_multiple_operators():
    result = calculate("2 + 3 * 4 - 5 / 2")
    assert result == 11.5, f"Expected 11.5, but got {result}"

def test_calculate_expression_with_invalid_character():
    with pytest.raises(ValueError):
        calculate("2 + a")

def test_calculate_expression_with_trailing_operators():
    with pytest.raises(SyntaxError):
        calculate("2 + 3 *")

def test_calculate_expression_with_leading_operators():
    with pytest.raises(SyntaxError):
        calculate("+ 2 + 3")

def test_calculate_expression_with_missing_operands():
    with pytest.raises(SyntaxError):
        calculate("2 + * 3")

def test_calculate_expression_with_empty_expression():
    with pytest.raises(SyntaxError):
        calculate("")
def test_multiply_large_number_and_zero():
    result = multiply(1e100, 0)
    assert_float_equal(result, 0, f"Expected 0, but got {result}")

# Запуск всех тестов
if __name__ == "__main__":
    pytest.main()
