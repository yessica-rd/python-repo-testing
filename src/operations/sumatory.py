import os
os.path.dirname(os.path.abspath("__file__"))

from utils.utils import print_message


def sumatory(num1, num2):
    print('This is the sumatory function')
    return print_message(num1, num2, '+', num1 + num2)

result = sum(1, 2)

print(result)

if __name__ == "__main__":
    from utils.utils import print_message

