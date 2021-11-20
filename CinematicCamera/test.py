from ursina import *
from CinematicCamera import CinematicCamera
from paths import *
import math

app = Ursina()

ref = Entity(model='cube', color=color.white, position=(5,0,6))
ref2 = Entity(model='cube', color=color.white, position=(2,0,6))
cube = Entity(model='cube', color=color.orange, position=(0,0,5))

def tfunc(cam, focus, foci):
    if (focus.x <= 0):
        return 0
    if (focus.x >= 2):
        return 1

    return 1 - (2 - focus.x)/2

func = SimplePath(tfunc, fpos=(1,0,3), c=0.5).func

def rfunc(cam, focus, foci):
    if (focus.x <= 0):
        return (0,0,0)
    disp = displacement(focus.position, cam.position)
    if (disp[0] == 0):
        return (0,0,0)
    slope = disp[2]/disp[0]
    angle = 90-math.degrees(math.atan(slope))
    return (0,angle,0)

cam = CinematicCamera(pfunc=func, rfunc=rfunc, focus=cube)

def update():
    if(held_keys['d']):
        cube.x += 0.05
    if(held_keys['a']):
        cube.x -= 0.05

    cam.update()

app.run()