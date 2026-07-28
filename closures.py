def outer():
    message = "Hello"

    def inner():
        print(message)   # Accesses variable from outer function

    return inner

greet = outer()
greet()