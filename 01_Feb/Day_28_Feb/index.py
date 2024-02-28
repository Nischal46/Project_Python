#some of the useful string method in python

name = 'Ram Bahadur'

#iterate each character using loop

for character in name:
    if(character == " "):
        print("--")
    else:
        print(character)

#reverse the string

original_string = 'I am a core programmer'
count = len(original_string) - 1
reverse_string = ""

while(count >= 0):
    print(original_string[count], end="")
    count -= 1

