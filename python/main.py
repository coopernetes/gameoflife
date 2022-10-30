import life
import pyglet
DEAD_COLOUR = (0, 0, 0)
LIVE_COLOUR = (240, 240, 240)
window = pyglet.window.Window(720, 720)
background = pyglet.shapes.Rectangle(x=0, y=0, width=720, height=720, color=(64, 64, 64))
shape_batch = pyglet.shapes.Batch()
cell_grid = []
for i in range(24):
    for j in range(24):
        cell_grid.append(pyglet.shapes.Rectangle(x=30 * j + 5, y=30 * i + 5, width=22, height=22, color=DEAD_COLOUR, batch=shape_batch))


def mouse_intersects(x, y, rect: pyglet.shapes.Rectangle) -> bool:
    return (rect.x <= x < rect.x + 22 and
            rect.y <= y < rect.y + 22)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        print(f"LMB pressed at {x},{y}")
        for i, c in enumerate(cell_grid):
            if mouse_intersects(x, y, c):
                print(f"{x},{y} insects with cell {c.x},{c.y} at index {i}")
                c.color = LIVE_COLOUR if c.color == DEAD_COLOUR else DEAD_COLOUR

def update_cells(dt):
    print(f"Called update at {dt}")

pyglet.clock.schedule_interval(update_cells, 0.5)




@window.event
def on_draw():
    window.clear()
    background.draw()
    shape_batch.draw()

if __name__ == '__main__':
    c = life.random_cell()
    # c = life.initialize_cell()
    print(c)
    print(f"Is alive? {life.is_alive(c)}")
    print(f"Is dead? {life.is_dead(c)}")
    print(f"Live Neighbours? {life.count_neighbours(c, True)}")
    print(f"Dead Neighbours? {life.count_neighbours(c, False)}")
    print(f"Should live? {life.should_live(c)}")

    pyglet.app.run()