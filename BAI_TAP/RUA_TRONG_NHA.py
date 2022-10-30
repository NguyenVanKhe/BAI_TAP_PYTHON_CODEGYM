import turtle
import random as r


''' khởi tạo đối tượng turtle và đặt vị trí đầu tiên
    vẽ đường bao nhốt rùa trong nhà
    '''
t=turtle.Turtle()
t.penup()
t.hideturtle()
t.goto(0,-200)

''' vẽ đường bao màu đen nhốt rùa'''
t.shape("turtle")
t.fillcolor("yellow")
t.begin_fill()
t.pencolor("black")
t.speed(10)
t.pensize(10)
t.pendown()
t.circle(200)
t.end_fill()

''' Đặt con rùa ở vị trí giữa đường bao và cho rùa quay theo một hướng ngẫu nhiên'''
t.penup()
t.speed(10)
t.shape("turtle")
t.pencolor("red")
t.goto(0,0)

''' tạo một hướng ngẫu nhiên cho con rùa'''

angle = r.randint(0,360)
t.right(angle)
t.showturtle()


'''Cho rùa chạy, bắt về vị trí cũ khi rùa chạy đến đường giới hạn và cho rùa chạy hướng mới'''
count = 0
while True:
    t.speed(1)
    # rùa chỉ di chuyển một khoảng cách
    # hơi bé hơn bán kính của hộp tròn là 200
    # tránh rùa di chuyển đè lên vạch
    t.forward(188)
    # Bắt rùa về vị trí ban đầu, chính giữa hộp tròn
    t.hideturtle()
    t.speed(10)
    t.goto(0, 0)
    angle = r.randint(0, 360)
    # Tạo hướng mới cho rùa chạy, thử vận may mới
    t.right(angle)
    t.showturtle()
    # Khi rùa thử đến số lần nào đó thì dừng lại
    # kết thúc chương trình bằng lệnh break
    count += 1
    if count == 10:
        break

turtle.done()

