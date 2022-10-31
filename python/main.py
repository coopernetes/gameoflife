import itertools
import random
import life
import pyglet

DEAD_COLOUR = (0, 0, 0)
LIVE_COLOUR = (240, 240, 240)
DIMENSION = 48
CELL_WIDTH, CELL_HEIGHT = 11, 11
INTERVAL = 14
PADDING = 3
MAX_BACKOFF = 50
SEEDED_CELLS = 500
REFRESH_RATE = 0.2
window = pyglet.window.Window(730, 780)

# Very noisy debugging but helpful to use on occasion
# win_event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(win_event_logger)
background = pyglet.shapes.Rectangle(x=0, y=0, width=720, height=720, color=(64, 64, 64))
shape_batch = pyglet.shapes.Batch()
cell_grid = []
r = random.Random()
seeded_cells = [(r.randint(0, DIMENSION - 1), r.randint(0, DIMENSION - 1)) for _ in range(SEEDED_CELLS)]
print(seeded_cells)

for i in range(DIMENSION):
    cell_grid.append([])
    for j in range(DIMENSION):
        colour = DEAD_COLOUR
        for s in seeded_cells:
            if i == s[0] and j == s[1]:
                colour = LIVE_COLOUR
        cell_grid[i].append(pyglet.shapes.Rectangle(x=INTERVAL * j + PADDING, y=INTERVAL * i + PADDING,
                                                    width=CELL_WIDTH, height=CELL_HEIGHT,
                                                    color=colour, batch=shape_batch))


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


backoff = MAX_BACKOFF

def update_cells(dt):
    global backoff
    print(f"Called update at {dt} (backoff: {backoff})")
    if (0 < backoff <= MAX_BACKOFF):
        backoff -= 1
        return
    bools = []
    for i in range(DIMENSION):
        bools.append([])
        for j in range(DIMENSION):
            bools[i].append(cell_grid[i][j].color == LIVE_COLOUR)

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            c = life.cell_from_grid(bools, i, j)
            cell_grid[i][j].color = LIVE_COLOUR if life.should_live(c) else DEAD_COLOUR


pyglet.clock.schedule_interval(update_cells, REFRESH_RATE)


@window.event
def on_draw():
    window.clear()
    background.draw()
    shape_batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
