import os

from player_turn import player_turn
from random import randint
from scoreprompt import scoreprompt
from hide_check import hide_check
from time import sleep
from newturn import new_turn


winningFloor = randint(1, 10)
if winningFloor == 1:
    p1Position = winningFloor + 1
else:
    p1Position = winningFloor - 1
p2Position = randint(1, 3)
takenTurns = False
wonGame = False
currentTurn = 1
p1HiddenStatus = False
p2HiddenStatus = False
score = [0, 0]
winAmount = 5

print('Welcome to Floor War.\n')
sleep(1)
print('Player 1, please enter your name.')
p1 = input()
print('Player 2, please enter your name.')
p2 = input()
print('Loading...')
sleep(2)

while wonGame is False:
    while takenTurns is False:
        if currentTurn == 1:
            new_turn(p1)
            print(p1 + ': You must stop ' + p2 + ' from getting to floor ' + str(winningFloor) + '.')
            hide_result = hide_check(p1Position, p2Position, p1HiddenStatus, p2HiddenStatus, currentTurn, p1, p2)
            p1update = player_turn(p1Position, p1HiddenStatus)
            hide_result = hide_check(p1Position, p2Position, p1HiddenStatus, p2HiddenStatus, currentTurn, p1, p2)
            if p1update is True:
                p1HiddenStatus = True
            else:
                p1Position = p1update
            if hide_result is True:
                print(p1, 'wins the round.')
                score[0] = score[0] + 1
                scoreprompt(score, p1, p2)
                wonGame = True
            currentTurn = 2
            break
        elif currentTurn == 2:
            new_turn(p2)
            print(p2 + ':')
            hide_result = hide_check(p1Position, p2Position, p1HiddenStatus, p2HiddenStatus, currentTurn, p1, p2)
            p2update = player_turn(p2Position, p2HiddenStatus)
            hide_result = hide_check(p1Position, p2Position, p1HiddenStatus, p2HiddenStatus, currentTurn, p1, p2)
            if p2update is True:
                p2HiddenStatus = True
            else:
                p2Position = p2update
            if p2Position == winningFloor:
                print(p2, 'wins the round.')
                score[1] = score[1] + 1
                scoreprompt(score, p1, p2)
                wonGame = True
            if hide_check is True:
                print(p2, 'wins the round.')
                score[1] = score[1] + 1
                scoreprompt(score, p1, p2)
                wonGame = True
            currentTurn = 1
            break
while wonGame is True:
    if score[0] < winAmount or score[1] < winAmount:
        scoreprompt(score, p1, p2)
        print('Next round starting in 5 seconds.')
        sleep(5)
        wonGame = False
    else:
        if score[0] >= winAmount:
            print(p1, 'won the game!')
        elif score[1] >= winAmount:
            print(p2, 'won the game!')


