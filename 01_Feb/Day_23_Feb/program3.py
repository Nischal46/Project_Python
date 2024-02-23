#Grade Calculator Program

score = int(input("Enter a score of your subject marks: "))

if(score > 100):
    print('Please enter a valid marks range from 0 to 100')
    exit()

grade = 'E' if score < 60 else 'D' if score < 70 else 'C' if score < 80 else 'B' if score < 90 else 'A' 

print(f"You had score {score} marks and you had got {grade} grade. Congratulations")