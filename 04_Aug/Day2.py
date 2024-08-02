#lambda function : anonymonous function

greeting = lambda x : 'Hello' + x

print(greeting('nischal'))

#loop

for i in range(0, 12):
    print(f'{i} Hello Friend')


def divide(a, b):
    try:
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
    except TypeError:
        return "Invalid input types"

result = divide(10, 0)
print(result)