#!/usr/bin/env python3

def step(state):
    x, y = state
    if x < 20:
        yield (x+1, y)
    if y < 20:
        yield (x, y+1)


paths_found = 0
states = [(0, 0)]

while len(states) > 0:
    print(len(states), paths_found)
    state = states.pop()
    if state == (20, 20):
        paths_found += 1
    else:
        states.extend(step(state))

print(paths_found)
