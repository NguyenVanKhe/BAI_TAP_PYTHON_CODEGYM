import turtle


t=turtle.Turtle()

turtle.bgcolor("pink")
t.speed(1000)
t.penup()
t.goto(150,150)
t.pendown()

#vẽ hình mặt trời
t.pensize(1)
t.pencolor("black")
t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

#vẽ đường viền bên ngoài
t.penup()
t.goto(150,180)
t.rt(90)
t.fd(30)
t.pendown()
t.fd(30)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(20)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(30)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(20)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(30)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(20)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(30)

t.penup()
t.goto(150,180)
t.rt(45)
t.fd(30)
t.pendown()
t.fd(20)
t.lt(45)


#vẽ hình cây thông

t.penup()
t.goto(200,-100)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.fd(40)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(100)
t.end_fill()

t.penup()
t.goto(220,-100)
t.lt(90)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.goto(320,-100)
t.goto(220,-40)
t.goto(120,-100)
t.goto(220,-100)
t.end_fill()

t.penup()
t.goto(220,-40)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.goto(300,-40)
t.goto(220,10)
t.goto(140,-40)
t.goto(220,-40)
t.end_fill()

t.penup()
t.goto(220,10)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.goto(280,10)
t.goto(220,50)
t.goto(160,10)
t.goto(220,10)
t.end_fill()


#ve ngoi nha
t.penup()
t.goto(-300,-200)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.goto(-100,-200)
t.goto(-100,50)
t.goto(-300,50)
t.goto(-300,-200)
t.end_fill()

# ve cua so
t.penup()
t.goto(-230,-200)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.goto(-230,-30)
t.goto(-170,-30)
t.goto(-170,-200)
t.end_fill()

t.penup()
t.goto(-100,-200)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.goto(50,-100)
t.goto(50,150)
t.goto(-100,50)
t.end_fill()

t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.goto(20,50)
t.goto(20,80)
t.goto(-50,30)
t.goto(-50,0)
t.end_fill()

t.penup()
t.goto(-300,50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.goto(-200,200)
t.goto(-100,50)
t.end_fill()



t.penup()
t.goto(-200,200)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.goto(-50,300)
t.goto(50,150)
t.goto(-100,50)
t.end_fill()







         







     














turtle.done()