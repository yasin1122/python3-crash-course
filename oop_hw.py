class Line:
    def __init__(self, c1, c2) -> None:
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        """
        Could've done tuple unpacking as such:
        x1, y1 = self.c1
        x2, y2 = self.c2
        """
        return ((self.c2[0] - self.c1[0])**2 + 
                 (self.c2[1] - self.c1[1])**2) ** 0.5

    def slope(self):
        return ((self.c2[1]-self.c1[1]) / 
                (self.c2[0]-self.c1[0]))

c1, c2 = (3, 2), (8, 10)
line1 = Line(c1, c2)
print(line1.distance(), line1.slope())

class Cylinder:

    def __init__(self, height=1, radius=1) -> None:
        self.height = height
        self.radius = radius

    # V=pi(r^2)h
    def volume(self):
        return 3.14*(self.radius**2)*self.height

    # A=2pi(r^2) + 2pi(rh)
    def surface_area(self):
        return (2*3.14*(self.radius**2)+
                2*3.14*self.radius*self.height)
    
cylinder1 = Cylinder(2, 3)
print(cylinder1.volume(), cylinder1.surface_area())