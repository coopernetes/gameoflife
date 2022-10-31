import copy
import itertools
import random
from typing import List, Callable, Any


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
    # when x = 0 and y = 0:
    #   c[j][i]...
    #   c[0][0] == grid[-1][-1]
    #   c[1][0] == grid[0][-1]
    #   c[2][0] == grid[1][-1]

    #   c[0][1] == grid[-1][0]
    #   c[1][1] == grid[0][0]
    #   c[2][1] == grid[1][0]

    #   c[0][2] == grid[-1][1]
    #   c[1][2] == grid[0][1]
    #   c[2][2] == grid[1][1]

    # when x, y = grid - 1 (23) and grid == 24:
    #   c[j][i]...
    #   c[0][0] == grid[22][22] ([x-1][y-1])
    #   c[1][0] == grid[23][22] ([x][y-1])
    #   c[2][0] == grid[-1][22] ([0][y-1])

    #   c[0][1] == grid[-1][0] ([x-1][y])
    #   c[1][1] == grid[0][0]  ([x][y])
    #   c[2][1] == grid[1][0]  ([0][y])

    #   c[0][2] == grid[-1][1]
    #   c[1][2] == grid[0][1]
    #   c[2][2] == grid[1][1]
    for i in range(3):
        for j in range(3):
            c[j][i] = grid[j - (x % grid_len + 1)][i - (y % grid_len + 1)]
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
