class car:
    tax = 2
    def __init__(self,brand,model,money):
        self.brand = brand
        self.model = model
        self.money = money
    def tax_Mclaren(self):
        return (self.tax * self.money)
    
car1 = car("Mclaren","mclaren765LT",1200)
car2 = car("Lambogini","Adventador",1000)
print("Profile car:", car1.brand,car1.model,car1.money, sep=' ')
print(f"{car1.brand} Price {car1.tax_Mclaren()}$")
print(f"{car2.brand} Price {car2.tax_Mclaren()}$")
