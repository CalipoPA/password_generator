import random
import string
import pyperclip
import time
from string import ascii_letters, digits


def generator(size):
    password = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return password


quantity = int(input("How many digits do you want the password to have?: "))
pasw = generator(quantity)

pyperclip.copy(pasw)
print("Your password has been copied to the clipboard ")

time.sleep(10)
quit()
