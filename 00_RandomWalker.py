import rhinoscriptsyntax as rs
import random as r
import perlin as p

# set the random seed for the sketch
# defaults to 1, range between 0 and 10
#seed = rs.GetReal("Enter Random Seed: ", 5, 0, 10 )
#r.seed(seed)

class Walker:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0 
        
    def location(self):
        shape = rs.AddPoint(self.x, self.y, self.z)
        return shape
        
    def step(self):
        #r.uniform produces a float instead of an int
        stepX = r.uniform(-1,1)  #uniform returns a float with uniform distribution
        self.x += stepX
        
        stepY = r.uniform(-1,1)
        self.y += stepY
        
        stepZ = r.uniform(-1,1)
        self.z += stepZ
        
     

for s in range(5):
    r.seed(s)

    w = Walker()
    points = []
    radii = []
    parameters = []
    
    for t in range(500):
        w.step()
        points.append( w.location() )
    
    
    # add a polyline through the entire list of a
    rs.AddPolyline(points, replace_id=None)
    # add a degree 3 nurbs curve through the entire list of a
    curve = rs.AddCurve(points, degree=3)
    
    #create a bunch of radii that match the amount of points
    parameterCounter = 0
    for point in points:
        tempRadius = r.uniform(.25, 1.0)
        radii.append(tempRadius)
        parameters.append(parameterCounter)
        parameterCounter += 1/len(points)
    
    # add a pipe through all the points?
    rs.AddPipe(curve, parameters, radii, 1, 2, False)