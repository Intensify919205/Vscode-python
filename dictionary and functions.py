"""#total matches of players
matches={"Virat Kohli": "25","Rohit Sharma": "30","M.S Dhoni": "60", "Hardik Pandya": "20"}
print(matches)
print(matches["Hardik Pandya"])
matches["Ravindra Jadeja"]="40"
print(matches)
matches["M.S Dhoni"]="55"
print(matches)
del matches["Ravindra Jadeja"]
print(matches)
#Harry potter hobby
HarryPotterHobby={"Harry Potter": "Playing Quidditch", "Ron Weasley": "Playing Wizard Chess","Hermione Granger": "Studying"}
print(HarryPotterHobby)
print(HarryPotterHobby.keys())
print(HarryPotterHobby.values())
if "Albus Dumbledore" in HarryPotterHobby:
    print(HarryPotterHobby["Albus Dumbledore"])
else:
    print("I Dont Know")
#happy birthday
def birthday(name):
    print("Happy Birthday",name)
birthday("Vihaan")
#have a lovely day
def day(name):
    print("Have a lovely day",name)
day("Vihaan")
#repeating song if yo
def song(lyrics):
    print("If you're happy and you know it  "  +lyrics)
    print("If you're happy and you know it  "  +lyrics)
    print("If you're happy and you know it and you really want to show it"   +lyrics)
    print("If you're happy and you know it "  +lyrics)
song("clap your hands")
song("stom your feet")
song("shout hurray (hurray)")
song("do all three (hurray) ")"""
#animals
"""cat={"name":"Cutie", "Gender":"Female","age":2, "weight":5, "hungry":True, "photo":"=^'^="}
rat = {'name':'MrFatRat', 'weight': 3, 'age':2, 'hungry':True, 'photo':'<:3 )~~~~', 'healthyWt':5}
bat = {'name':'Bat-tery', 'weight': 2, 'age':64, 'hungry':True, 'photo':'\_(ツ)_/¯', 'healthyWt':1.5 }
print('Hi, let\'s meet the pets')
print('These are your pets')
print('This is a rat')
print(rat)
print('\n This is a cat')
print(cat)
print('\n This is a bat')
print(bat)
def play(pet):
  print('\nPlaying with ' + pet['name'])
  pet['weight'] = pet['weight']- 1
  pet['hungry'] = True

def sleep(pet):
  print('\n'+pet['name'] + ' is sleeping')
  print (pet['name'] + ': ZZZZZ')
  pet['weight'] = pet['weight']- 1
  pet['hungry'] = True
def feed(pet):
  print('\n '+pet['name']+'is feeding')
  print(pet['name']+': chabchabchab')
  pet['weight']+=1
  pet['hungry']= False
sleep(bat)
play(cat)
feed(rat)
print(rat)
"""# tables
def tables(number):
    print("Multiplication Table Of", str(number))
    for i in range(1,11):
        print(str(number)+'x'+ str(i) + '=' + str(number * i ))
tables(162)
#Calculator Using Functions
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("This is a Simple Calculator")
print("Press 1. to add , 2. to subtract , 3. Multiplication , 4. Division , 5. Break")
while True:
    choice=int(input("What operation you want?"))
    if choice==5:
        print("Bye Bye")
        break
    else:
        num1=int(input("Enter the first number"))
        num2=int(input("Enter the second number"))
        if choice==1:
            s=sum(num1,num2)
            print(s)
        elif choice==2:
            t=sub(num1,num2)
            print(t)
        elif choice==3:
            m=mul(num1,num2)
            print(m)

        elif choice==4:
            d=div(num1,num2)
            print(d)
