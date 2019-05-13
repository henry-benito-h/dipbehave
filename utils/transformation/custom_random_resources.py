import random
from transformation.random_resources import RandomResources


class CustomRandomResources(RandomResources):
    def random_week_day(self):
        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return random.choice(week_days)

    def random_boolean(self):
        bool_values = ["true", "false"]
        return random.choice(bool_values)

    def random_privacy(self):
        bool_values = ["private", "public"]
        return random.choice(bool_values)
