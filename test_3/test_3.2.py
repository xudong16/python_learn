while True:
    x = input("请输入四位整数作为年份：")
    if x.isdigit():
        if int(x) <= 9999 and int(x) > 1000:
            if int(x) % 400 == 0:
                print(f"{x}是闰年。")
            elif int(x) % 4 == 0 and int(x) % 100 != 0:
                print(f"{x}是闰年。")
            else:
                print(f"{x}不是闰年。")
        else:
            continue
    else:
        continue
