def count_chars(input_string):
    letters = 0
    digits = 0
    spaces = 0
    others = 0
    for char in input_string:

        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1

    return letters, digits, spaces, others


input_string = input("请输入一个字符串: ")
letters, digits, spaces, others = count_chars(input_string)
print(f"英文字母出现的次数: {letters}")
print(f"数字出现的次数: {digits}")
print(f"空格出现的次数: {spaces}")
print(f"其他字符出现的次数: {others}")
