class car:
    tax = 2
    def __init__(self,brand,model,money):
        self.brand = brand
        self.model = model
        self.money = money
#regular method
    def tax_Mclaren(self):
        return (self.tax * self.money)
    @classmethod
    def set_tax(cls):
        cls.tax = 4
    @classmethod
    def front_string(cls,car_string):
        brand,model,money = car_string.split('-')
        money = int(money)
        return  cls(brand,model,money)

car1 = car("Mclaren","mclaren765LT",1200)
car2 = car("Lambogini","Adventador",1000)
car3 = "Ferari-ferari88-1300"
car3 = car.front_string(car3)
print("Profile car:", car1.brand,car1.model,car1.money, sep=' ')
print(f"{car1.brand} Price {car1.tax_Mclaren()}$")
print(f"{car2.brand} Price {car2.tax_Mclaren()}$")
print(car1.set_tax())
print(car2.tax_Mclaren())
print(car3.brand ,car3.model,car3.money)
