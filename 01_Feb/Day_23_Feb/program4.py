#calculate the no of the count of the positive number in list

def positive_num_count():
    mynumList = [12, -5, 65, -8 ,87, -33, 56]
    count = 0

    for i in mynumList:
        if(i > 0):
            count += 1

    print(f"There are {count} positive number in array")


#calculate the sum of even numbers upto n

number = int(input('Enter a number of range: '))
sum = 0
even_num_list = []

for num in range(0, number):
    if(num % 2 == 0):
        even_num_list.append(num)
        sum += num

print(f"The list of the even number are {even_num_list} and the total sum is {sum}")


multiply_num = int(input("Enter a number to multiply: "))

for num in range(1, 11):
    #1st approach
    # print(f"{multiply_num} * {num} = {num * multiply_num}") if num != 5 else "" 


    #2nd approach
    if(num == 5):
        continue

    print(f"{multiply_num} * {num} = {num * multiply_num}")
    

#reversing the string

reversString = 'programmer'
i = len(reversString) - 1

while(i >= 0 ):

    print(reversString[i], end="")
    i = i - 1
print("")







    