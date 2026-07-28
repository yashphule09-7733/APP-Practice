def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"

for fruit in fruits():
    print(fruit)