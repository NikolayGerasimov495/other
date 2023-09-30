import pytest
from tests.fizzbuzz_func import fizzbuzz

@pytest.mark.parametrize("test_input, expected", [(0, [])])
def test_fizzbuzz_is_zero(test_input: int, expected: list) -> list:
    assert fizzbuzz(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(16, ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16'])])
def test_fizzbuzz_is_digit(test_input: int, expected: list) -> list:
    assert fizzbuzz(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(3, 3)])
def test_size(test_input: int, expected: bool) -> True:
    assert len(fizzbuzz(test_input)) == expected




# def test_fizzbuzz():
#    assert fizzbuzz(16) == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16']

# def test_size():
#     assert len(fizzbuzz(3)) == 3
