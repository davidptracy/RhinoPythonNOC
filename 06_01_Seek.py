import rhinoscriptsyntax as rs
import math
import random
import time

class Vehicle:
    def __init__(self, _origin):
        self.location = _origin 
        self.velocity = rs.VectorCreate([0,2,0],[0,0,0])
        self.acceleration = rs.VectorCreate([0,0,0],[0,0,0])
        self.maxSpeed = 10
        self.maxForce = 100

    def update(self):
        self.velocity = rs.VectorAdd(self.velocity, self.acceleration) 
        self.velocity = self.limit(self.velocity, self.maxSpeed)
        self.location = rs.VectorAdd(self.location, self.velocity)
        self.acceleration = rs.VectorScale(self.acceleration, 0)
        
    def applyForce(self, _force):
        self.acceleration = rs.VectorAdd(self.acceleration, _force)
        
    def seek(self, _target):
        desired = rs.VectorSubtract(_target, self.location)
        desired = rs.VectorUnitize(desired)
        desired = rs.VectorScale(desired, self.maxSpeed)
        steer = rs.VectorSubtract(desired, self.velocity)
        steer = self.limit(steer, self.maxForce)
        self.applyForce(steer)
        
    def display(self):
        rs.AddPoint(self.location)

    def limit(self, _vector, _max):
        length = rs.VectorLength(_vector)
        if (length > _max) and not rs.VectorCompare(_vector, [0,0,0]):
            normalized = rs.VectorUnitize(_vector)
            return rs.VectorScale(normalized, _max)
        else:
            return _vector

basePlane = rs.PlaneFromPoints([0,0,0], [1,0,0], [0,1,0])
mWidth = 500
mHeight = 500
counter = 0
rs.AddRectangle(basePlane, mWidth, mHeight)
mVehicle = Vehicle(rs.VectorCreate([0,0,0],[0,0,0]))

for t in range(5000):
    counter = counter + .001
    target = rs.AddPoint( (math.cos(counter)*mWidth/2)+mWidth/2, (math.sin(counter)*mHeight/2)+mHeight/2, 0 )
    mVehicle.seek(target)
    mVehicle.update()
    mVehicle.display()    
