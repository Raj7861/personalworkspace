import logging
from pathlib import Path

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('./logging/employee.log')
file_handler.setFormatter(formatter)



logger.addHandler(file_handler)



class Employee:
    """A simple employee class"""
    
    def __init__(self, first, last):
        self.first = first
        self.last =last

        logger.info(f'Created Employee: {self.fullname} - {self.email}')
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Siraj', 'Motaung')
emp_2 = Employee('Shameel', 'Nkosi')
emp_2 = Employee('Ossama', 'Issah')

print(f'No Parent - Printing the path = {Path(__file__)}')
print(f'Printing the path with parent = {Path(__file__).parent.absolute()/"Data"}')