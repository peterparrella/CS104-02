#Peter Parrella
#Average.py
average=0
total=0
howManyEntered=0
howMany= int(input('How many Test Scores do you want to enter?'))
while howManyEntered<howMany:
    testscore= int(input('Enter Test Scores'))
    total=total+testscore
    howManyEntered=howManyEntered+1
average=total/howMany
print('The average for the test scores you entered is')
print(average)
