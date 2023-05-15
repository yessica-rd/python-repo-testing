def sum(num1, num2):
    return _message(num1, num2)

def method_2():
    return "This is method 2"

def method_3():
    return "This is method 3"

def _message(num1, num2):
    return "The sum of {} and {} is {}".format(num1, num2, sum(num1, num2))
