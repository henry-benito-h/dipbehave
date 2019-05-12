import random
import string


def random_string(args=['20']):
    return "".join([random.choice(string.ascii_letters) for i in range(int(args[0]))])


def random_integer(args=[0, 10]):
    return random.randint(int(args[0]), int(args[1]))


def random_week_day():
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return random.choice(week_days)


def random_boolean():
    bool_values = ["true", "false"]
    return random.choice(bool_values)


def random_privacy():
    bool_values = ["private", "public"]
    return random.choice(bool_values)
