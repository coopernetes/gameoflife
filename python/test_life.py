import life


def test_rule_live_two_neighbours_should_stay_alive():
    two_neighbours = [[True, False, False], [True, True, False], [False, False, False]]
    assert life.should_live(two_neighbours) is True


def test_rule_live_three_neighbours_should_stay_alive():
    three_neighbours = [[True, False, False], [True, True, False], [True, False, False]]
    assert life.should_live(three_neighbours) is True


def test_rule_live_should_die():
    one_neighbour = [[True, False, False], [False, True, False], [False, False, False]]
    assert life.should_live(one_neighbour) is False


def test_life_counts_live_neighbours():
    c1 = [[True, True, True], [False, False, False], [True, False, True]]
    assert life.count_neighbours(c1, True) == 5


def test_life_counts_dead_neighbours():
    c1 = [[True, True, True], [False, False, False], [True, False, True]]
    assert life.count_neighbours(c1, False) == 3


def test_update():
    c1 = [[True, True, True], [False, False, False], [False, False, False]]
    assert life.update(c1, True)[1][1] is True

    c2 = [[True, False, False], [False, True, False], [False, False, False]]
    assert life.update(c2, False)[1][1] is False

TEST_GRID = [[False, False, True, False, False, False, False, False, True, False, True, False, False, False, True, True, True, True, True, False, False, False, False, True], [True, True, False, False, True, False, False, True, True, True, False, False, True, True, False, True, False, False, True, True, False, True, True, False], [True, True, False, True, True, False, False, False, True, False, True, True, True, True, False, True, False, True, True, True, False, True, False, False], [False, False, False, True, False, False, True, True, True, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False], [False, True, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, True], [True, False, False, False, True, False, True, True, True, False, True, True, True, False, False, True, False, False, False, False, False, True, False, False], [False, False, True, True, False, True, False, True, True, False, False, False, True, False, True, True, False, True, False, True, False, True, True, False], [True, True, False, True, True, False, False, True, False, True, False, False, True, True, False, True, True, False, True, False, False, False, True, True], [True, True, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, True, True, True, True, False], [False, False, True, True, True, False, True, True, False, True, False, True, False, False, False, False, True, True, True, False, False, False, False, True], [False, True, True, False, True, True, True, False, True, True, True, False, True, False, False, True, True, False, False, True, True, True, True, True], [True, False, False, False, False, False, False, True, False, True, True, False, False, False, True, True, True, False, True, False, False, False, False, False], [False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, True, True, True, False, True, True, True, False], [False, True, False, True, False, True, False, True, True, True, True, True, False, False, True, True, True, True, True, False, False, True, False, False], [False, True, True, False, True, False, False, True, True, True, False, False, False, False, True, True, False, False, False, True, True, False, True, False], [True, True, False, True, False, False, True, False, True, True, True, False, True, False, False, True, True, True, True, True, False, False, True, False], [True, False, False, True, True, True, True, False, False, False, False, True, False, False, True, False, False, True, False, False, False, True, False, False], [False, True, True, False, False, False, True, True, False, False, True, True, False, True, True, True, True, False, False, True, True, False, False, True], [True, False, True, True, False, False, False, True, False, False, True, True, True, True, True, False, True, False, False, False, False, True, False, False], [True, False, True, True, True, True, True, True, False, True, False, True, False, False, False, True, True, True, False, False, False, False, True, False], [False, False, True, False, False, True, False, True, False, True, True, False, False, True, True, False, True, True, True, False, False, False, True, False], [True, True, True, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True], [True, False, True, True, True, True, True, True, True, True, False, True, False, False, True, False, False, True, True, True, True, False, False, True], [True, False, False, True, True, True, True, False, True, False, True, True, False, True, False, True, False, False, True, False, True, False, True, False]]
    

def test_wrapped_cell_bottom_left():
    x = 0
    y = 0
    assert not TEST_GRID[x][y] # Cell to observe
    expected_cell = [
        [False, True, False], # 0: 0 = Top-right or g[23][23], 1 = top-left or g[0][23] and 2 = top-left shift 1 or g[1][23]
        [True, False, False], # 1: 0 = bottom-right or g[23][0], 1 = this cell or g[0][0], 2 = g[0][1]
        [False, True, True]   # 2: 0 = bottom-right shift 1 or g[23][1], 1 = g[1][0], 2 = g[1][1]
    ]
    assert life.cell_from_grid(TEST_GRID, x, y) == expected_cell


def test_wrapped_cell_top_right():
    x = len(TEST_GRID) - 1
    y = len(TEST_GRID) - 1
    expected_cell = [
        [False, True, True],
        [True, False, True],
        [False, True, False]
    ]
    assert life.cell_from_grid(TEST_GRID, x, y) == expected_cell
