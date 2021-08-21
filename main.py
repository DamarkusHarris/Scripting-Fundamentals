# Import the random Module
import random

import attacks

gameOver = False

# added text file characters to pirates variable
pirates = attacks.char_importer()

# Here are your list of Pirates
print pirates

# PRINT THE CONTENT OF THE PIRATES LIST TO THE SCREEN HERE
print "The Pirates are " + ' '.join(pirates)

#  Attacks List
attack = ['dodge', 'parry', 'thrust']  # equivalent to rock, paper, scissors

# PRINT THE CONTENTS OF THE ATTACK LIST TO THE SCREEN HERE
print "The attacks are dodge, parry and thrust \n"

# Choosing the Characters for the fight
player = random.choice(pirates)
opponent = random.choice(pirates)

# Loop is to avoid the same character being chosen for both player and opponent.
while player == opponent:
    random.shuffle(pirates)
    opponent = random.choice(pirates)

print "Player: " + player
print "Opponent: " + opponent + "\n"

# #############################################################################
# Change the line below to correctly concatenate PLAYER and OPPONENT with
# the variables above so that when the statement prints to screen, the chosen
# character names are shown.
# #############################################################################

print "Ahoy ye swabs! Prepare for battle!"
print "PLAYER has challenged OPPONENT in one on one combat!\n"

# dodge beats parry > parry beats thrust > thrust beats dodge
while not gameOver:
    while True:
        try:
            pattack = int(raw_input("Pick an attack: [1]:Dodge [2]:Parry [3]:Thrust - "))
            if pattack <= 3:
                if pattack == 1:
                    pattack = 'dodge'
                    break
                elif pattack == 2:
                    pattack = 'parry'
                    break
                elif pattack == 3:
                    pattack = 'thrust'
                    break
        except ValueError:
            print "Please enter a valid number 1 - 3"
        else:
            print "Please enter a valid number 1 - 3"

    # Choosing the attack
    random.shuffle(attack)
    oattack = random.choice(attack)

    # To make sure the same attack is not chosen between players
    while pattack == oattack:
        random.shuffle(attack)
        oattack = random.choice(attack)

    print player + " attacks with " + pattack
    print opponent + " attacks with " + oattack

    if pattack == 'dodge' and oattack == 'parry':
        attacks.pdefeats(player, opponent)
        print player + ' defeats ' + opponent + "\n"
    elif pattack == 'parry' and oattack == 'thrust':
        attacks.pdefeats(player, opponent)
        print player + ' defeats ' + opponent + "\n"
    elif pattack == 'thrust' and oattack == 'dodge':
        attacks.pdefeats(player, opponent)
        print player + ' defeats ' + opponent + "\n"
    elif oattack == 'dodge' and pattack == 'parry':
        attacks.odefeats(opponent, opponent)
        print opponent + ' defeats ' + player + "\n"
    elif oattack == 'parry' and pattack == 'thrust':
        attacks.odefeats(opponent, opponent)
        print opponent + ' defeats ' + player + "\n"
    elif oattack == 'thrust' and pattack == 'dodge':
        attacks.odefeats(opponent, opponent)
        print opponent + ' defeats ' + player + "\n"




