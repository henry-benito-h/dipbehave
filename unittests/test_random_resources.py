from utils.random_resources import *


def test_random_string_default_value():
    new_string = random_string()
    assert len(new_string) == 20


def test_random_string_with_size_10():
    new_string = random_string(10)
    assert len(new_string) == 10


def test_random_boolean():
    values = ['true', 'false']
    new_bool = random_boolean()
    if new_bool in values:
        result = True
    else:
        result = False
    assert result


def test_random_week_day():
    values = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    weekday = random_week_day()
    if weekday in values:
        result = True
    else:
        result = False
    assert result
