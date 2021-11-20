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

def dist3D(p1, p2):
	return ((p1[0]-p2[0])**2.0 + (p1[1]-p2[1])**2.0 + (p1[2]-p2[2])**2.0)**0.5