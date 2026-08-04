class Keyboard:
    def type(self):
        print("Typing with Keyboard")


class Computer:
    def __init__(self):
        self.keyboard = Keyboard()   # Direct dependency

    def start(self):
        self.keyboard.type()


computer = Computer()
computer.start()
