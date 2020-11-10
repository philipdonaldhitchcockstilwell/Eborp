# from getch import getch
# import os
# import pygame
# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_RIGHT,
# )
# pygame.init()

def player_turn(playerPosition, hiddenStatus):
    print('You are on floor', playerPosition, '\nType U to go up a level. Type D to go down a level. Type H to hide.')
    # pygame.event.clear()
    key = input()
    if key == 'down' or key == 'DOWN' or key == 'd' or key == 'D':  # Down Arrow
        playerPosition = playerPosition - 1
        return playerPosition
    elif key == 'up' or key == 'UP' or key == 'u' or key == 'U':
        playerPosition = playerPosition + 1
        # os.system('clear')
        return playerPosition
    elif key == 'hide' or key == 'HIDE' or key == 'h' or key == 'H':
        hiddenStatus = True
        # os.system('clear')
        return hiddenStatus
    else:
        print('You must choose to go up, down, or hide.\n')