#scope is the concept where there is availability of the reference of the variable or other in the form of global or inside scope block

global_variable = 'This is the global variable which can access from any scope inside this file'


def scope1():
    #This variable is acces to only this scope or futher inside of this scope
    scope1_var = 'scope 1 variable'
    print(f"From scope1: {global_variable}")
    print(f"{scope1_var}")

scope1()

def scope2():

    #This variable can be access further inside another scope but not outside or another from the scope
    scope2_var = 'scope 2 variable'
    def inner_scope2():
        print(F"\nFrom inner of second scope: {global_variable}")

        print(f"\n{scope2_var}")

    inner_scope2()

scope2()