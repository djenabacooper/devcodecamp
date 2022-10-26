from Customer import Customer
from Product import Product
from ShoppingCart import ShoppingCart

prod1 = Product('Eggs', 2.15,'Dairy')
prod2 = Product('Milk', 2.15, 'Dairy')
prod3 = Product('Flour', 4.25, 'Baking')


customer1 = Customer('Peter','Parker','Cheese')
print(customer1.FirstName + ' '+ customer1.LastName)

customer1.add_new_prod(prod1)
customer1.add_new_prod(prod2)
customer1.add_new_prod(prod3)

customer1.see_cart()
customer1.cart_total()
