import heapq

#heapq is the function use for different purpose

numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]

#finding the largest data of list
highest = (heapq.nlargest(4, numbers))
print(f"Largest data from {numbers} is {highest}")

#finding the smallest data of list
smallest = heapq.nsmallest(2, numbers)
print(f"Smallest data from {numbers} is {smallest}")

#in case of array
people = [
    {'name': 'Nischal Baniya', 'email': 'nisalbaniya@gmail.com', 'age': 24},
    {'name': 'Bibek Baniya', 'email': 'bibekbaniya@gmail.com', 'age': 28},
    {'name': 'David Baniya', 'email': 'david@gmail.com', 'age': 21}
]

eldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(eldest)

#filter method

stdetails = list(filter(lambda x: x['email'] == 'nisalbaniya@gmail.com', people))
print(f"Filter using email: {stdetails}")