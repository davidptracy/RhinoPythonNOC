import rhinoscriptsyntax as rs
import math
import time
import random

class Particle:
    def __init__(self, _startPoint ):
        self.location = _startPoint
        self.velocity = rs.VectorCreate([random.uniform(-1,1),random.uniform(-1,1),random.uniform(1,2)],[0,0,0])
        self.acceleration = rs.VectorCreate([0,0,-0.005],[0,0,0])
        self.lifeSpan = random.uniform(100,200)
        
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

class ParticleSystem:
    def __init__(self, _location):
        self.particles = []
        self.origin = rs.VectorCreate(_location,[0,0,0])
        
    def addParticle(self):
        self.particles.append(Particle(self.origin))
        
    def run(self):
        #   create a copy of the particles list first  
        #   So when you modify the original list,
        #   you do not modify the copy that you iterate over
        #   note: this is slow because it iterates over the entire list each time
        for p in self.particles[:]:
            p.run()
            print len(self.particles)
            if p.isDead():
                self.particles.remove(p)


ps = ParticleSystem(rs.VectorCreate([0,0,0],[0,0,0]))
ps2 = ParticleSystem(rs.VectorCreate([50,50,0],[0,0,0]))

for t in range(100):
    ps.addParticle()
    ps2.addParticle()
    ps.run()
    ps2.run()

