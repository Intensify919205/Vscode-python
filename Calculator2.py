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