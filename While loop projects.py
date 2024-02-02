#Miles
"""mile=0
while mile>0:
    print("Are u there?")
    print("Not yet")
    mile=mile-5
    print("I am",mile,"miles away")
print("I have reached")

#Elections
T=0
G=0
vote=True
while vote== True:
  vote=input("Enter your vote for Mr Trump by pressing T or Give your vote to Mr Grump by pressing 6:").upper()
  
  if vote=="T":
    
    T=T+1
  elif vote=="6":
    G=G+1
  else:
    break
print("Total votes for Mr Trump:",T)
print("Total votes for Mr Grump:",G)
if T>G:
  print("Mr Trump has won the election by",T-G,"votes")
else:
  print("Mr Grump has won the election by",G-T,"votes")
#Potato Race
po=0
while po<10:
    
  p=input("Did you successfully deposited the potato or it felldown?")
  if p=="deposited":
    print("You deposited the potato.")
    po=po+1
    print(po)
  elif p=="felldown":
    print("potato felldown.")
    continue
print("Congratulations! You have completed the potato race!!!!!")   
#distance
while True:   
  d=int(input("Enter distance in kms: "))
  if d < 0:    
    print("Distance cannot be negative")
    d=int(input("Enter distance in kms: "))
  else:     
   continue
  t=int(input("Enter time it took u to cover the distance in mins:"))
  speed=d/t
  print(d)
  print(t)    
  print("Your speed is",speed)"""
#list of guests
list=[]
cont="y"
while cont =="y":
  
  name=str(input("Enter The Guest Name:"))
  list.append(name)
  cont=input("Would you like to continue? (y/n)")
    
  print(name)
  if cont== 'n':
    break
  else:
    continue




    
