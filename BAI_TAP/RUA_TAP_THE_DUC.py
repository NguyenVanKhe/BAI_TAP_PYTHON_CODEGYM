import turtle
import random as r


# khởi tạo turtle
t=turtle.Turtle()
t.shape("turtle")

# Ẩn hình con rùa
t.hideturtle()
t.pensize(2)
t.color("Blue")
t.speed(1)
t.penup()

# Đặt vị trí ban đầu con rùa sang bên trái
t.goto(-400,0)
# Hiện bị trí con rùa
t.showturtle()

# cho con rùa di chuyển từ trái qua phải

count =0
while count <10:
    
    down =r.randint(20,50)
    up =r.randint(20,50)
    t.pendown()
    
    
    t.fd(up)
    t.penup()
    
    
    t.fd(down)
    
    count+=1

turtle.done()


