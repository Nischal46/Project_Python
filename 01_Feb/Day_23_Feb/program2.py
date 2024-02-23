#movie ticket pricing

age = int(input("Enter your age: "))
# day = 'friday'
day = 'wednesday'


print("")
print("1st approach")
if (day == 'wednesday'):

    if(age < 18):
        price = 8
        print(f"Your ticket price is ${price} and you got $2 discount on wednesday.\nYour total price is ${price - 2}")

    else:
        price = 12
        print(f"Your ticket price is ${price} and you got $2 discount on wednesday.\nYour total price is ${price - 2}")

else:
    if(age < 18):
        price = 8
        print(f"Your ticket price is ${price}.")

    else:
        price = 12
        print(f"Your ticket price is ${price} and you got $2 discount on wednesday.\nYour total price is ${price - 2}")

print("")
print("2nd approach")

ticket_price = 12 if age > 18 else 8
ticket_price = ticket_price - 2 if day == 'wednesday' else ticket_price

print(f"Your age is {age} and price is {ticket_price}")