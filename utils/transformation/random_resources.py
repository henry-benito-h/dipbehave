import random
import string


class RandomResources:
    def random_string(self, args=['20'], context=None):
        return "".join([random.choice(string.ascii_letters) for i in range(int(args[0]))])

    def random_integer(self, args=[0, 10], context=None):
        return random.randint(int(args[0]), int(args[1]))
