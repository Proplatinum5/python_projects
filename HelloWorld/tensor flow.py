import random
import turtle
colors = ['turquoise','cyan','violet' ,'blue', 'magenta','purple']
t = turtle.Turtle()
t.speed(1000)
turtle.bgcolor("black")
length=1000
angle =69
size=5
for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+35)
    t.pendown()
    t.right(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")