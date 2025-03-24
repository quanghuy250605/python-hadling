#dùng list vì cần insert nhiều và đọc ít
arr = []

arr.append(("groceries",30))
arr.append(("movie",20))
arr.append(("membership",20))

tong = sum(a for _, a in arr)
for x1,x2 in arr:
    print("loai chi tieu: ",x1)
    print("gia tien:",x2)
print("tổng kết cuối tháng:",tong)

