import turtle



t=turtle.Turtle()
t.goto(0,0)
turtle.Screen().bgcolor("black")
R=float(input("Nhập bán kính:"))
Angle=float(input("nhập góc lệch cho hình ellipse:"))
count =0
i=0
array_color=['red','pink','yellow', 'blue', 'green']
while True:
    t.pencolor(array_color[i])
    print(array_color[i])
    t.speed(100)
    t.circle(200,90)
    t.circle(100,90)
    t.circle(200,90)
    t.circle(100,90)
    t.rt(Angle)
    count+=1
    i+=1
    if i==len(array_color):
        i=0
    if count==(360/Angle):
        break
turtle.done()