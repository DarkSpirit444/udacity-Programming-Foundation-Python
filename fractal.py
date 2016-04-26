import turtle

depth = 6
cursor = None

def drawLine(x1, y1, x2, y2):
    cursor.up()
    cursor.goto(x1, y1)
    cursor.down()
    cursor.goto(x2, y2)

def subTriangle(n, x1, y1, x2, y2, x3, y3):
    global depth
    
    drawLine(int(x1), int(y1), int(x2), int(y2))
    drawLine(int(x1), int(y1), int(x3), int(y3))
    drawLine(int(x2), int(y2), int(x3), int(y3))

    if n < depth:
        subTriangle(
            n + 1,
            (x1 + x2) / 2 + (x2 - x3) / 2,
            (y1 + y2) / 2 + (y2 - y3) / 2,
            (x1 + x2) / 2 + (x1 - x3) / 2,
            (y1 + y2) / 2 + (y1 - y3) / 2,
            (x1 + x2) / 2,
            (y1 + y2) / 2)

        subTriangle(
            n + 1,
            (x3 + x2) / 2 + (x2 - x1) / 2,
            (y3 + y2) / 2 + (y2 - y1) / 2,
            (x3 + x2) / 2 + (x3 - x1) / 2,
            (y3 + y2) / 2 + (y3 - y1) / 2,
            (x3 + x2) / 2,
            (y3 + y2) / 2)

        subTriangle(
            n + 1,
            (x1 + x3) / 2 + (x3 - x2) / 2,
            (y1 + y3) / 2 + (y3 - y2) / 2,
            (x1 + x3) / 2 + (x1 - x2) / 2,
            (y1 + y3) / 2 + (y1 - y2) / 2,
            (x1 + x3) / 2,
            (y1 + y3) / 2)
    
def drawSierpinski(x1, y1, x2, y2, x3, y3):
    drawLine(int(x1), int(y1), int(x2), int(y2))
    drawLine(int(x1), int(y1), int(x3), int(y3))
    drawLine(int(x2), int(y2), int(x3), int(y3))

    subTriangle(
        1,
        (x1 + x2) / 2,
        (y1 + y2) / 2,
        (x1 + x3) / 2,
        (y1 + y3) / 2,
        (x2 + x3) / 2,
        (y2 + y3) / 2)

def draw_fractal():
    global cursor
    
    window = turtle.Screen()
    window.bgcolor("white")

    w = 500
    h = 500
    window.setup(1000, 1000)
    window.screensize(1000, 1000)

    cursor = turtle.Turtle()
    cursor.color("black")
    cursor.speed(0)
    cursor.hideturtle() # enchance performance

    drawSierpinski(10, 10, w - 10, 10, w / 2, h - 10)

    window.exitonclick()

draw_fractal()
                 
