user_info = {}

name = input("请输入您的姓名：")
user_info["姓名"] = name

age = input("请输入您的年龄：")
user_info["年龄"] = age

gender = input("请输入您的性别：")
user_info["性别"] = gender

for key, value in user_info.items():
    print(f"{key}：{value}")