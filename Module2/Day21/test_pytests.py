# Pytest primarily uses assert statements to test functions in the module.
# This allows the developer to determine different cases in which the program
# should succeed or fail.
# The testing code is separated from the rest of the program in a separate file.
# This testing file should start with test_ or end with _test.py.
import pytest
from module2_day21_pytest import BasicCalc


# Day 21: Pytest
def test_add():
    calculator = BasicCalc()
    result = calculator.add(2, 2)
    assert result == 4


def test_subtract():
    calculator = BasicCalc()
    result = calculator.subtract(2, 2)
    assert result == 0


def test_multiply():
    calculator = BasicCalc()
    result = calculator.multiply(2, 2)
    assert result == 4


def test_divide():
    calculator = BasicCalc()
    result = calculator.divide(2, 2)
    assert result == 1


def test_zero_div():
    calculator = BasicCalc()
    result = calculator.divide(5, 0)
    assert result == "ZeroDivisionError"


def test_will_fail():
    calculator = BasicCalc()
    result = calculator.add(2, 2)
    assert result == 5

#test will fail (useful for unfinished code)

def test_man_fail():
    calculator = BasicCalc()
    with pytest.fail("I made this one fail."):
        calculator.add(2, 2)

# thank god for stackoverlow
# Pating "pytest --show-capture" in terminal allowed me to see which tests would fail