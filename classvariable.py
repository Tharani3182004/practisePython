class phone:
    chargertype="Ctype"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(self.brand)
        print(self.price)
        print(self.chargertype)

redmi=phone("redmi","10000")
redmi.display()