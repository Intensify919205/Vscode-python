#Guess the number of candies in the jar
"""import random
r=random.randint(40,60)
for i in range(5):
    rand=int(input("Guess the number of  candies in the jar between 40 to  60 you have 5 attempts"))
    if rand==r:
        print("Congratulations! You have guessed it correctly!")
        print("The number is"+ rand)
        break
    elif rand > r:
        print("Lower")
        ra=print("Would you like to continue? (y/n)")         
        if rand == 'n':
          break
        else:
          continue
    else:
       print("Higher")"""


'''
Number Guessing Game
-------------------------------------------------------------
'''

# import random


# def show_score(attempts_list):
#     if not attempts_list:
#         print('There is currently no best score,'
#               ' it\'s yours for the taking!')

#     else:
#         print(f'The current best score is'
#               f' {min(attempts_list)} attempts')


# def start_game():
#     attempts = 0
#     rand_num = random.randint(1, 10)
#     attempts_list = []

#     print('Hello traveler! Welcome to the game of guesses!')
#     player_name = input('What is your name? ')
#     wanna_play = input(
#         f'Hi, {player_name}, would you like to play '
#         f'the guessing game? (Enter Yes/No): ')

#     if wanna_play.lower() != 'yes':
#         print('That\'s cool, Thanks!')
#         exit()
#     else:
#         show_score(attempts_list)

#     while wanna_play.lower() == 'yes':
#         try:
#             guess = int(input('Pick a number between 1 and 10: '))
#             if guess < 1 or guess > 10:
#                 raise ValueError(
#                     'Please guess a number within the given range')

#             attempts += 1

#             if guess == rand_num:
#                 attempts_list.append(attempts)
#                 print('Nice! You got it!')
#                 print(f'It took you {attempts} attempts')
#                 wanna_play = input(
#                     'Would you like to play again? (Enter Yes/No): ')
#                 if wanna_play.lower() != 'yes':
#                     print('That\'s cool, have a good one!')
#                     break
#                 else:
#                     attempts = 0
#                     rand_num = random.randint(1, 10)
#                     show_score(attempts_list)
#                     continue
#             else:
#                 if guess > rand_num:
#                     print('It\'s lower')
#                 elif guess < rand_num:
#                     print('It\'s higher')

#         except ValueError as err:
#             print('Oh no!, that is not a valid value. Try again...')
#             print(err)


# if __name__ == '__main__':
#     start_game()

#Dice game





    

 
#Leap year checker 
while True:
    
    leap=int(input("Enter the year"))
    if leap%4 ==0:
        print("The year "+  str(leap)  +" is a leap year")
        w=input("Would you like to continue? (y/n)")
        if w== 'n':
            break
        else:
            continue
    else:
        print("The year"+str(leap)+"is not a leap year")
        w=input("Would you like to continue?(y/n)")
        

