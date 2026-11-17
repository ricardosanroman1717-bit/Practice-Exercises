apply_discount = lambda price, pct: price * (1 - pct / 100)
apply_tax = lambda price, rate: price * (1 + rate / 100)
final_price = lambda price, disc, tax: apply_tax(apply_discount(price, disc), tax)

product = input("Product name: ")
category = input("Category: ")
price = float(input("Original price $: "))
discount = float(input("Discount %: "))
tax_rate = float(input("Tax rate %: "))

discounted = apply_discount(price, discount)
taxed = apply_tax(discounted, tax_rate)
total = final_price(price, discount, tax_rate)
savings = price - discounted

print(f"""
====== PriceIQ - Product Pricing Report ======
Product : {product}
Category : {category}
----------------------------------------------
Original price   : ${price:.2f}
Discount ({discount:.0f}%)    : -${savings:.2f}
Price after disc : ${discounted:.2f}
Tax ({tax_rate:.0f}%)         : +${taxed - discounted:.2f}
----------------------------------------------
Final price      : ${total:.2f}
==============================================
""")
