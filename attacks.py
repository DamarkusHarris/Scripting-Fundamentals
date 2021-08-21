import sys

pscore = 0
oscore = 0


def char_importer():
    with open('characters', 'r') as f:
        return f.read().splitlines()


# If player beats opponent in attack
def pdefeats(player, opp):
    global pscore
    global oscore

    pscore += 1
    print "Player: " + str(pscore)
    print "Opponent: " + str(oscore)
    check_winner(player, opp)
    print "---------------------------------------"


# If opponent beats player in attack
def odefeats(player, opp):
    global pscore
    global oscore

    oscore += 1
    print "Player: " + str(pscore)
    print "Opponent: " + str(oscore)
    check_winner(player, opp)
    print "---------------------------------------"


# Game Over logic if player or opponent score is 3
def check_winner(player, opp):
    if pscore == 3:
        print "\n The Player " + player + " WON!"
        sys.exit()
    elif oscore == 3:
        print "\n The Opponent " + opp + " WON!"
        sys.exit()


