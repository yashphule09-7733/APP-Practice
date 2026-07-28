def uppercase_decorator(func):

    def wrapper():
        result = func()
        return result.upper()

    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())