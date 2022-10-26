from Product import Product
#cart_prods = []
class ShoppingCart:
    def __init__(self):
        self.cart_prods = []


    #def cart_total(self):
     #   total = 0
      #  for product in self.cart_prods:
       #     total += 
       # self.item_price = self.
        #self.items = self.cart_prods
        #self.total = self.cart_prods + Product.prod_price

       # print(self.total)
    
    def add_to_cart(self,new_prod):
        self.cart_prods.append(new_prod)
        print(self.cart_prods)


    def empty_cart(self):
        self.cart_prods.clear


