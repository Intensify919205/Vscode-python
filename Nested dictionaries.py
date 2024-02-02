details = {"Benz": {'Car': 'Mercedes' ,'Model': 'Benz' , 'Price': '99999999$' } , "BMWx9": {'Car': 'BMW' , 'Model': 'X9' , 'Price': '1000000000$'}}
print(details)
print(details['Benz'])
print(details['BMWx9'])
#Tupel

Center_a = ()
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