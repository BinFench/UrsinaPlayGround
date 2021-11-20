from paths.utils import *

class Line():
    def __init__(self, tfunc, ipos=(0,0,0), fpos=(1,0,0)):
        self.tfunc=tfunc
        self.ipos = ipos
        self.fpos = fpos
        self.line = displacement(fpos, ipos)

    def func(self, cam, focus, foci):
        t = self.tfunc(cam, focus, foci)
        return (ipos[0] + line[0]*t, ipos[1] + line[1]*t, ipos[2] + line[2]*t)