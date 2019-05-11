from transformation.random_resources import *


def test_random_string_default_value():
    new_string = random_string()
    assert len(new_string) == 20


def test_random_string_with_size_10():
    new_string = random_string(['10'])
    assert len(new_string) == 10


def test_random_integer_with_default_values():
    new_integer = random_integer(['0', '10'])
    assert 0 <= new_integer < 10


def test_random_boolean():
    values = ['true', 'false']
    new_bool = random_boolean()
    assert new_bool in values


def test_random_week_day():
    values = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    weekday = random_week_day()
    assert weekday in values


def test_random_privacy():
    values = ['public', 'private']
    weekday = random_privacy()
    assert weekday in values
