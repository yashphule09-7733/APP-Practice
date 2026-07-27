class Student:
    school = "ABC School"   # Class variable

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

    # Class Method
    @classmethod
    def school_name(cls):
        print("School:", cls.school)

    # Static Method
    @staticmethod
    def message():
        print("Have a great day!")

# Create object
s1 = Student("Yash", 47)

# Call methods
s1.display()              # Instance method
Student.school_name()     # Class method
Student.message()         # Static method