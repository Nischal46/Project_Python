#dictionaries
#similar as object in other programming language

gadget = {'instrument': 'guitar', 'brand': 'mantra', 'color': 'black', 'equalizer': True}

print(gadget)

#can also the reference into new reference using copy function
newgadget = gadget.copy()
print(f"The new copy of the gadget array is {newgadget}")

#find the key and its value
print(gadget.get("brand"))

#find the properties of the object value length
print(len(gadget))

#loop iterations in object
for item in gadget:
    print(f"{item}: {gadget[item]}")

#destructure directly
print(f"destructure in loop")
for item, value in gadget.items():
    print(f"{item}: {value}")

#delete item on the basis of key
# gadget.pop("color")
# print(gadget)
    
#delete the last item in object
gadget.popitem()
print(gadget) 

del gadget["brand"]
print(gadget)

cubenum = {x:x**3 for x in range(2,5)}
print(cubenum)

#creating a new dictionaries

keys = ['name', 'age', 'email']
value = 'Best'

new_dict = dict.fromkeys(keys, value)
print(new_dict)






