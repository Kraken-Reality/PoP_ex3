
class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, point):

        if isinstance(point, tuple):
            xdif = self.centre[0] - point[0]
            ydif = self.centre[1] - point[1]
            dist = (xdif**2 + ydif**2)**(1/2)
            
            if dist < self.radius:
                return True
            else:
                return False
        else:
            return NotImplemented
