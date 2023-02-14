import turtle
import time

#Step1: Set up the turtle
t = turtle.Turtle()
t.speed(10)
t.color("red")
t.pensize(10)


# Move the turtle to the starting position
t.penup()
t.goto(-200, 0)
t.setposition(-220, -170)
t.pendown()

#Step2: Write "I" on the screen
t.write("I ", font=("Georgia", 140, "bold"))

#Step3: Move the turtle to the position for the heart symbol
t.penup()
t.goto(20, -10)
t.pendown()

# Draw the heart symbol using turtle graphics
t = turtle.Turtle()
t.speed(10)

def heart():
  t.begin_fill()
  t.left(140)
  t.forward(111.65)
  t.circle(-45, 180)
  t.setheading(60)
  t.circle(-45, 180)
  t.forward(111.65)
  t.end_fill()

t.color("red")
heart()

#Step4: Move the turtle to the position for the "U" text
t.penup()
t.goto(80, 0)
t.setposition(150, 100)
t.pendown()

# Write "U" on the screen
t.write("U", font=("Verdana", 140, "bold"))

# Hide the turtle
t.hideturtle()

#step5
t = turtle.Turtle()

colors = ["orange", "yellow", "green", "blue", "indigo", "violet"]

while True:
    for color in colors:
        t.screen.bgcolor(color)
        time.sleep(1)

# Keep the window open until the user closes it
turtle.done()