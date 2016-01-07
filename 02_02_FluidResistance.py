import rhinoscriptsyntax as rs
import math
import time
import random
import sys
#Bouncing Ball Sketch

#global variables
width  = 500
depth  = 200
height = 50

# Rectangles to indicate boundaries
basePlane = rs.PlaneFromPoints([0,0,0], [1,0,0], [0,1,0])
rs.AddRectangle(basePlane, width, depth)
basePlane = rs.PlaneFromPoints([0,0,height], [1,0,height], [0,1,height])
rs.AddRectangle(basePlane, width, depth)

class Liquid:
    def __init__(self, _x, _y, _w, _h, _d, _c):
        self.xOrigin = _x
        self.yOrigin = _y
        self.width = _w
        self.height = _h
        self.depth  = _d
        self.coefficient = _c

class Mover:
    def __init__(self, _location, _velocity):
        self.location = _location
        self.velocity = _velocity
        self.acceleration = rs.VectorCreate([0,0,0],[0,0,0])
        self.attractor = rs.VectorCreate([width/2, depth/2, height/2],[0,0,0])
        self.mass = random.uniform(1.0, 5.0)
    
    def applyForce(self, _force):
        force = rs.VectorDivide(_force, self.mass)
        print "Force ", force
        self.acceleration = rs.VectorAdd(self.acceleration, force)
    
    def update(self):
        self.velocity = rs.VectorAdd(self.velocity,self.acceleration)
        self.location = rs.VectorAdd(self.location,self.velocity)
        
    def checkEdges(self):
        
        if self.location[0] < 0:
            self.location[0] = 0
            self.velocity[0] = self.velocity[0]*-1
        elif self.location[0] > width:
            self.location[0] = width
            self.velocity[0] = self.velocity[0]*-1

        if self.location[1] < 0:
            self.location[1] = 0
            self.velocity[1] = self.velocity[1]*-1
        elif self.location[1] > depth:
            self.location[1] = depth
            self.velocity[1] = self.velocity[1]*-1

        if self.location[2] < 0:
            self.location[2] = 0
            self.velocity[2] = self.velocity[2]*-1
        elif self.location[2] > height:
            self.location[2] = height
            self.velocity[2] = self.velocity[2]*-1

    def display(self):
        self.sphere = rs.AddSphere(self.location, self.mass/2)
        
    def drag(self):
        coeff = 0.1
        speed = rs.VectorLength(self.velocity)
        dragMagnitude = coeff*speed*speed
        
        if (rs.VectorCompare(self.velocity, [0,0,0])):
            try:
                drag = self.velocity
                drag = rs.VectorScale(drag, -1)
                drag = rs.VectorUnitize(drag)
                drag = rs.VectorScale(drag, dragMagnitude)
                print "Drag ", drag
                self.applyForce(drag)
            except:
                print sys.exc_info()[0]
movers = []
wind = rs.VectorCreate([.05,0.025,0], [0,0,0])
gravity = rs.VectorCreate([0,0,-.05],[0,0,0])
#coeff = .1

for m in range(5):
    location = rs.VectorCreate([0,0,height],[0,0,0])
    velocity = rs.VectorCreate([0,0,0],[0,0,0])
    mover = Mover(location, velocity)
    movers.append(mover)

for t in range(500):
    
    for mover in movers:
        
        
        if mover.location[1] > 3*width/4:
            mover.drag()
        mover.applyForce(wind)
        mover.applyForce(gravity)
        
        mover.update()
        mover.checkEdges()
        mover.display()
