from .operations.divide import divide
from .operations.multiply import multiply
from .operations.sumatory import sumatory


def sum_operation(a, b):
    return sumatory(a, b)

def multiply_operation(a, b):
    return multiply(a, b)

def divide_operation(a, b):
    return divide(a, b)
