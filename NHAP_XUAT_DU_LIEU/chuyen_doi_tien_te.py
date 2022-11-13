usd=int(input("nhập số tiền usd cần chuyển đổi:"))
ti_gia=int(input("nhập tỉ giá giữa vnd/usd:"))

vnd=usd*ti_gia
print("số tiền {0} usd đổi sang vnd theo tỉ giá {1} là: {2}".format(usd,ti_gia,vnd))