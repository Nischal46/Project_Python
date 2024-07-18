# lambda function is also known as anonymonous function
# it can handle only one expressions

# lambda arguements: expression

#first case
area_of_circle = lambda x, y: 2*x + 2*y
print(area_of_circle(2,3))

#second case
numbers = [12,13,14,15,16,17]
divisible_by_two = list(filter(lambda x: x%2 == 0, numbers))
print(divisible_by_two)

#functions
def greetings(name, email):
    print(f'welcome {name} and your email is {email}')

greetings('nischal', 'nischal@gmail.com')

#likewise object in js there is dictionaries

instrruments_price = {
    "guitar": 7500,
    "ukulele": 2500
}

print(instrruments_price)

#looping in object
for x in instrruments_price:
    print(f'Instrument name: {x} and price is {instrruments_price[x]}')

# we can also get the direct values
for x in instrruments_price.values():
    print(f'accessing the direct val {x}')