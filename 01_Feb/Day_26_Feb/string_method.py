#to uppeercase the string
str = 'hello python programmer'

print(str.upper())

#capitalize the first letter of the string
print(str.capitalize())

#to capitalizee every letter after space in string
print(str.title())

str2 = "Nischal Baniya"

#to check whether the string contains space or not
print(str2.isspace())

#to cheeck the letter contains in string or not
print("s" in str2)

#join a list of string into one

joinstr = " ".join(['Hardworking', 'Determineed', 'Disciplined', 'Consistenncy'])
print(joinstr)

#count a word in paragrapgh
paragraph = "Learning programming is actually fun and make a programmer more creative. This is one of the best idea of one's if he chooses"
print(paragraph.count("is"))

#startwith and endwith

status = 'success'
print(status.startswith('s'))
print(status.endswith('s'))