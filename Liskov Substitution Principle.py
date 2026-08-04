class Bird:
    def fly(self):
        print("Bird can fly")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")


def make_bird_fly(bird):
    bird.fly()


sparrow = Sparrow()
make_bird_fly(sparrow)

ostrich = Ostrich()
make_bird_fly(ostrich)   # Error
