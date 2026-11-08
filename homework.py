# homework: in class, we drew one carrot inside our canvas
# TODO: by calling the draw_carrot() function, draw 10 carrots with random spawn positions inside the canvas.
# website to run turtle is https://pyroom.app

import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0) # speed 0 is the fastest
t.pensize(1)
t.pencolor("green")
t.fillcolor("green")
screen.bgcolor("skyblue")
screen.setup(1000, 500)

t.penup()
t.goto(-500, 50)
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(1000)
    t.right(90)
t.end_fill()



def draw_carrot(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    
    
    t.pensize(1)
    t.pencolor("black")
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(30)
    t.right(100)
    t.forward(80)
    t.right(160)
    t.forward(80)
    t.end_fill()

    
    t.pensize(7)
    t.pencolor("lime")
    t.forward(30)
    t.forward(-30)
    t.setheading(0)
    t.forward(30)
    t.left(75)
    t.forward(30)



for i in range(10):
    # Generates a random position safely within the green grass boundaries
    random_x = random.randint(-450, 420)
    random_y = random.randint(-200, -20)
    
    
    draw_carrot(random_x, random_y)














