#checking whether the string is palindrome or not

original_string = 'popp'

string_length = len(original_string) - 1
reverse_string = ""

while(string_length >= 0):
    reverse_string = reverse_string + original_string[string_length]

    string_length -= 1

if(original_string == reverse_string):
    print(f'{original_string} is a palindrome string')
else:
    print(f'{original_string} is not palindrome number')



array = [12,43,54,58,98,66]
swap = 3

array.append(None)  # Add an extra element at the end to avoid losing the last element

for i in range(len(array) - 1, swap, -1):
    array[i] = array[i - 1]

array[swap] = 10

print(f'After adding data: {array}')
