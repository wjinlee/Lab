class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setx(self, x):
        self.x = x
        # print(self.x)
    def sety(self, y):
        self.y = y
        # print(self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        # print(self.x, self.y)
    def get(self):
        return (self.x, self.y)

# a = point(1, 1)

# a.setx(10)
# a.sety(10)
# a.move(3, 3)



