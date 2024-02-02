
#Multiplication
"""print("Multiplication table from 2 to 10")
for j in range(2,11):    
    for i in range(1,11):        
        table=j*i
        print(f'{j}*{i}={table}\t',end="")
    print("\n")
#Date and time
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%a"))
#Stopwatch
import turtle
import time
t=turtle.Turtle()
s=turtle.Screen()
for j in range(1):
    for i in range(1,61):

        t.pu()
        t.goto(0,0)
        t.write(j, font=("Aerial",20,"bold"))
        t.pu()
        t.goto(40,0)
        t.write(":",font=("Aerial",20,"bold"))
        t.goto(90,0)
        t.write(i, font=("Aerial",20,"bold"))
        time.sleep(1)
        s.clear()
#Rows
rows=int(input("Write the number of rows"))
for j in range(rows):
    for i in range(j):
        print("*",end=" ")
    print("*")

#1 22 333 4444 5555
for num in range(1,6):
    print("\n")
    for numb in range(num):

        print(num,end=" ")

#12345
for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")
"""
#54321
for i in range(5,-1,-1):
    for j in range(5,i,-1):
        print(j,end=" ")
    print("\n")




