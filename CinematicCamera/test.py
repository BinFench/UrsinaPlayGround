from ursina import *
from CinematicCamera import CinematicCamera
from SimplePath import SimplePath

app = Ursina()

cube = Entity(model='cube', color=color.orange, position=(0,0,5))

def tfunc(focus, foci):
    if (focus.x <= 0):
        return 0
    if (focus.x >= 2):
        return 1

    return 1 - (2 - focus.x)/2

func = SimplePath(tfunc).func

cam = CinematicCamera(pfunc=func, focus=cube)

def update():
    if(held_keys['d']):
        cube.x += 0.05
    if(held_keys['a']):
        cube.x -= 0.05

    cam.update()

app.run()