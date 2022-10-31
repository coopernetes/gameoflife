import itertools
import random
import life
import pyglet

DEAD_COLOUR = (0, 0, 0)
LIVE_COLOUR = (240, 240, 240)
DIMENSION = 24
window = pyglet.window.Window(730, 780)

# Very noisy debugging but helpful to use on occasion
# win_event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(win_event_logger)
background = pyglet.shapes.Rectangle(x=0, y=0, width=720, height=720, color=(64, 64, 64))
shape_batch = pyglet.shapes.Batch()
cell_grid = []
r = random.Random()
# seeded_cells = [(r.randint(0, 23), r.randint(0, 23)) for _ in range(20)]
# print(seeded_cells)
g = [[False, False, True, False, False, False, False, False, True, False, True, False, False, False, True, True, True, True, True, False, False, False, False, True], [True, True, False, False, True, False, False, True, True, True, False, False, True, True, False, True, False, False, True, True, False, True, True, False], [True, True, False, True, True, False, False, False, True, False, True, True, True, True, False, True, False, True, True, True, False, True, False, False], [False, False, False, True, False, False, True, True, True, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False], [False, True, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, True], [True, False, False, False, True, False, True, True, True, False, True, True, True, False, False, True, False, False, False, False, False, True, False, False], [False, False, True, True, False, True, False, True, True, False, False, False, True, False, True, True, False, True, False, True, False, True, True, False], [True, True, False, True, True, False, False, True, False, True, False, False, True, True, False, True, True, False, True, False, False, False, True, True], [True, True, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, True, True, True, True, False], [False, False, True, True, True, False, True, True, False, True, False, True, False, False, False, False, True, True, True, False, False, False, False, True], [False, True, True, False, True, True, True, False, True, True, True, False, True, False, False, True, True, False, False, True, True, True, True, True], [True, False, False, False, False, False, False, True, False, True, True, False, False, False, True, True, True, False, True, False, False, False, False, False], [False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, True, True, True, False, True, True, True, False], [False, True, False, True, False, True, False, True, True, True, True, True, False, False, True, True, True, True, True, False, False, True, False, False], [False, True, True, False, True, False, False, True, True, True, False, False, False, False, True, True, False, False, False, True, True, False, True, False], [True, True, False, True, False, False, True, False, True, True, True, False, True, False, False, True, True, True, True, True, False, False, True, False], [True, False, False, True, True, True, True, False, False, False, False, True, False, False, True, False, False, True, False, False, False, True, False, False], [False, True, True, False, False, False, True, True, False, False, True, True, False, True, True, True, True, False, False, True, True, False, False, True], [True, False, True, True, False, False, False, True, False, False, True, True, True, True, True, False, True, False, False, False, False, True, False, False], [True, False, True, True, True, True, True, True, False, True, False, True, False, False, False, True, True, True, False, False, False, False, True, False], [False, False, True, False, False, True, False, True, False, True, True, False, False, True, True, False, True, True, True, False, False, False, True, False], [True, True, True, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True], [True, False, True, True, True, True, True, True, True, True, False, True, False, False, True, False, False, True, True, True, True, False, False, True], [True, False, False, True, True, True, True, False, True, False, True, True, False, True, False, True, False, False, True, False, True, False, True, False]]

for i in range(DIMENSION):
    cell_grid.append([])
    for j in range(DIMENSION):
        # colour = DEAD_COLOUR
        # print(f"i: {i}, j: {j}")
        # for s in seeded_cells:
        #     if i == s[0] and j == s[1]:
        #         colour = LIVE_COLOUR
        cell_grid[i].append(pyglet.shapes.Rectangle(x=29 * j + 5, y=29 * i + 5, width=22, height=22,
                                                    # color=colour,
                                                    color=LIVE_COLOUR if g[i][j] else DEAD_COLOUR,
                                                    batch=shape_batch))


def mouse_intersects_cell(x, y, rect: pyglet.shapes.Rectangle) -> bool:
    return (rect.x <= x < rect.x + 22 and
            rect.y <= y < rect.y + 22)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        print(f"LMB pressed at {x},{y}")
        flattened_cells = itertools.chain(*cell_grid)
        for i, c in enumerate(flattened_cells):
            if mouse_intersects_cell(x, y, c):
                print(f"{x},{y} insects with cell {c.x},{c.y} at index {i}")
                c.color = LIVE_COLOUR if c.color == DEAD_COLOUR else DEAD_COLOUR


def is_live(rect: pyglet.shapes.Rectangle):
    return rect.color == LIVE_COLOUR


MAX_BACKOFF = 4
backoff = MAX_BACKOFF

def update_cells(dt):
    pass


def _update_cells(dt):
    global backoff
    print(f"Called update at {dt} (backoff: {backoff})")
    if (0 < backoff <= MAX_BACKOFF):
        backoff -= 1
        return
    print("Update cells")
    #TODO: Need to convert every rect cell to a bool
    bools = []
    for i in range(DIMENSION):
        bools.append([])
        for j in range(DIMENSION):
            bools[i].append(cell_grid[i][j].color == LIVE_COLOUR)

    c1 = [ bools[0][0:3] ]
    c1 += [ bools[1][0:3] ]
    c1 += [ bools[2][0:3] ]
    print(c1)
    c1 = life.update(c1, life.should_live(c1))
    print(c1)
    bools[0:3] = c1[0:3]
    for i in range(3):
        for j in range(3):
            cell_grid[i][j].color = LIVE_COLOUR if bools[i][j] else DEAD_COLOUR

    # for i in range(DIMENSION):
    #     this_group = [ cell_grid[i][i:i+3] ]
    #     for j in range(0, DIMENSION, 3):
    #         this_group.append()
    #     c = life.initialize_cell(this_group, is_live)
    #     print(c)


pyglet.clock.schedule_interval(update_cells, 0.5)


@window.event
def on_draw():
    window.clear()
    background.draw()
    shape_batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
