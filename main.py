from turtle import *

def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360 / sides)
    turtle.end_fill()   

def draw_rectangle(turtle):
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(75)
        turtle.right(90)
    turtle.end_fill()

def draw_parallelogram(turtle):
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(150)
        turtle.left(60)
        turtle.forward(80)
        turtle.left(120)
    turtle.end_fill()

def draw_iso_trapezoid(turtle):
    turtle.begin_fill()
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(80)
    turtle.left(60)
    turtle.forward(70)
    turtle.left(60)
    turtle.forward(80)
    turtle.left(120)
    turtle.end_fill()

def draw_general_trapezoid(turtle):
    turtle.begin_fill()
    turtle.goto(200, 0)
    turtle.goto(150, 100)
    turtle.goto(50, 100)
    turtle.goto(0, 0)
    turtle.end_fill()
    turtle.setheading(0)

def draw_irregular_quad(turtle):
    turtle.begin_fill()
    turtle.goto(160, 20)
    turtle.goto(110, 140)
    turtle.goto(-30, 80)
    turtle.goto(0, 0)
    turtle.end_fill()
    turtle.setheading(0)

screen = Screen()
screen.bgcolor("teal")

pen = Turtle()
pen.speed(0)
pen.color("lavender")
pen.shape("turtle")

while True:
   
    
    sides = int(input("How many sides does the polygon have? "))
        
    if sides != 4:
        regular_polygon(pen, sides)
        
    else:
        par = int(input("How many sides are parallel?  "))
        
        if par == 4:
            equal = int(input("How many sides are equal?  "))
            if equal == 4:
                regular_polygon(pen, 4)
            elif equal == 2:
                angles = int(input("Are the angles 90 degrees? 1 = Yes 0 = No "))
                if angles == 1:
                    draw_rectangle(pen)
                else:
                    draw_parallelogram(pen)
                
        elif par == 2:
            equal = int(input("How many sides are equal? (2 or 0): "))
            if equal == 2:
                draw_iso_trapezoid(pen)
            else:
                draw_general_trapezoid(pen)
                
        elif par == 0:
            draw_irregular_quad(pen)

screen.exitonclick()