from paths.utils import *

class SegmentPath():
    def __init__(self, paths):
        assert len(paths) > 0, "Empty paths array not supported"
        self.paths = paths
        self.ipos = paths[0].ipos
        self.fpos = paths[-1].fpos
        self.current = 0

    def func(self, cam, focus, foci, prev=None):
        path = self.paths[self.current]
        place = path.func(cam, focus, foci)
        if (place == path.ipos and prev != place and self.current > 0):
            self.current -= 1
            return self.func(cam, focus, foci, place)
        if (place == path.fpos and prev != place and self.current < len(self.paths) - 1):
            self.current += 1
            return self.func(cam, focus, foci, place)
        return place