# function to accept the tuple or multiple arguement as parameter

#the parameter should be namecase by *args
def addition(*args): 

    return sum(args)
    

num_addition = addition(1,2,3)
print(num_addition)

#function to accept the optional parameter

def optional_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

optional_function(name=['ram', 'shyam'], position="Full stack")
optional_function(name="Hari")