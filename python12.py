"""
#
# Part: Python String Formatting
#
"""

price = 60
txt = f"Price is {price} Bath."
print (txt)
txt = f"Price is {price:.2f} Bath"
print (txt)

price = 50
tax = 0.25
txt = f"Price is {price + (price*tax):.2f} Bath."
print (txt)

price = 10000
txt = f"Price is {price:,.2f} Bath."
print (txt)