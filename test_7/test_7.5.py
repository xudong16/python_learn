def find_three_letter_words(text):
    words = text.split()
    three_letter_word = [word for word in words if len(word) == 3]
    return three_letter_word


user_input = input("请输入一段英文文本: ")

corrected_user_input_1 = ""
for char in user_input:
    if char.isalpha() or char.isspace():
        corrected_user_input_1 += char

three_letter_words = find_three_letter_words(corrected_user_input_1)
print("长度为3个字母的单词有:", three_letter_words)
