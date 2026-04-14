from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-240, 240)
    t.pendown()
    t.fillcolor("teal")
    t.begin_fill()
    for i in range(4):
        t.forward(480)
        t.right(90)
    t.end_fill()

def create_turtle():
    y = Turtle()
    y.shape("turtle")
    y.color(generate_color())
    y.speed(0)
    y.penup()
    y.setheading(random.randint(0, 360))
    return y

def move_with_heading(t):
    spawn = False
    t.forward(5)
    
    if t.xcor() >= 240 or t.xcor() <= -240:
        t.setheading(180 - t.heading())
        spawn = True
        
    if t.ycor() >= 240 or t.ycor() <= -240:
        t.setheading(-t.heading())
        spawn = True
    return spawn

screen = Screen()
screen.bgcolor("black")
screen.setup(520, 520)

playing_area()
turtles = [create_turtle()]

while True:
    for yertle in turtles:
        if move_with_heading(yertle):
            turtles.append(create_turtle())

screen.exitonclick()