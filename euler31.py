#!/usr/bin/env python3

def makeamount(goal, coins=[200, 100, 50, 20, 10, 5, 2, 1]):
    if goal==0:
        return 1
    elif len(coins)==0: 
        return 0
    elif coins[0]>goal:
        return makeamount(goal, coins[1:])
    else:
        return makeamount(goal-coins[0], coins    ) + \
               makeamount(goal,          coins[1:])

print(makeamount(200))
