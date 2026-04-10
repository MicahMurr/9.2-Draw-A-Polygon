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
    t.begin_fill()
    
    t.penup()
    t.goto(-300, 300)
    t.pendown()
    for i in range(4):
        t.forward(600)
        t.right(90)
    
    t.end_fill()

playing_area(t)
t.hideturtle()
angle=random.randint(0,360)
yertle = Turtle()
yertle.color("blue")
yertle.shape("turtle")
yertle.penup() 
yertle.setheading(angle) 


def move_forward(turtle):
    turtle.forward(5)
    
    if turtle.xcor() >= 290 or turtle.xcor() <= -290:
        turtle.right(angle-180)
    if turtle.ycor() >= 290 or turtle.ycor() <= -290:
        turtle.right(angle-180)
        


while True:
    move_forward(yertle)
    yertle.pendown()
screen.exitonclick()