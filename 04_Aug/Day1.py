
divisibleby2 = []

for x in range(1, 10):
    if(x % 2 == 0):
        divisibleby2.append(x) #append add thee items in list

print(divisibleby2)

#lambda function is also known s anonymous function

x = lambda a, b, c : a + b + c
print(x(6, 6, 2))

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)