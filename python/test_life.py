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
