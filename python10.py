"""
#
# Part: Python JSON
# API = Application Programming Interface
"""

import json

# make a json (Dictionary String)
x = '{"name": "john", "age": 20 , "city": "Phuket"}'
print(x)

# parse
y = json.loads(x)

# python dictionary
print(y)
print(type(y))
print(y["city"])

# python dictionary
a = {
    "name": "Noa",
    "age": 20,
    "city": "Phuket"
}

# convert to JSON (String)
b = json.dumps(a)

# JSON String
print (b)