from paths.utils import *

class BezierPath():
    def __init__(self, tfunc, points):
        self.tfunc = tfunc
        self.points = points
        assert len(self.points) > 0, "Empty points array not allowed"
        self.fpos = self.points[-1]
        self.ipos = self.points[0]

    def func(self, cam, focus, foci):
        t = self.tfunc(cam, focus, foci)
        return self.bezier(t, self.points)

    def bezier(self, t, points):
        if (len(points) == 1):
            return points[0]
        newpoints = []
        for i in range(len(points) - 1):
            line = displacement(points[i + 1], points[i])
            newpoints.append((points[i][0] + line[0]*t, points[i][1] + line[1]*t, points[i][2] + line[2]*t))
        if (len(newpoints) == 1):
            return newpoints[0]
        return self.bezier(t, newpoints)