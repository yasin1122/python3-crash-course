class Line:
    def __init__(self, c1, c2) -> None:
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        return ((self.c2[0] - self.c1[0])**2 + 
                 (self.c2[1] - self.c1[1])**2) ** 0.5

    def slope(self):
        return ((self.c2[1]-self.c1[1]) / 
                (self.c2[0]-self.c1[0]))

c1, c2 = (3, 2), (8, 10)
line1 = Line(c1, c2)
print(line1.distance(), line1.slope())