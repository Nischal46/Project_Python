# def secret_fn(f):
#     print('Hello there')
#     print(type(f))
#     return f

# #in order to access the main function we must return the decorator function and then the main function will call

# @secret_fn
# def secondary_fn():
#     print('This is decorator concept')


# secondary_fn()


#defining the decorator function

def print_num_args(fun):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)

        return fun(*args, **kwargs)
    print('Here')
    return inner_func

@print_num_args
def multiply(num1, num2):
    return num1 * num2

print(multiply(4,6))

@print_num_args
def key_val(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    return "kwargs function concept"

print(key_val(x = 4, y = 6))

print(key_val(name = 'Nischal', drivingLicense = True, citizen = 'Nepali'))
