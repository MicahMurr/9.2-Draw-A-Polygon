from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def create_player():
    global player
    player=Turtle()
    player.speed(0)
    player.shape("square")
    player.color("white")

def up():
    global player 
    player.sety(player.ycor()+10)

def down():
    global player
    player.sety(player.ycor()-10)

def left():
    global player
    player.setx(player.xcor()-10)

def right():
    global player 
    player.setx(player.xcor()+10)

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
screen.listen()
screen.onkeypress(create_player,"space")
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")

playing_area()
turtles = [create_turtle()]
player = None

while True:
    for yertle in turtles[:]:
        should_spawn = move_with_heading(yertle)
        if should_spawn:
            turtles.append(create_turtle())

        if player is not None and player.distance(yertle) < 20: 
            yertle.hideturtle()
            turtles.remove(yertle)
            
