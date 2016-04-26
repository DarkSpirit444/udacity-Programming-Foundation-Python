import turtle

# Draw all shapes on a single window
_window = None

class Shape(object):

    # initialize window only once
    @classmethod
    def init_window(cls, bgColor):
        global _window
        if _window == None:
            _window = turtle.Screen()
            _window.bgcolor(bgColor)

    # deinitialize window only once
    @classmethod
    def close_window(cls):
        global _window
        if not _window == None:
            _window.exitonclick()
            _window = None

    # set window properties    
    def __init__(self, winBgColor, turShape, turColor, turSpeed):
        self.winBgColor = winBgColor
        self.turShape = turShape
        self.turColor = turColor
        self.turSpeed = turSpeed

    # initialize the window
    def __enter__(self):
        self.init_window(self.winBgColor)
        return self

    # deinitiallize the window
    def __exit__(self, type, value, traceback):
        self.close_window()

    # initialize the cursor   
    def draw(self):        
        self.turtle = turtle.Turtle()
        self.turtle.reset()
        self.turtle.shape(self.turShape)
        self.turtle.color(self.turColor)
        self.turtle.speed(self.turSpeed)

class Circle(Shape):

    def __init__(self, radius):
        super(Circle, self).__init__("red", "arrow", "blue", 2)
        self.radius = radius

    def draw(self):
        super(Circle, self).draw()
        self.turtle.circle(self.radius)

class EquilateralPolygon(Shape):

    # polygon needs the number of sides and length
    def __init__(self, sides, length, winBgColor, turShape, turColor, turSpeed):
        super(EquilateralPolygon, self).__init__(winBgColor, turShape, turColor, turSpeed)
        if sides == 0:
            raise ValueError("Number of sides cannot be zero!")
        else:
            self.sides = sides
            self.length = length

    def draw(self):
        super(EquilateralPolygon, self).draw()
        angle = 360 / self.sides  # calculate our turning angle
        for index in range(self.sides):
            self.turtle.forward(self.length)
            self.turtle.right(angle)
        
class Square(EquilateralPolygon):

    # square has 4 sides
    def __init__(self, length):
        super(Square, self).__init__(4, length, "red", "turtle", "yellow", 2)

class EquilateralTriangle(EquilateralPolygon):

    # triangle has 3 sides
    def __init__(self, length):
        super(EquilateralTriangle, self).__init__(3, length, "red", "arrow", "green", 2)

with Circle(100) as circle, Square(100) as square, EquilateralTriangle(100) as triangle:
    circle.draw()
    square.draw()
    triangle.draw()

