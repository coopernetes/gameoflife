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
seeded_cells = [(r.randint(0, 23), r.randint(0, 23)) for _ in range(5)]
print(seeded_cells)
for i in range(DIMENSION):
    cell_grid.append([])
    for j in range(DIMENSION):
        colour = DEAD_COLOUR
        print(f"i: {i}, j: {j}")
        for s in seeded_cells:
            if i == s[0] and j == s[1]:
                colour = LIVE_COLOUR
        cell_grid[i].append(pyglet.shapes.Rectangle(x=29 * j + 5, y=29 * i + 5, width=22, height=22,
                                                 color=colour, batch=shape_batch))


# frame = pyglet.gui.Frame(window, order=1)
# go_button = pyglet.gui.PushButton(x=720 // 2, y=721, pressed=pyglet.resource.image('rocket_small.png'),
#                                   depressed=pyglet.resource.image('go-button.png'),
#                                   hover=pyglet.resource.image('go-button-down.png'),
#                                   batch=shape_batch)
# go_button.set_handler('on_press', activate_update)
# frame.add_widget(go_button)


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


MAX_BACKOFF = 20
backoff = MAX_BACKOFF


def update_cells(dt):
    global backoff
    print(f"Called update at {dt} (backoff: {backoff})")
    if (0 < backoff <= MAX_BACKOFF):
        backoff -= 1
        return
    print("Update cells")
    #TODO: Slice cell_grid in 3x3 md arrays and use life functions
    #TODO: Convert 3x3 md array to cell_grid entries
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
