import pyglet
from pygame.draw_py import draw_lines

window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()

pyglet.app.run()