#reversing thee string

string_original = 'Code everyday' #string to be reversed
# string_length = len(string_original)-1 #determine the length of the string
# string_reverse = "" #declare the empty string first

# while(string_length >= 0):
#     string_reverse = string_reverse + string_original[string_length]
#     string_length = string_length - 1

# print(string_reverse)

number = 3456 # '3456'

numtostr = str(number)
numlength = len(numtostr) - 1
numreverse = ''

while(numlength >= 0):
    numreverse = numreverse + numtostr[numlength]
    numlength = numlength - 1

finalreverse = int(numreverse)
print(finalreverse, type(finalreverse))

# print(numtostr[1])
