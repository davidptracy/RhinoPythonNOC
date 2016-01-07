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
velocity     = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(0,1)],[0,0,0])
acceleration = rs.VectorCreate([-.001,-.001,-.5],[0,0,0])

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
        dist = height - self.location[2]
        self.sphere = rs.AddSphere(self.location, dist/10)

mover = Mover(location, velocity, acceleration)

for t in range(100):
    
    mover.update()
    mover.checkEdges()
    mover.display()
