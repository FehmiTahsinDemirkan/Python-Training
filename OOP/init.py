class Product : 
    def __init__(self,name,price,isActive) :
        self.name=name
        self.price = price
        self.isActive = isActive
        print("product nesnesi oluşturuldu")

p1 = Product("İphone 15",50000,False)
p2 = Product("İphone 15 Pro", 60000,True)

print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)
    