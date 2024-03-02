#reversing thee string

string_original = 'Code everyday'
string_length = len(string_original)-1
string_reverse = ""

while(string_length >= 0):
    string_reverse = string_reverse + string_original[string_length]
    string_length = string_length - 1

print(string_reverse)
