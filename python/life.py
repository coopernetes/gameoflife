import copy
import itertools
import random
from typing import List

def empty_cell():
    '''Create a 2d array and initalize all values to False.
    :return: List[List[bool]]
    '''
    return [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]


def random_cell():
    cell = empty_cell()
    for i in range(3):
        for j in range(3):
            cell[i][j] = random.choice([True, False])
    return cell


def cell_from_grid(grid: List[List[bool]], x: int, y: int) -> List[List[bool]]:
    c = empty_cell()
    grid_len = len(grid)
    for i in range(3):
        for j in range(3):
            x_idx = (x - 1 + j) % grid_len
            y_idx = (y - 1 + i) % grid_len
            c[j][i] = grid[x_idx][y_idx]
    return c


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


def update(cell: List[List[bool]], state: bool) -> List[List[bool]]:
    new_cell = copy.deepcopy(cell)
    new_cell[1][1] = state
    return new_cell


if __name__ == '__main__':
    c = random_cell()
    # c = initialize_cell()
    print(c)
    print(f"Is alive? {is_alive(c)}")
    print(f"Is dead? {is_dead(c)}")
    print(f"Live Neighbours? {count_neighbours(c, True)}")
    print(f"Dead Neighbours? {count_neighbours(c, False)}")
    print(f"Should live? {should_live(c)}")
