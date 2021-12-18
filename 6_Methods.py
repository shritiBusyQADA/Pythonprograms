def my_fun(var):
    print(var)


my_fun('hello') # calling of the my_fun method


def my_fun1(name='NA'): # Default value assignment
    print('Hello ' + name)

my_fun1('Simran')
my_fun1()


def square(num):
    """
    THIS IS DOCSTRING
    This method is taking a number and
    returning square of the number
    """
    return num**2

square_value= square(2)
print(square_value)
print(square(4))
