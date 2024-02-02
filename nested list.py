#Marks

name = ['ben' , 'riya' , 'diya']
"""marks = [[100,100,100,100,100] , [99,99,99,99,99] , [98,98,98,98,98]]
subjects = ['phy' , 'chem' , 'math' , 'sci' , 'comp']
for i in range(3):
    print("Name:  " ,name[i])
    for j in range(5):
        print(subjects[j] , marks[i][j])
#Change marks
name_d = int(input("Choose the student whose marks you want to change:   (0-ben , 1-riya , 2-diya)"))
subjet_d = int(input("Choose the subject:    (0-phy , 1-chem , 2-math , 3-sci , 4-comp)"))
updated_marks = int(input("Enter the new marks:      "))
marks[name_d][subjet_d] = updated_marks
for i in range(3):
    print("Name:  " ,name[i])
    for j in range(5):
        print(subjects[j] , marks[i][j])
#transpose matrix
matrix = [[6,9] , [3,4] , [2,7]]
for i in range(3):
    for j in range(2):
        print(matrix[i],[j] , "   " , end = '  ')
    print('\n')
for j in range(2):
    for i in range(3):
        print(matrix[i][j] , '  ' , end = '  ')
    print("\n")
#transpose marks
marks = [[100,100,100,100,100] , [99,99,99,99,99] , [98,98,98,98,98]]
subjects = ['phy' , 'chem' , 'math' , 'sci' , 'comp']
for i in range(3):
    total = 0
    print(subjects[i])
    for j in range(5):
        total += marks[i][j]
        print(marks[i][j] , '   ' , end = '   ')
    avg = total/3
    print(avg)
#Ragged list
Rhyme = []
students = int(input("Enter the number of students:   "))
for i in range(students):
    w = int(input("Enter the number of rhyming words: "))
    for j in range(w):
        word = input("Enter the word:   ")
        Rhyme.append(word)
print(Rhyme)
#Volunteers
count = 0
Volunteers = ['Anil' , 'Meg' , 'Ravi' , 'Ramesh']
Available_dates = [[12,13] , [12,14,16] , [13,16,19,20] , [14,15,17,19,21]]
for i in range(len(Available_dates)):
    if(len(Available_dates[i])>count):
        count = len(Available_dates[i])
        name = Volunteers[i]
print(Volunteers)
print(Available_dates)
print(f'{name} is ready to serve for maximum days')
#Volunteers between 15 and 20
for i in range(len(Available_dates)):
    for j in range(len(Available_dates[i])):
        if Available_dates[i][j] >= 15 and Available_dates[i][j] <=20:
            print(f'{Volunteers[i]} \t {Available_dates[i][j]} ')
            count +=1
print(f'Volunteers who are available between 15 and 20 are:    {count} ')"""
#Heterogenous
list = [['Anna' , 'Percy' , 'Nick' , 'Leo'] ,[14,15,10,13] , ['Female' , 'Male' , 'Male' , 'Male']]
donate = []
for i in range(4):
    donation = int(input('Enter 1-Food , 2-Games , 3-Money , 4-Toys:  '))
    if donation == 1:
        a = input("Enter the food item you want to donate:  ")
        donate.append(a)
    elif donation == 2:
        a = input("Enter the game  you want to donate:  ")
        donate.append(a) 
    elif donation == 3:
        a = input("Enter the amount of money you want to donate:  ")
        donate.append(a) 
    elif donation == 4:
        a = input("Enter the toy  you want to donate:  ")
        donate.append(a) 
for i in range(4):
    print(f'{list[0][i]}  donated {donate[i]}')

#Heterogenous
"""list=[['Anna','Olivia','Marry','kevin','Nick'],[8,5,7,6,10],['female','female','female','male','male']]
m=[]
for i in range(5):
    donation=int(input('Enter 1-food, 2- Money, 3-Toys, 4-Books: '))
    if donation==1:
       f=input('Enter the food item you wish to donate:')
       m.append(f)
    elif donation==2:
       f=input('Enter the Money you wish to donate:')
       m.append(f)
    elif donation==3:
        f=input('Enter the toy item you wish to donate:')
        m.append(f)
    elif donation==4:
        f=input('Enter the book item you wish to donate:')
        m.append(f)
for i in range(5):
    print(f'{list[0][i]}  donated  {m[i]}')
print('Display all children whose age is less than 7')
for j in range(len(list[1])):
    if list[1][j]<7:
        print(f'{list[0][j]} \t {list[1][j]}')"""


