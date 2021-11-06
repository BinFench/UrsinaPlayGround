from ursina import *

class CinematicCamera():
    # By default, a fixed view camera.  The dev provides functions for 
    # movement, rotation, and pov dependent on a primary focus object and/or
    # array of focus objects

    # Example: Functions are provided to keep a focus object in the center
    # of the screen, as well as keep all foci objects on screen

    def __init__(self, pos=(0,0,0), rot=(0,0,0), fov=40, focus=None, foci=[], pfunc=None, rfunc=None, fovfunc=None):
        self.position=pos
        self.rotation=rot
        self.fov=fov
        self.focus=focus
        self.foci=foci
        self.pfunc=pfunc
        self.rfunc=rfunc
        self.fovfunc=fovfunc
        self.camera=camera
        self.updateCamera()

    def updateCamera(self):
        self.camera.position = self.position
        self.camera.rotation = self.rotation
        self.camera.fov = self.fov

    def update(self):
        if (self.pfunc is not None):
            self.position = self.pfunc(self.focus, self.foci)
        if (self.rfunc is not None):
            self.rotation = self.rfunc(self.focus, self.foci)
        if (self.fovfunc is not None):
            self.fov = self.fovfunc(self.focus, self.foci)
        self.updateCamera()