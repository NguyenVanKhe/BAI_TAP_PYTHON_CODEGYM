import turtle


hinh = input ("nhập hình dạng circle hoặc square:")

if hinh=='circle' or hinh=='square' :
    mau = input ("nhập màu :red, yellow , blue:")
    
    if mau=='red' or mau== 'yellow' or mau=='blue' :
        
        wn = turtle.Screen() # gọi thư viện Screen trong turtle
        wn.bgcolor("black") # hình nền
        wn.title("Your shape") # thanh tiêu đề
        
        hien_thi=turtle.Turtle()
        hien_thi.shape(hinh)
        hien_thi.color(mau)
        
        turtle.done()   
    else :
         print("Sorry, I don't have this color :(")
else:
      print("Sorry, I don't have this shape :(")
     