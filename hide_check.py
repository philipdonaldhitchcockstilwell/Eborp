from random import randint

def attack_prompt(player):
    for i in range(10):
        print('\n')
    print('You are hidden and', player, 'is on your floor. Would you like to attack? (Y/N)')
    attack = input()
    if attack == 'Y' or attack == 'y' or attack == 'YES' or attack == 'yes':
        result = randint(0, 10)
        if result >= 3:
            return True
        else:
            return False
    if attack == 'N' or attack == 'n' or attack == 'NO' or attack == 'no':
        return False
    else:
        return False


def hide_check(p1p, p2p, p1h, p2h, turn, p1, p2):
    if turn == 1:
        if p1p == p2p and (p1h is True and p2h is False):
            attackResult = attack_prompt(p2)
            if attackResult is True:
                return True
            if attackResult is False:
                print('Your attack attempt failed.')
                return False
        elif p1p == p2p and (p1h is False and p2h is False):
            print('You spotted each other on the same floor.\n')
            return False
        else:
            return False
    if turn == 2:
        if p1p == p2p and (p2h is True and p1h is False):
            attackResult = attack_prompt(p1)
            if attackResult is True:
                return True
        elif p1p == p2p and (p1h is False and p2h is False):
            print('You spotted each other on the same floor.\n')
            return False
        else:
            return False
