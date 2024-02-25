import types

class CheckUp:

    def __init__(self, cookie_function):
        self.cookie_function = cookie_function

    def __call__(self, *args, **kwargs):
        print(args)

        response = self.cookie_function(*args)

        if(response):
            self.cookie_function(**kwargs)

        return response
    
@CheckUp

def cookie(returnVal):
    print(returnVal)

def login(**kwargs):
    email = kwargs.get('email')
    password = kwargs.get('password')

    print(email, password)

    if(email == 'abc@gmail.com' and password == 'pass'):
        print('Login Successfull')

    else:
        print('Login Failed')

    
cookie('xfsdfsdfdgdfg34445')
login(email = 'abc@gmail.com', password = 'pass')
