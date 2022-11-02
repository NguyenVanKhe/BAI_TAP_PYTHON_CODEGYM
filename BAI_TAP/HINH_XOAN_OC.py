import turtle
#import math



t=turtle.Turtle()
t.pensize(3)
t.pencolor("red")
t.goto(0,0)
t.speed(100)
F=1200
d=0
while (turtle.distance(0,0) < F):
    t.pendown()
    t.fd(d)
    d=d+0.1
    t.lt(10)
   
   
turtle.done()
