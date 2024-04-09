i = input("请输入一个四位自然数：")
if i.isdigit() and len(i) == 4:
    t = str(i)
    for j in t:
        print(j)
else:
    print("输入有误")
