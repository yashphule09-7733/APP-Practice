class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()

d.sound()   # Inherited from Animal
d.bark()    # Dog's own method