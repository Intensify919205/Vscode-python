GameOn = True
num=0
while gameOn:
    if num == 5:
        GameOn = False
    num = num+1
    print(num)
    if GameOn == False:
        break

x = int(input("Enter the number"))
y = int(input("Enter the second number"))
z = x
x = y
y = z
print(x)
print(y)