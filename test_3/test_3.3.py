import random
while True:
    num = input("请输入投掷次数：")
    count = 0
    for t in range(1, int(num)):
        if (random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2) < 1:
            count += 1
    print(f"圆周率近似值为；{count / int(num) * 4}")
