import turtle
from pprint import pprint

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    #window.colormode(255)

    brad = turtle.Turtle()

    #brad.pen(pencolor="yellow", fillcolor="green")
    brad.color("yellow")
    brad.shape("turtle")

    brad.speed(2)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_square()
