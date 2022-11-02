Weight=float(input("Nhập cân nặng của bạn:"))
High =float(input("Nhập chiều cao của bạn:"))

BMI =Weight/High**2

if BMI >40 :
    print(" Cơ thể bạn đang ở mức béo phì cấp độ III:")
elif BMI >=35 and BMI<=40 :
    print (" Cơ thể bạn đang ở mức béo phì cấp độ II:")
elif BMI >=30 and BMI<35 :
    print (" Cơ thể bạn đang ở mức béo phì cấp độ I:")
elif BMI >=25 and BMI<30 :
    print (" Cơ thể bạn đang ở mức thừa cân:")
elif BMI >=18.5 and BMI<25 :
    print (" Cơ thể bạn đang ở mức bình thường:")   
elif BMI >=17 and BMI<18.5 :
    print (" Cơ thể bạn đang ở mức gầy cấp độ I:")
elif BMI >=16 and BMI<17 :
    print (" Cơ thể bạn đang ở mức gầy ở cấp độ II:")  
else:
    print (" Cơ thể bạn đang ở mức gấy cấp độ III:")
    
           