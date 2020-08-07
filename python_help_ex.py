def add(x, y):
    """
    This function adds the given integer arguments
    :param x: integer
    :param y: integer
    :return: integer
    """
    return x + y

class Employee:
    """
    Employee class, mapped to "employee" table in 
    Databas
    """
    id = 0
    name = ''

    def __init__(self, i, n):
        """
        Employee object constructor
        :param i: integer, must be positive
        :param n: string
        """
        self.id = i
        self.name = n

# First execute the script to load the function
# and class definition in py shell.
# executing here creates a recursion error! ofc
# exec(open("python_help_ex.py").read())

# the practice viewing the help()
help('python_help_ex')
help('python_help_ex.add')
help('python_help_ex.Employee')
help('python_help_ex.Employee.__init__')
# Python help() function is very helpful to get details
# about modules, classes, functions. it's always best 
# practice to define docstring for the custom classes
# and functions to explain their usage
