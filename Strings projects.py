"""id = ["a-76274" , "b-37247" , "g-23794" , "i-3793" , "r-385656469","a-73434574" , "b-3232726727" , "g-2455234794" , "i-334793""g-24563794" , "i-377293" , "r-382378","a-735435" , "b-3726726877" , "g-2234794" ]
print(id)
list = []
for i in range(len(id)):
    list.append(id[i][0])
print(list)
print("The number of employes in department a are:",list.count("a"))
print("The number of employes in department b are:",list.count("b"))
print("The number of employes in department g are:",list.count("g"))
print("The number of employes in department i are:",list.count("i"))
print("The number of employes in department r are:",list.count("r"))

x = 'Who said that,"I am scared of this ride"'
print(len(x))#Tells total number of words used in the line or paragraph
print(x[4])# Tells which word is in 4th position(starting from 0)   
print(x.capitalize())#To capitalize
print(x.replace("I","you"))#To replace a word with another
print(x.lower())#Lower's all the words
print(x.upper())#Capitalizes all the words
print(x.count("I"))#Tells how many times a particular word has been used
print(x.title())#Capitalizes  the first letter word of all the words in the paragraph
print(x.index("r"))#Tells the position of the alphabet
print(x[4:30:5])#tells all he words between 4 and 30 while skipping 5 words
print(s.split(" "))#Makes space between the words


#Palindrome
while True:
    word = input("Enter the word:  ")
    flip = word[::-1]
    if word == flip:
        print("It is a Palindrome")
        print(flip)
    else:
        print("It is not a Palindrome")
        print(flip)
    cont = input("Do you want to continue (yes/no)")
    if cont == "yes":
        continue
    else:
        break

#piglitan language
w = input("Enter the your name")
vowels = ['a' , 'e' , 'i' , 'o' , 'u']
for i in range(len(w)):
    if w[i] in vowels:
        if i == 0:
            n = w+"way"
            print(n)
            break
        else:
            n = w[i:]+w[0:i]+"ay"
            print(n)
            break
# ..
text = input("Enter text:    ")
for i in range(len(text)):
    for j in range(i+1):
       print(text[j] , end = "  ")
    print("\n")
#
guests = "'jenny brown' , 'mini singh' , 'tarun vaidya' , 'zoya amir' , 'martin smith' , 'tina sharma' , 'gita rao' , 'jenny lobo'"     
print(guests)
print(guests.title())
#Find the animal
print("Lets play find the animal game !!!!")
choose = input(Which place you want to choose?)
                        Mountains
                        Jungle
                        Hills
                        Plains )
while True:
#Mountain
    if choose == 'Mountains':
       Mountain = 'ugwqbvsmcsnwghjagwggbeargwggeggoattuwnydahhhetywkqweaglelqyygdwqdgggwjgfggkqkfalconnjqjudhquduufvwqyivgdgghwgakcgorillaqhjdhbjqjd'
       print(Mountain)
       result = Mountain
       guess1 = input("Find all of the Mountain animals in this word :   (Hint:Total 5 animals)")
       if guess1 in Mountain:
          result = result.replace(guess1 ,"*" *len(guess1))
          cont1 = input("Congratulations! you have got it right! Do you want to continue and find other animals??(y/n)")
          if cont1 == 'y':
             continue
          else:
             break
       else:    
            print("Sorry you have got it wrong Pls try again")
            break
#Jungle
    elif choose == 'Jungle':
       Jungle = 'jgqwdvkgwhdldgswywiiqovlionwqgagkgsgdwquftasvsdfugukqkjaguaryoqulwdbhgtigerguqwgwkkqwdvqgmonkeyqwdgjqgwdfmmmmhqdkqwelqwlekeelephantttygqgghke'
       print(Jungle)
       guess2 = input("Find all of the Jungle animals in this word :   (Hint:Total 5 animals)")
       result=Jungle
       if guess2 in Jungle:
          result = result.replace(guess2 , "*"*len(guess2))
          cont2 = input("Congratulations! you have got it right! Do you want to continue and find other animals??(y/n)")
          if cont2 == 'y':
             continue
          else:
             break
       else:

          print("Sorry you have got it wrong Pls try again")
          break
#Hills
    elif choose == 'Hills':
       Hills = 'gqweuwhgegkwkeghghdigusukbasnowleopardgjqgjkgjdkwgku3gggaggkdwkkwpandagwqgdqkdkgqgwgdwgqjkfqakfoxhhqgdjqgwdqwoldkwgadvfqgjdgqsheepwqgdvgoooppp'
       print(Hills)
       guess3 = input("Find all of the Hill animals in this word :   (Hint:Total 5 animals)")
       result=Hills
       if guess3 in Hills:
          result = result.replace(guess3 ,"*" *len(guess3))
          cont3 = input("Congratulations! you have got it right! Do you want to continue and find other animals??(y/n)")
          if cont3 == 'y':
             continue
          else:
             break
       else:

           print("Sorry you have got it wrong Pls try again")
           break
#Plains
    elif choose == 'Plains':
         Plains = 'hqwhdhqkwqvwdvqhvdhwvhvvhjdeerwgqdgqwhvdqwjqgacatsoqwuddogqhkehwqgdelkrabbitsgqwgydgkwqjdqgf'
         print(Plains)
         guess4 = input("Find all of the Hill animals in this word :   (Hint:Total 5 animals)")
         result=Plains
         if guess4 in Plains:
            result = result.replace(guess4 , *len(guess4))
            cont4 = input("Congratulations! you have got it right! Do you want to continue and find other animals??(y/n)")
            if cont4 == 'y':
               continue
            else:
               break
         else:
            print("Sorry you have got it wrong Pls try again")
            break     """
#Encryption and Decryption
import random 
code = {'a':'4' , 'b':'l' , 'c':'3' , 'd':'x' , 'e':'f' , 'f':'8' , 'g':'v' , 'h':'q' , 'i':'m' , 'j':'k' , 'k':'g' , 'l':'z' , 'm':'9' , 'n':'1' , 'o':'6' , 'p':'n' , 'q':'v' , 'r':'p' , 's':'u' , 't':'y' , 'u':'5' , 'v':'0' , 'w':'2' , 'x':'s' , 'y':'7' , 'z':'b'}
codelist = code.keys()
def encryptedcode(v):
     v=v.lower()
     for i in range(len(v)):
         if v[i] in codelist:
             v=v.replace(v[i] , code [v[i]])
         rnum = random.randint(33 , 47)
         ch = chr(rnum)
         codeword = v+ch+ch+ch
         codeword = codeword.capitalize()
     return codeword
#Decrypted
dcode = {'4':'a' , 'l':'b' , '3':'c' , 'x':'d' , 'f':'e' , '8':'f' , 'v':'g' , 'q':'h' , 'm':'i' , 'k':'j' , 'g':'k' , 'z':'l' , '9':'m' , '1':'n' , '6':'o' , 'n':'p' , 'a':'q' , 'p':'r' , 'u':'s' , 'y':'t' , '5':'u' , '0':'v' , '2':'w' , 's':'x' , '7':'y' , 'b':'z'}
dcodelist = code.values()
def Decryptedcode(va):
    va = va.lower()
    for j in range(len(va)):
        if va[j] in dcodelist:
            va = va.replace(va[j] , dcode [va[j]])
    va=va[:-3]
    dcodeword = va
    return dcodeword
print("************************************** Enigma ********************************************")
inp = input("Enter the word:  ")
print("Your encoded word is:     " +encryptedcode(inp))
inp = input("Enter the encrypted word:  ")
print("Your decoded word is :   " + Decryptedcode(inp))


            
    

     
     


