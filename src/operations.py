# from src.operations.divide import divide
# from src.operations.multiply import multiply
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from operations.sumatory import sumatory


def sum_operation(a, b):
    return sumatory(a, b)

# def multiply_operation(a, b):
#     return multiply(a, b)

# def divide_operation(a, b):
#     return divide(a, b)

def hello():
    return "Hello world!"
