import turtle


# nhập chiều dài cạnh của hình vuông
a =int (input ( "Nhập chiều dài cạnh của hình vuông: "))


t=turtle.Turtle()
#t.pensize(3)
t.hideturtle()
t.pencolor("red")
edge=0


while edge<=4:
        
    t.fd(90)
    t.rt(90)
    edge+=1
    
turtle.done()
       