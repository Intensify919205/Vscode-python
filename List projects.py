#Cricket
"""list = []
list = ["Virat Kohli" , "M.S Dhoni" , "Sachin Tendulkar"]
print(list)
list.append("jad")
print(list)
print(len(list))
list.extend(["Rohit Sharma" , "Jadi" , "gad"])
print(list)
list.remove("Virat Kohli")
print(list)
list.clear()
print(list)"""
#Avengers
"""list = []
list = ["Iron Man" , "Captain America" , "Thor" , "Hulk" , "Black Panther"]
print(list)
print(len(list))
list.append("Doctor Strange")
print(list)
list.extend(["Peter Quill" , "Gamora" , "Scarlet"])
print(list)
print(len(list))
list.extend(["Vision" , "Doctor Panther" , "Drakes" , "Grout" , "Rocket" , "Doctor Strange"])
print(list)
print(len(list))
list.remove("Doctor Strange")
print(list)
print(len(list))
list.sort()
print(list)"""
#Ages
ages = [12 , 3 , 4 , 23 , 18 , 11 , 20 , 14 , 10 , 13]
print(ages)
print(max(ages))#What is the maximum age?
print(min(ages))#What is the minimum age?
ages.sort()#Sort in ascending order
print(ages)
ages.sort(reverse = True)#Sort in descending order
print(ages)
print(sum(ages))#Sum of the ages
if 3 in ages:
    print("it is in the list")
else:
    print("Its not in the list")

print(ages.count(11))
print(ages[0])
print(ages[1:5])
ages.insert(4 , 69)
print(ages)
del ages[5]
print(ages)
#Ages 2
name = ["Bin" , "Jack" , "Tim"]
age = [34,36,92,76,65,69,10,2,34,35,45,44,23,76,97,43,67,56,46,42]
age.sort()
for i in ages:
    print(i)