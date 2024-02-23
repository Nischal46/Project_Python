string1 = 'tester'
print(string1.__contains__("r"))
check__repeated_string = ""

for character in string1:
    
    if check__repeated_string.__contains__(character):
        print(f"{character} contains multiple times ")
        print("")


    check__repeated_string = check__repeated_string + character
print(check__repeated_string)

#program to compute the factorial munber
num = 5

fact = 1
while(num > 0):
    fact = fact * num
    num = num - 1

print(f"factorial: {fact}")

#program that take number input from user until the input is between 1 to 10 from the user

num_condition = True

while num_condition:
    num_input = int(input("Enter a number: "))
    if(1 <= num_input <= 10):
        print('Program is quitting')
        break

    else:
        print("Please give valid input number")


#to check the duplicacy

list1 = ['flute', 'guitar', 'ukulele', 'drum', 'casion', 'ukulele']

list2 = set()

for item in list1:
    if(item in list2):
        print(f"duplicate item detected {item}")
        break
    
    else:
        list2.add(item)


