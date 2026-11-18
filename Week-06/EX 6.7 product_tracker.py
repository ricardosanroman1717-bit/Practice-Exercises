class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name : {self.name}")
        print(f"Category     : {self.category}")
        print(f"Price        : ${self.price:.2f}")
        print(f"Quantity     : {self.quantity} units")
        print("-----------------------------")

    def inventory_value(self):
        total = self.price * self.quantity
        print(f"Inventory value for {self.name}: ${total:.2f}")
        print("-----------------------------")


print("=== Enter Product 1 ===")
name1 = input("Product name: ")
category1 = input("Category:     ")
price1 = float(input("Price $:      "))
quantity1 = int(input("Quantity:     "))

print("\n=== Enter Product 2 ===")
name2 = input("Product name: ")
category2 = input("Category:     ")
price2 = float(input("Price $:      "))
quantity2 = int(input("Quantity:     "))

product1 = Product(name1, category1, price1, quantity1)
product2 = Product(name2, category2, price2, quantity2)

print(f"\n===== Product 1: {product1.name} =====")
print(f"Product 1: {product1.name}   {product1.category}")
product1.display_info()
product1.inventory_value()

print(f"===== Product 2: {product2.name} =====")
print(f"Product 2: {product2.name}   {product2.category}")
product2.display_info()
product2.inventory_value()
