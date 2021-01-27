import random
import string
from string import ascii_letters, digits


def generator(size):
    password = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return password


quantity = int(input("How many digits do you want the password to have?: "))
pasw = generator(quantity)
print(pasw)
