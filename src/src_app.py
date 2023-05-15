from src.src_message import print_src_message


def sum(num1, num2):
    return print_src_message(num1, num2)

def method_2():
    return "This is method 2"

def method_3():
    return "This is method 3"


from src.operations.divide import divide
from src.operations.multiply import multiply
from src.operations.sumatory import sumatory


def sum_operation(a, b):
    return sumatory(a, b)

def multiply_operation(a, b):
    return multiply(a, b)

def divide_operation(a, b):
    return divide(a, b)