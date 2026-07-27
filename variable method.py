class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


# Creating objects outside the class
s1 = Student("Yash", 47)
s2 = Student("Om", 46)

s1.display()
print()
s2.display()
