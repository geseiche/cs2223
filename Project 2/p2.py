import math
import time

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __repr__(self):
        return str(self)

def distance(coord1, coord2):
    return math.sqrt(pow(coord1.x - coord2.x, 2) + pow(coord1.y - coord2.y, 2))

def brute_force(coords):
    minDist = distance(coords[0], coords[1])
    startCoord = coords[0]
    endCoord = coords[1]
    for i in range(0, len(coords)):
        for j in range (i+1, len(coords)):
            dist = distance(coords[i], coords[j])
            if(dist < minDist):
                startCoord = coords[i]
                endCoord = coords[j]
                minDist = dist
    return minDist

def EFC(p, q):
    if(len(p) <= 3):
        return brute_force(p)
    else:
        p1 = p[:len(p)//2]
        pr = p[len(p)//2:]
        q1 = q[:len(q)//2]
        qr = q[len(q)//2:]
        d1 = EFC(p1, q1)
        d2 = EFC(pr, qr)
        d = min(d1, d2)
        m = p[len(p)//2 -1].x
        s = []
        for coord in q:
            if(abs(coord.x - m) < d):
                s.append(coord)
        dminsq = pow(d, 2)
        for i in range(0, len(s)-1):
            k = i + 1
            while k <= len(s)-1 and pow(s[k].y - s[i].y, 2) < dminsq:
                dminsq = min((pow(s[k].x - s[i].x, 2) + pow(s[k].y - s[i].y, 2)), dminsq)
                k = k+1
    return math.sqrt(dminsq)

def eff_brute_force(coords):
    start = time.clock()
    brute_force(coords)
    end = time.clock()
    print("Brute force time:\t", end - start)

def eff_EFC(p, q):
    start = time.clock()
    EFC(p, q)
    end = time.clock()
    print("Recursive time:\t\t", end - start)

with open("input.txt", "r") as file:
    for line in file:
        print(line.rstrip())
        x = line.replace(")", "").replace("]", "").replace("[", "").replace("(", "").split(",")
        coords = []
        for i in range(0, len(x), 2):
            coords.append(Coordinate(float(x[i]),float(x[i+1])))
        print("Shortest Distance:\t", brute_force(coords))
        eff_brute_force(coords)
        p = sorted(coords, key = lambda x: x.x)
        q = sorted(coords, key = lambda x: x.y)
        eff_EFC(p, q)
        print()
        
            

