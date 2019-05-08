import random
import string


def random_string(size='20'):
    return "".join([random.choice(string.ascii_letters) for i in range(int(size))])


def random_integer(max_value='5'):
    return random.randint(1, int(max_value))


def random_week_day():
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return random.choice(week_days)


def random_boolean():
    bool_values = ["true", "false"]
    return random.choice(bool_values)


def random_privacy():
    bool_values = ["private", "public"]
    return random.choice(bool_values)
