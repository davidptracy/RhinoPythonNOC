import rhinoscriptsyntax as rs
import math
import time
import random
#Bouncing Ball Sketch

#global variables
width  = 50
depth = 25
height = 25

location     = rs.VectorCreate([0,0,height-5],[0,0,0])
#random velocity vector
velocity     = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)],[0,0,0])
acceleration = rs.VectorCreate([0,0,0],[0,0,0])

basePlane = rs.PlaneFromPoints([0,0,0], [1,0,0], [0,1,0])
rs.AddRectangle(basePlane, width, height)
basePlane = rs.PlaneFromPoints([0,0,height], [1,0,height], [0,1,height])
rs.AddRectangle(basePlane, width, height)

class Mover:
    def __init__(self, _location, _velocity, _acceleration):
        self.location = _location
        self.velocity = _velocity
        self.acceleration = _acceleration
    def update(self):
        self.location = rs.VectorAdd(self.location,self.velocity)
        self.velocity = rs.VectorAdd(self.velocity,self.acceleration)
        print "X Location ", self.location[0]
        print "Velocity ", self.velocity[0]
    def checkEdges(self):
        if self.location[0] < 0 or self.location[0] > width:
            print "x triggered"
            self.velocity[0] = self.velocity[0]*-1
            print "new x velocity ", self.velocity 
        if self.location[1] < 0 or self.location[1] > depth:
            print "y triggered"
            self.velocity[1] = self.velocity[1]*-1
            print "new y velocity ", self.velocity
        if self.location[2] < 0 or self.location[2] > height:
            print "z triggered"
            self.velocity[2] = self.velocity[2]*-1
    def display(self):
        self.sphere = rs.AddSphere(self.location, 1.0)

mover = Mover(location, velocity, acceleration)

for t in range(200):
    
    mover.update()
    mover.checkEdges()
    mover.display()
    
#    time.sleep(.125)