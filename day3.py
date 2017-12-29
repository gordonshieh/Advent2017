#!/usr/bin/python3.6
import math
import sys
from collections import namedtuple
from enum import IntEnum
from functools import lru_cache


class Direction(IntEnum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


Block = namedtuple("Block", "val x y")


def get_odd_powers():
    x = 1
    while True:
        yield int(math.pow(x, 2))
        x += 2


def draw_spiral():
    for layer, power in enumerate(get_odd_powers()):
        current_direction = Direction.LEFT
        num_block_per_layer = layer * 2 * 4
        x = layer
        y = -layer
        # compute block from the corner since it is always a root of an odd base
        for block in range(0, num_block_per_layer):
            current_block = power - block
            yield Block(current_block, x, y)

            if block > 0 and block % (layer * 2) == 0:
                # going counter clockwise, so negative it is
                current_direction = (current_direction - 1) % 4

            if current_direction == Direction.LEFT:
                x -= 1
            elif current_direction == Direction.UP:
                y += 1
            elif current_direction == Direction.RIGHT:
                x += 1
            else:
                y -= 1


@lru_cache(maxsize=sys.maxsize)
def manhattan_distance_spiral(block_num):
    if block_num == 1:
        return Block(1, 0, 0)
    for block in draw_spiral():
        if block.val == block_num:
            return block

@lru_cache(maxsize=sys.maxsize)
def is_adjacent(block, ref):
    if ref.val > block.val:
        return False

    # difference should be at most 1 block
    return max(block.x, ref.x) - min(block.x, ref.x) <= 1 and max(block.y, ref.y) - min(block.y, ref.y) <= 1


@lru_cache(maxsize=sys.maxsize)
def spiral_sum(block_num):
    assert block_num > 0
    if block_num <= 2:
        return 1
    block = manhattan_distance_spiral(block_num)
    min_block = 1
    adjacent_blocks = [ref_block for ref_block in range(min_block, block_num) if ref_block > 0 and
                       is_adjacent(block, manhattan_distance_spiral(ref_block))]
    return sum(spiral_sum(item) for item in adjacent_blocks)


def adjacent_sums(max_sum):
    sum_block = 1
    block = 1
    while sum_block < max_sum:
        block += 1
        sum_block = spiral_sum(block)
    return sum_block


ans1 = manhattan_distance_spiral(10)
print(abs(ans1.x) + abs(ans1.y))

ans2 = adjacent_sums(361527)
print(ans2)
