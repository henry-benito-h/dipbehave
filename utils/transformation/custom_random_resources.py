import random
from transformation.random_resources import RandomResources


class CustomRandomResources(RandomResources):
    def random_week_day(self, context=None):
        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return random.choice(week_days)

    def random_boolean(self, context=None):
        bool_values = ["true", "false"]
        return random.choice(bool_values)

    def random_privacy(self, context=None):
        bool_values = ["private", "public"]
        return random.choice(bool_values)

    def get_var(self, var_name, context=None):
        if context is not None:
            result = context.vars[var_name[0]]
            return str(result)
            # return str(getattr(context.vars, str(var_name[0])))
