import copy
import itertools
from typing import List


def initialize_cell():
    return [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]


def is_alive(cell: List[List[bool]]) -> bool:
    return cell[1][1]


def is_dead(cell: List[List[bool]]) -> bool:
    return not cell[1][1]


def should_live(cell: List[List[bool]]) -> bool:
    live_neighbours = count_neighbours(cell, True)
    if (is_dead(cell) and
            live_neighbours == 3):
        return True
    if (is_alive(cell) and
            (live_neighbours == 2 or live_neighbours == 3)):
        return True
    return False


def count_neighbours(cell: List[List[bool]], state: bool = False) -> int:
    neighbours = copy.deepcopy(cell)
    neighbours[1].pop(1)
    flattened = list(itertools.chain(*neighbours))
    return len([x for x in flattened if x is state])

def convert_to_live(cell: List[List[bool]]) -> List[List[bool]]:
    return cell
