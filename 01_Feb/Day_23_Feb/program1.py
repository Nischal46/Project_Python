print(f"Age Group Categorization")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if(age < 13):
    print(f"Your name is {name} and You are {age} years old")
    print("Child Group")

elif(age <=19):
    print(f"Your name is {name} and You are {age} years old")
    print("Teenager Group")

elif(age <= 59):
    print(f"Your name is {name} and You are {age} years old")
    print("Adult Group")

else:
    print(f"Your name is {name} and You are {age} years old")
    print("Senior Group")