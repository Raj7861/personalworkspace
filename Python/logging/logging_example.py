import logging
import employee


FORMAT = '%(asctime)s - %(levelname)s - %(message)s' 
logging.basicConfig(filename='./logging/testloging.log',level=logging.DEBUG, format=FORMAT)

def add(x, y):
    """Add function"""
    return x+y

def subtract(x, y):
    """Subtract function"""
    return x - y

def multiply(x, y):
    """Multiply function"""
    return x * y

def divide(x, y):
    """Divide function"""
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logging.debug(f'Sub: {num_1} + {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logging.debug(f'Mul: {num_1} + {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logging.debug(f'Div: {num_1} + {num_2} = {div_result}')
