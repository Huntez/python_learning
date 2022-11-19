# from functools import wraps

def header(func):
    def inner(*args):
        print("<h1>")
        func(*args)
        print("</h1>")
    return inner

def table(func):
    @my_wraps
    def inner(*args):
        print("<table>")
        func(*args)
        print("<table>")
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner

@table
def say(name, surname, age):
    print("hello world", name, surname, age)

@table
def sqr(x):
    """
    multiply x to cube
    :param x
    :return 
    """
    print(x**2)


print(help(sqr))


