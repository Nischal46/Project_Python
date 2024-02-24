
def scope1(inp):

    def scope2():
        return 'Hello ' + inp
    
    return scope2

input1 = scope1('nischal')
print(input1())
