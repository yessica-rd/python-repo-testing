from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.utils import print_message


def sumatory(num1, num2):
    return print_message(num1, num2, '+', num1 + num2)

result = sum(1, 2)

print(result)

