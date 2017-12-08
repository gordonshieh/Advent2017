#!/usr/bin/python3.6
import math

def get_odd_powers():
    x = 1
    while True:
        yield int(math.pow(x, 2))
        x += 2

def compute_steps(num):
    if num == 1:
        return 0
    num_layer = 0
    for layer, pow in enumerate(get_odd_powers()):
        if pow > num:
            break
    # bring everything into the bottom half
    first_diagonal = pow - (layer * 4)
    if num < first_diagonal:
        num += (first_diagonal - num) * 2
    
    second_diagonal = pow - (layer * 2)
    if num < second_diagonal:
        num = second_diagonal + (second_diagonal - num)
    diff_from_middle = abs((pow - layer) - num)
    return diff_from_middle + layer
    
print(compute_steps(361527))
