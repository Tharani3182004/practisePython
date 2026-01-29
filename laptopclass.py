class laptop:
    price=""
    processer=""
    ram=""
    def hp(self):
        print("hello hp")
    def lenova(self):
        print("hello lenova")
    def dell(self):
        print("hello dell")

hp=laptop()
lenova=laptop()
dell=laptop()

hp.price="33"
hp.ram="8gb"

lenova.price="44"
lenova.ram="7gb"
print(hp.price)
print(hp.ram)
print(lenova.price)
print(lenova.ram)