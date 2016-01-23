import rhinoscriptsyntax as rs
import math
import time
import random

class Particle:
    def __init__(self, _startPoint ):
        self.location = _startPoint
        self.velocity = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(1,2)],[0,0,0])
        self.acceleration = rs.VectorCreate([0,0,-0.005],[0,0,0])
        self.lifeSpan = random.uniform(500,3000)
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        self.velocity = rs.VectorAdd(self.velocity,self.acceleration)
        self.location = rs.VectorAdd(self.location,self.velocity)
        self.lifeSpan -= 2.0
        
    def display(self):
        self.point = rs.AddPoint(self.location, 5.0)
        
    def isDead(self):
        if (self.lifeSpan < 0.0):
            return True
        else:
            return False


particles = []

#particle = Particle(rs.VectorCreate([20,20,20],[0,0,0]))

for p in range(200):
    p = Particle(rs.VectorCreate([20,20,20],[0,0,0])) 
    particles.append(p)

            
for t in range(5000):
#   create a copy of the particles list first  
#   So when you modify the original list,
#   you do not modify the copy that you iterate over
#   note: this is slow because it iterates over the entire list each time
    for p in particles[:]:
        p.run()
        if p.isDead():
            particles.remove(p)