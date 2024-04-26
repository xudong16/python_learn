def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        # 不对非字母进行处理
        else:
            encrypted_char = char
        result += encrypted_char
    return result


input_text = input("请输入一个字符串: ")
input_key = int(input("请输入一个整数作为密钥: "))
encrypted_text = caesar_encrypt(input_text, input_key)
print("加密后的字符串是:", encrypted_text)
