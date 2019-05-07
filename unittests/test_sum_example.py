import pytest


def sum_numbers(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2


def test_sum_output_type():
    assert type(sum_numbers(1, 2)) is int


def test_sum_numbers():
    assert sum_numbers(1, 2) == 3


@pytest.mark.parametrize('num1, num2, expected', [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)])
def test_sum_numbers(num1, num2, expected):
    assert sum_numbers(num1, num2) == expected


@pytest.fixture
def get_sum_test_data():
    return [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]


def test_sum(get_sum_test_data):
    for data in get_sum_test_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert sum_numbers(num1, num2) == expected
