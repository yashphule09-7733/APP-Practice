class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def save_to_database(self):
        print(f"Saving {self.name} to the database.")

    def generate_report(self):
        print(f"Generating report for {self.name}.")
