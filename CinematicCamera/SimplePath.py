def unit(point):
    length = (point[0]**2.0 + point[1]**2.0 + point[2]**2.0)**0.5
    return (point[0]/length, point[1]/length, point[2]/length)

def invert(point):
    return (-point[0], -point[1], -point[2])

def cross(v1, v2):
    return (v1[1]*v2[2] - v1[2]*v2[1], -(v1[0]*v2[2] - v1[2]*v2[0]), v1[0]*v2[1] - v1[1]*v2[0])

def displacement(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])

def dot(v1, v2):
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]

def getPoint2(p, l):
    return(p[0]+l[0], p[1]+l[1], p[2]+l[2])

def intersect(p1, l1, p2, l2):
    if (dot(cross(l1, l2), displacement(p1, p2)) == 0):
        m = [
            [l1[0], -l2[0], p2[0] - p1[0]],
            [l1[2], -l2[2], p2[2] - p1[2]]
            ]
        print(m)
        a = m[1][0]/m[0][0]
        m[1][0] = 0
        m[1][1] -= m[0][1]*a
        m[1][2] -= m[0][2]*a
        a = m[0][1]/m[1][1]
        m[0][1] = 0
        m[0][2] -= m[1][2]*a
        s = m[0][2]/m[0][0]
        
        return (p1[0] + l1[0]*s, p1[1] + l1[1]*s, p1[2] + l1[2]*s)

    return None

class SimplePath():
    def __init__(self, tfunc, ipos=(0,0,0), ipoint=(1,0,0), fpos=(1,0,1), fpoint=(0,0,1), c=1):
        self.ipos = ipos
        self.ipoint = unit(ipoint)
        self.fpos = fpos
        self.fpoint = unit(fpoint)
        self.c = c
        self.tfunc = tfunc
        self.intersect = intersect(self.ipos, self.ipoint, self.fpos, self.fpoint)
        assert ipos != fpos, "start and end pos cannot be the same"
        assert self.intersect is not None, "Start and end tangents must intersect"
        assert c > 0 and c <= 1, "0 < c <= 1 is the valid range"
        assert tfunc is not None, "t function must exist"

    def func(self, focus, foci):
        t = self.tfunc(focus, foci)
        ret = None
        assert t <= 1 and t >= 0, "tfunc out of range (0 <= t <= 1)"
        l1 = (self.intersect[0] - self.ipos[0], self.intersect[1] - self.ipos[1], self.intersect[2] - self.ipos[2])
        l2 = (self.fpos[0] - self.intersect[0], self.fpos[1] - self.intersect[1], self.fpos[2] - self.intersect[2])
        if (self.c == 1):
            p = (self.ipos[0] + l1[0]*t, self.ipos[1] + l1[1]*t, self.ipos[2] + l1[2]*t)
            l3 = (self.intersect[0] + l2[0]*t - p[0], self.intersect[1] + l2[1]*t - p[1], self.intersect[2] + l2[2]*t - p[2])
            ret = (p[0] + l3[0]*t, p[1] + l3[1]*t, p[2] + l3[2]*t)
        else:
            l1 = (l1[0]*self.c, l1[1]*self.c, l1[2]*self.c)
            p4 = (self.intersect[0] + l2[0]*(1-self.c), self.intersect[1] + l2[1]*(1-self.c), self.intersect[2] + l2[2]*(1-self.c))
            p3 = (self.ipos[0] + l1[0], self.ipos[1] + l1[1], self.ipos[2] + l1[2])
            l2 = (l2[0]*self.c, l2[1]*self.c, l2[2]*self.c)
            p2 = (p4[0] + l2[0]*t, p4[1] + l2[1]*t, p4[2] + l2[2]*t)
            p1 = (self.ipos[0] + l1[0]*t, self.ipos[1] + l1[1]*t, self.ipos[2] + l1[2]*t)
            l3 = (p4[0] - p3[0], p4[1] - p3[1], p4[2] - p3[2])
            p3 = (p3[0] + l3[0]*t, p3[1] + l3[1]*t, p3[2] + l3[2]*t)
            l1 = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
            l2 = (p2[0] - p3[0], p2[1] - p3[1], p2[2] - p3[2])
            p1 = (p1[0] + l1[0]*t, p1[1] + l1[1]*t, p1[2] + l1[2]*t)
            p2 = (p3[0] + l2[0]*t, p3[1] + l2[1]*t, p3[2] + l2[2]*t)
            l3 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
            ret = (p1[0] + l3[0]*t, p1[1] + l3[1]*t, p1[2] + l3[2]*t)
        return ret
