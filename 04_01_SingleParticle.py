import rhinoscriptsyntax as rs
import math
import time
import random

class Particle:
    def __init__(self, _startPoint ):
        self.location = _startPoint
        self.velocity = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(1,2)],[0,0,0])
        self.acceleration = rs.VectorCreate([0,0,-0.005],[0,0,0])
        self.lifeSpan = 255.0
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        self.velocity = rs.VectorAdd(self.velocity,self.acceleration)
        self.location = rs.VectorAdd(self.location,self.velocity)
        self.lifeSpan -= 2.0
        
    def display(self):
        self.sphere = rs.AddSphere(self.location, 5.0)
        
    def isDead(self):
        if (self.lifeSpan < 0.0):
            return True
        else:
            return False

p = Particle(rs.VectorCreate([20,20,20],[0,0,0]))

            
for t in range(500):
    p.run()
    if p.isDead():
        print "Particle Died"
    
    