import random
import sys

# One = Rock | Two = Paper | Three = Scissors

gen = random.randint(1, 3)
tracker = 0
chance = 3

print('''

####################################
#   Rock-Paper-Scissors            #
####################################

Winner takes it all you have 3 chances

Use R for Rock | P for Paper | S for Scissors 

''')

while chance > 0:

    choice = str(input('Choice: '))

    if choice == 'p' or choice == 'P':
        if gen == 1:
            print('You : Paper | Computer : Rock')
            print('Congrats Bruh . You won !')
            tracker += 1
        elif gen == 2:
            print('You : Paper | Computer : Paper')
            print('Uhh huh. Its a tie')
            tracker = tracker
        elif gen == 3:
            print('You : Paper | Computer : Scissors')
            print('You lose u noob')
            tracker -= 1
        else:
            print('Please make a valid choice')

    elif choice == 'r' or choice == 'R':
        if gen == 1:
            print('You : Rock | Computer : Rock')
            print('Uhh huh. Its a tie')
            tracker = tracker
        elif gen == 2:
            print('You : Rock | Computer : Paper')
            print('You lose u noob')
            tracker -= 1
        elif gen == 3:
            print('You : Rock | Computer : Scissors')
            print('Congrats Bruh . You won !')
            tracker += 1
        else:
            print('Please make a valid choice')

    elif choice == 'S' or choice == 's':
        if gen == 1:
            print('You : Scissors | Computer : Rock')
            print('You lose u noob')
            tracker -= 1
        elif gen == 2:
            print('You : Scissors | Computer : Paper')
            print('Congrats Bruh . You won !')
            tracker += 1
        elif gen == 3:
            print('You : Scissors | Computer : Scissors')
            print('Uhh huh. Its a tie')
            tracker = tracker
        else:
            print('Please make a valid choice')
    else:
        print('Something went worng please try later')
        sys.exit()

    chance  = chance - 1

    if chance == 0:
        break

if tracker > 2:
        print('''

                      You
           Computer |--------|      You won the game !!!!!!
        |-----------| First  |
            Loser
        ''')
elif tracker == 2 or tracker == 0:
    print(''' 
            
            Computer            You
        |-------------------|---------------------|     Its a tie man !
        
    ''')
elif tracker < 2 or tracker == 0:
    print(''' 
        
                     Computer
           First    |--------|      You lose the game bruh !!!!!!
        |-----------| First  |
            Loser
        
    ''')
else:
    print('Something went worng !')
    sys.exit()