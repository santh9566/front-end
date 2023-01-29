class mobile:
    def __init__(self,brand,price):
        print("inside constructor")
        self.brand=brand
        self.price=price
        
    def purchase(self):
        print("purchasing a mobile")
        print("this mobile has brand",self.brand,"and price"),
        
        print("mobile-1")
        mob1=mobile("Apple",20000)
        mob1.purchase()
        
        print("mobile-2")
        mob2=mobile("Samsung",3000)
        mob2.purchase()
