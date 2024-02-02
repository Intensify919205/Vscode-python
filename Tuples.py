#Tupel

"""Center_a = ()
Center_b = ()
Center_c = ()
a=b=c=1000
noA = int(input("Enter the number of participants in center A:  "))
noB = int(input("Enter the number of participants in center B:  "))
noC = int(input("Enter the number of participants in center C:  "))
for i in range(noA):
    regid = 'A'+str(a)
    Center_a+=(regid , )
    a+=1
for i in range(noB):
    regid = 'B'+str(b)
    Center_b+=(regid , )
    b+=1
for i in range(noC):
    regid = 'C'+str(c)
    Center_c+=(regid , )
    c+=1
print(Center_a)
print(Center_b)
print(Center_c)
print("Last 3 id of center_A are:  ")
print(Center_a[len(Center_a):3:-1])
print("Last 2 id of center_B are:  ")
print(Center_b[len(Center_b):-3:-1])
print("From the second till last of center_C are :")
print(Center_c[2::1])
print(Center_a[::2])
print(Center_b[::2])
print(Center_c[::2])

t1 = (2323,)
t2 = (131313,)
print(t1+t2)
print(type(t1))
print(type(t2))"""

# Birthday game

import random
print("************************LUCKY DRAW!!!**************************")
print("*********************BIRTHDAY PARTY GAME!!!******************** \n")
student_name=()
coupon_number = ()
cont = 'y'
while cont == 'y':
    name = input("Enter your name:  ")
    number = random.randint(1,25)
    print(f'Generated coupon number for {name} is {number}')
    student_name+=(name,)
    coupon_number+=(number, )
    cont = input("Do you want to continue??? (y/n)")

winner = random.randint(0,len(coupon_number)-1)
print(f'The LUCKY DRAW winner is {coupon_number[winner]}\n {student_name[winner]} is the winner')



