# list

programming_language = ['C', 'C++', 'python', 'Java', 'C#', 'Rust', 'Ruby', 'Go']

#calculate the length of the list
print(len(programming_language))

#display the element according to index
print(programming_language[1:]) #print all the element in list after index 1

#insert element in the specific index of the list
programming_language[2:2] = ['JavaScript'] #basically this add the element in index 2 of list
print(programming_language)

#delete the last element of the list
programming_language.pop()
print(programming_language)

#delete specific index value
programming_language.remove("Rust")
print(programming_language)

#add the element in list at last
programming_language.append('Flutter')
print(programming_language)

#insert in specific index
programming_language.insert(3, "React Native")
print(programming_language)

#copy function to duplicate and new reference to store the array in variable
copied_programming = programming_language.copy()
copied_programming.append("SQL")
print(copied_programming, programming_language)

#loop list comprehension 

square_num = [x**2 for x in range(1,5)]
print(square_num)
