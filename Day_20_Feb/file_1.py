# here we define the function and import from the main file

#simple greeting message function
def greeting():
    print(f"Learning python you can have a wider scope.\n1)Machine Learning\n2)Web Development")

#defining function that run the loop
def calculationLoop():
    print("Loop Begins")
    for i in range(0,5):
        print(f"Number printed is {i}")

#defining function that accepts the parameter
def calculator(num1, num2, option):

    if(option == "add"):
        add = num1 + num2
        print(f"The sum of {num1} and {num2} is {add}")
    
    elif (option == "subtract"):
        subtract = num1 - num2
        print(f"The subtract of {num1} and {num2} is {subtract}")

    elif (option == "multiply"):
        multiply = num1 * num2
        print(F"The multiplication of {num1} and {num2} is {multiply}")

    elif (option == "divide"):
        divide = num1 / num2
        print(f"The division of {num1} and {num2} is {divide}")

    else:
        print("Invalid option provided")