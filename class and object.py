#Định nghĩa class
class car:
    def __init__(self,make, model, year): #Constructor
        self.make = make
        self.model = model
        self.year = year
    def diplay_info(self):
        print(f"Car:{self.make}{self.model}{self.year}")
car1 = car("mclaren","mclaren 767LT",2022)
car2 = car("mclaren","mclaren 750S",2015)

car1.diplay_info()
car2.diplay_info()
#Có 4 khái niệm quan trọng 
#Tính đóng gói , đa hình , trừu tượng , kế thừa