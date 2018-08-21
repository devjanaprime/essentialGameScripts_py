# seed the pseudorandom number generator
from random import seed
from random import random
import time

def diceRoll( dice, max ):
    total = 0
    for x in range(0, dice):
        millis = int( round( time.time() * 1000 ) )
        seed( millis )
        total += int( random() * max ) + 1
    return total;

print diceRoll( dice=3, max=6 );