#mod(even or odd)
number=int(input("Enter the number:"))
if number%2 == 0:
  print("The number is even")
else:
  print("The number is odd")
if number%2 == 1:
  print("The number is odd")
else:
  print("The number is even")

#Rows of stars
rows=int(input("Write number of rows:"))
for i in range(rows):
  print("*"*i)
#Tables
table=int(input("What number table you want?"))
for i in range(1,11):

    print(i*table)

#age
age=int(input("What is you age????"))
if age >=18 and age <=30:
  print("You can focus on ur goal and can achieve it")
elif age <18:
  print("You are still learning")
elif age >=30 and age <=60:
  print("You are already settled enjoy your life")
else: print("You can take rest and take care of your self")

#Time
time=int(input("Write the time in 24 hours format"))
if time >=8 and time <=11:
  print("Good Morning")
elif time == 12:
  print("Good Noon")
elif time >12 and time <=15:
  print("Good Afternoon")
elif time >15 and time <=19:
  print("Good Evening")
else: print("Good Night")

#Calculator
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
op=input("Enter an operator")
if op == "+" or op == "add":
  print(num1+num2)
elif op == "-" or op == "sub":
  print(num1-num2)
elif op == "/" or op == "div":
  print(num1/num2)
elif op == "*" or op == "mul":
  print(num1*num2)
else: print("Sorry its a simple calculator")
for i in range(1,11):
    print(i)
for j in range(10,0,-1):
    print(j)
sum=0
for k in range(1,11):
    sum=sum+k
    print(sum)


#Tables of two numbers
table=int(input("What number table you want?"))
numoftab=int(input("How many times you want to multiply?"))
for i in range(1,numoftab+1):
    print(i*table)






#Python program to write the odd numbers between two given numbers
"""n1=int(input("Write the first number"))
n2=int(input("Write the second number"))
for i in range(n1+1,n2):
    if i%2 !=0:
        print(i)"""
#Python program to write the even numbers between two given numbers
n1=int(input("Write the first number"))
n2=int(input("Write the second number"))
for i in range(n1,n2):                                            
    if i%2 ==0:                           #amount=0.50*units
        print(i)                                         #additional=amount*(20/100)
                                                         #print("Units\t amount \t total*")
                   #print(str(unit)+"\t"+str(amount))+"\t"+str(additional))+"\t"+str(total))
#Electricity Bill
unit=int(input("Enter your electricity bill:"))
if unit <=100:
    amount = 0.50*unit
    additional=amount*(20/100)
    total=amount+additional
elif unit >=100 and unit <=250:

    amount = 1.20*unit
    additional=amount*(20/100)
    total=amount+additional
elif unit >=250:
    amount = 1.50*unit
    additional=amount*(20/100)
    total=amount+total
print("*******************Electricity Bill******************")
print("Unit:",unit)
print("Additional Amount:",additional)
print("Amount:",amount)
print("Total:",total)

    
