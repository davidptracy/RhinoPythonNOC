import rhinoscriptsyntax as rs
import math
import time
import random
#Bouncing Ball Sketch

#global variables
width  = 20
depth  = 20
height = 20

# Rectangles to indicate boundaries
basePlane = rs.PlaneFromPoints([0,0,0], [1,0,0], [0,1,0])
rs.AddRectangle(basePlane, width, depth)
basePlane = rs.PlaneFromPoints([0,0,height], [1,0,height], [0,1,height])
rs.AddRectangle(basePlane, width, depth)


class Attractor:
    def __init__(self, _location):
#       an attractor at the center of the screen 
        self.location = _location
        self.mass = random.uniform(10,20)
        self.G = 0.4
    def display(self):
        rs.AddSphere(self.location, self.mass/2)
    def attract(self, _mover):
        if rs.VectorCompare(self.location, _mover.location):
            force = rs.VectorSubtract(self.location, _mover.location)
            distance = rs.VectorLength(force)
            distance = self.constrain(distance, 20.0, 50.0 )
            print "Constrained Distance : ", distance
            force = rs.VectorUnitize(force)
            strength = (self.G * self.mass * _mover.mass) / (distance * distance)
            force = rs.VectorScale(force, strength)
            return force
            
    def constrain(self, value, minVal, maxVal):
        if value < minVal:
            print "MinVal returned: ", minVal
            return minVal
        elif value > maxVal:
            print "MaxVal returned: ", maxVal
            return maxVal
        else:
            print "Val returned: ", value
            return value

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
        self.sphere = rs.AddSphere(self.location, self.mass)
        rs.ObjectColor(self.sphere, rs.ColorHLSToRGB([rs.VectorLength(self.acceleration)*100, 100, 100]))
    
    def limit(self, _vector, _max):
        length = rs.VectorLength(_vector)
        if (length > _max) and not rs.VectorCompare(friction, [0,0,0]):
            normalized = rs.VectorUnitize(_vector)
            return rs.VectorScale(normalized, _max)
        else:
            return _vector

movers = []

attractor1 = Attractor(rs.VectorCreate([width/2, depth/2, height/2],[0,0,0]))
#attractor2 = Attractor(rs.VectorCreate([width/4, depth/4, height/4],[0,0,0]))

attractor1.display()
#attractor2.display()

wind = rs.VectorCreate([.05,0.025,0], [0,0,0])
gravity = rs.VectorCreate([0,0,-.05],[0,0,0])
friction = rs.VectorCreate([0,0,0],[0,0,0])

for m in range(5):
    location = rs.VectorCreate([0,0,height],[0,0,0])
#    location = rs.VectorCreate([random.uniform(0,width),random.uniform(0,depth),random.uniform(0,height)],[0,0,0])
#    velocity = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)],[0,0,0])
    velocity = rs.VectorCreate([0,0,0],[0,0,0])
    mover = Mover(location, velocity)
    movers.append(mover)

for t in range(250):
    
    for mover in movers:
        
        coeff = 0.01        
#        friction = mover.velocity
#        print rs.VectorCompare(friction, [0,0,0])
#        
#        if (rs.VectorCompare(friction, [0,0,0])):
#            print "Unscaled", friction
#            friction = rs.VectorScale(friction, -1)
#            print "Scaled -1 ", friction
#            friction = rs.VectorUnitize(friction)
#            print "Unitized ", friction
#            friction = rs.VectorScale(friction, coeff)
#            mover.applyForce(friction)
        
        gravityForce = attractor1.attract(mover)
        mover.applyForce(gravityForce)
#        gravityForce = attractor2.attract(mover)
#        mover.applyForce(gravityForce)
        
        
#        mover.applyForce(wind)
#        mover.applyForce(gravity)
        
        mover.update()
#        mover.checkEdges()
        mover.display()