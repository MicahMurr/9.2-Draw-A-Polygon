from turtle import *
import random

def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600) 

t = Turtle()
t.speed(0) 

def playing_area(t):
    t.fillcolor("teal") 
    t.penup()
    t.goto(-280, 280)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(560)
        t.right(90)
    t.end_fill()

playing_area(t)
t.hideturtle()

yertle = Turtle()
yertle.color("blue")
yertle.shape("turtle")
yertle.penup() 
yertle.setheading(65) 

def move_forward(turtle):
    turtle.forward(10)

    if turtle.xcor() > 275:
        turtle.setx(275)
        turtle.setheading(180 - turtle.heading())
    if turtle.xcor() < -275:
        turtle.setx(-275)
        turtle.setheading(180 - turtle.heading())
        
    if turtle.ycor() > 275:
        turtle.sety(275)
        turtle.setheading(-turtle.heading())
    if turtle.ycor() < -275:
        turtle.sety(-275)
        turtle.setheading(-turtle.heading())

while True:
    move_forward(yertle)
    yertle.pendown()

screen.exitonclick()