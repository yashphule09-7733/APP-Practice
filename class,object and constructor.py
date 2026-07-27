class car:
    def __init__(self,brand,car_name):
        self.brand=brand
        self.car_name=car_name
        
    def display(self):
        print("BRAND=",self.brand)
        print("car_name",self.car_name)
        
c1 = car("TOYOTA","INNOVA")
c2 = car("BMW","m")

c1.display()
c2.display()