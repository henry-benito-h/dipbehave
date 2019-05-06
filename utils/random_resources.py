import random
import string


def random_string(size='20'):
    return "".join([random.choice(string.ascii_letters) for i in range(int(size))])


def random_week_day():
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return random.choice(week_days)
