import rhinoscriptsyntax as rs
import math
import time
import random
#Bouncing Ball Sketch

#global variables
width  = 500
depth  = 50
height = 50

# Rectangles to indicate boundaries
basePlane = rs.PlaneFromPoints([0,0,0], [1,0,0], [0,1,0])
rs.AddRectangle(basePlane, width, height)
basePlane = rs.PlaneFromPoints([0,0,height], [1,0,height], [0,1,height])
rs.AddRectangle(basePlane, width, height)

class Mover:
    def __init__(self, _location, _velocity):
        self.location = _location
        self.velocity = _velocity
        self.acceleration = rs.VectorCreate([0,0,0],[0,0,0])
        self.attractor = rs.VectorCreate([width/2, depth/2, height/2],[0,0,0])
        self.mass = random.uniform(1.0, 5.0)
    
    def applyForce(self, _force):
        force = rs.VectorDivide(_force, self.mass)
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
        rs.ObjectColor(self.sphere, rs.ColorHLSToRGB([rs.VectorLength(self.acceleration)*100, 100, 100]))

movers = []
wind = rs.VectorCreate([.05,0.025,0], [0,0,0])
gravity = rs.VectorCreate([0,0,-.05],[0,0,0])
#friction = rs.VectorCreate([0,0,0],[0,0,0])

for m in range(5):
    location = rs.VectorCreate([0,0,height],[0,0,0])
#    location = rs.VectorCreate([random.uniform(0,width),random.uniform(0,depth),random.uniform(0,height)],[0,0,0])
#    velocity = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)],[0,0,0])
    velocity = rs.VectorCreate([0,0,0],[0,0,0])
    mover = Mover(location, velocity)
    movers.append(mover)

for t in range(1000):
    
    for mover in movers:
        
#        coeff = 0.01
        
        print type(mover.velocity)
        
#        friction = mover.velocity
#        print rs.VectorCompare(friction, [0,0,0])
#        
#        if (rs.VectorCompare(friction, [0,0,0])):
#            print "YES"
#            print type(friction)
#            friction = rs.VectorScale(friction, -1)
#            print "Scaled -1 ", friction
#            friction = rs.VectorUnitize(friction)
#            print "Unitized ", friction     
#            mover.applyForce(friction)
        
        mover.applyForce(wind)
        mover.applyForce(gravity)
        
        mover.update()
        mover.display()
        mover.checkEdges()