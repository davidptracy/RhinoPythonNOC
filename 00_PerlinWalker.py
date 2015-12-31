import rhinoscriptsyntax as rs
import random as r
import perlin as p

class Walker:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0 
                
    def step(self, n1, n2, n3):        
        self.x += n1
        print(self.x)
        self.y += n2
#        print(n2)
        self.z += n3
#        print(n3)
    def location(self):
        shape = rs.AddPoint(self.x, self.y, self.z)
        return shape

#time parameters to pass into the noise2d function
timerX1 = r.randint(0,1000)
timerX2 = r.randint(0,1000)

timerY1 = r.randint(0,1000)
timerY2 = r.randint(0,1000)

timerZ1 = r.randint(0,1000)
timerZ2 = r.randint(0,1000)

w = Walker()
points = []
parameters = []
radii = []

#take 500 steps 
for t in range(500):
    
    noise1 = p.SimplexNoise().noise2(timerX1, timerX2)
    noise2 = p.SimplexNoise().noise2(timerY1, timerY2)
    noise3 = p.SimplexNoise().noise2(timerZ1, timerZ2)    
    
    w.step(noise1, noise2, noise3)
    points.append( w.location() )
    
    timerX1 += .0125
    timerX2 += .0125
    timerY1 += .0125
    timerY2 += .0125
    timerZ1 += .0125
    timerZ2 += .0125

#create a curve object to 
curve = rs.AddCurve(points, degree=3)

#create a bunch of radii that match the amount of points
parameterCounter = 0
for point in points:
    tempRadius = r.uniform(.25, 1.0)
    radii.append(tempRadius)
    parameters.append(parameterCounter)
    parameterCounter += 1/len(points)

# add a pipe through all the points
# normalized curve parameters at which to place the radius
rs.AddPipe(curve, parameters, radii, 1, 2, False)