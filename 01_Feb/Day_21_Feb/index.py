username = 'Nischal'
print(username)

#List or Array

DataList = ['Nepal', 'America', 'Australia']

print(f"The array of python {DataList}")
print(f"The array length of python {len(DataList)}")


#Object or Dictionary
DataObject = {'id': '123',
    'name': 'Nischal Baniya',
    'email': 'baniyanisal12@gmail.com',
    'password': 'admin'
}

print(f"The object of the student {DataObject}")

#Tuple
DataTuple = (123, 'Python', True)
print(f"Tuple in python {DataTuple}")

#loops
Mobile = [{
    'name': 'Iphone',
    'price': 120000
},
{
    'name': 'Samsung',
    'price': 50000
},
{
    'name': 'Red MI',
    'price': 25000
},
{
    'name': 'Oppo',
    'price': 20000
}]

print(f"length of Array {len(Mobile)}")

for i in Mobile:
    print(f"Mobile Brand: {i['name']} Price: {i['price']}")

i = 0

while(i<len(Mobile)):
    print(Mobile[i])
    i = i + 1

# Summary of today
    # Mutable Data Type : List, Set, Dictionary, Array

    # Immutable Data Type: Integers, Float, Boolean, Strings, Tuples, Bytes

