import random
import string


class Helpers:

    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return random_string
