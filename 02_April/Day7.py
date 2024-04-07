# declaring a private method inside class

class Instruments:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def __VAT(self):
        amount = (self.price * 13) / 100
        return amount
    
    def MRP(self):
        total = self.__VAT() + self.price
        return total


    def details(self):
        print(f'{self.name} {self.brand} costs Rs {self.MRP()}')

obj1 = Instruments('Guitar', 'Karma', 7500)
obj1.details()
print(dir(obj1))

class Language():
    def __init__(self, name, framework):
        self.__name = name
        self.__framework = framework

    def details(self):
        print(f'{self.__name} and {self.__framework}')

obj2 = Language('js', 'nodejs')
obj2.details()
print(dir(obj2))

        