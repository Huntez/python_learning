def check(func):
    def inner(*args):
        if args[0] > args[1]:
            return func(*args)
        else:
            return f"{args[0]} < {args[1]}"
    return inner

@check
def numbers(*args):
    return f"{args[0]} > {args[1]}"

print(numbers(5,3))