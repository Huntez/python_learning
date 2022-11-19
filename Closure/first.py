# def adder(value):
#     def inner(a):
#         return value + a
#     return inner

# a = adder(10)
# print(a(20), a(50), a(10))

# def counter():
#     count = 0
#     def inner(value):
#         nonlocal count
#         count += value
#         return count
#     return inner        

# a = counter()
# print(a(10), a(15), a(20))

# def ssum(number):
#     suma = 0
#     def inner(value):
#         nonlocal suma
#         suma += value + number
#         return suma
#     return inner

# a = ssum(10)
# print(a(10), a(20), a(30))

# def avg_numbers():
#     numbers = []
#     def inner(number):
#         numbers.append(number)
#         print(numbers)
#         return sum(numbers) / len(numbers)
#     return inner

# r1 = avg_numbers()
# print(r1(10), r1(20), r1(25))

# from datetime import datetime
# from time import perf_counter

# def timer():
#     start = perf_counter()
#     def inner():
#         nonlocal start
#         result = perf_counter() - start
#         start = perf_counter()
#         print(start)
#         return result
#     return inner

# a = timer()
# print(a(), a())

# def add(a,b):
#     return a+b

# def counter(func):
#     count = 0
#     def inner(*args):
#         nonlocal count
#         count += 1
#         print(f"function {func.__name__} call count times {count}")
#         print(args)
#         return func(*args)
#     return inner

# q = counter(add)
# print(q(10,20), q(10,20))

# def func(*args):
#     print(*args)

# print(func(2,2,2,2))

# Lambda functions

# multiply = lambda *x : sum(x)
# print(multiply(1,2,3,4))

# t = lambda x: 'positvie' if x > 0 else 'negative'
# print(t(5))
 
# a = [5,2,1,2,4]
# a.sort(key=lambda x: x)
# print(a)

# decorator
def decator(func):
    
    def inner():
        print('start decorator')
        func()
        print('finish decorator')
    return inner

def say():
    print("hello world")

say = decator(say)

    