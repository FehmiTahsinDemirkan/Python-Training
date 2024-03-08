class Product : 
    def __init__(self,name,price):
        self.name = name
        self.price =price
        if price >=0:
            self._price =price
        else:
            raise ValueError("Negatif olamaz")
    @property
    def price(self):
        return self._price
   

    # def set_price(self,value):
    #     if value >=0:
    #         self._price = value  
    #     else :
    #         raise ValueError("Ürün fiyatı için negatif değer ataması yapma")  
    # def get_price(self):
    #     return self._price 

p = Product("iphone 11",99000)

# print(p.get_price())
# p.set_price(500)
# print(p.get_price())
print(p.price)