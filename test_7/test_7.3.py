def password_strength(password):
    has_digit = 0
    has_lowercase = 0
    has_uppercase = 0
    has_special_char = 0
    for char in password:
        if char.isdigit():
            has_digit = 1
        elif char.islower():
            has_lowercase = 1
        elif char.isupper():
            has_uppercase = 1
        else:
            has_special_char = 1

    if (has_digit + has_lowercase + has_uppercase + has_special_char) == 4:
        return "强密码"
    elif (has_digit + has_lowercase + has_uppercase + has_special_char) == 3:
        return "中高"
    elif (has_digit + has_lowercase + has_uppercase + has_special_char) == 2:
        return "中低"
    else:
        return "弱密码"


input_password = input("请输入一个密码: ")
print("该密码的安全等级为:", password_strength(input_password))
