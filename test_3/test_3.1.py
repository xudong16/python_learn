def ana(x):
    if x < 0:
        return 0
    elif x >= 0 and x < 5:
        return x
    elif x >= 5 and x < 10:
        return 3*x-5
    elif x >= 10 and x < 20:
        return 0.5*x-2
    elif x >= 20:
        return 0
while True:
    x = input("请输入x值:")
    print(f"结果是：{ana(int(x))}")
