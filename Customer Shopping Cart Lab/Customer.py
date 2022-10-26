from ShoppingCart import ShoppingCart
from Product import Product

class Customer:
    def __init__(self, FirstName, LastName, Cart):
        self.FirstName = FirstName
        self.LastName = LastName
        self.cart = ShoppingCart()


    def add_new_prod(self, prod_param):
        self.cart.add_to_cart(prod_param)

    def cart_total(self):
        total = 0
        for product in self.cart:
            total += self.cart.prod_price
        #self.item_price = Product.prod_price
        #self.items = Product.prod_name
        #self.total = self.cart_prods + Product.prod_price    

    def see_cart(self): #cart_prods):
        for product in self.cart.cart_prods:
            
            print(product.prod_name)