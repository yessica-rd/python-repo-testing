# from src.operations.divide import divide
# from src.operations.multiply import multiply
# from operations.sumatory import sumatory

import os
os.path.dirname(os.path.abspath("__file__"))


def sum_operation(a, b):
    print('This is the sum_operation function')
    return sumatory(a, b)

# def multiply_operation(a, b):
#     return multiply(a, b)

# def divide_operation(a, b):
#     return divide(a, b)

def hello():
    return "Hello world!"

if __name__ == "__main__":
    from src.operations.sumatory import sumatory
