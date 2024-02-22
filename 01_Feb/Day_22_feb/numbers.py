# Number data types in python
import math # built in math function
import random #generate random value

a = 10

a = a + a
print(a)

#floor method redundance the value after point
num1 = math.floor(2.6555)
print(type(num1))

#truncate also behave as same
num2 = math.trunc(5.8)
print(num2)


num3 = random.random()
print(num3)

# generate directly random integer value range from 1 to 5
num4 = random.randint(1, 5)
print(num4)

#if we want to get the random value from array then
#choice function is to extract a value
num5 = [32, 54, 76, 98]
randNum = random.choice(num5)
print(randNum)

#choices function is to extract value inside list
num6 = [43, 67, 32, 18, 35]
randNum2 = random.choices(num6)
print(randNum2)
print(type(randNum2))

#to operate some mathematical operation use paranthesis() to perform accurate operation
print(1+((2-1)*6))
