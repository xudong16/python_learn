import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


input_file = 're_test.txt'
output_image = 'wordcloud.png'
font_path = 'msyh.ttc'
width = 800
height = 400
background_color = 'white'
try:
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print(f"文件 {input_file} 未找到，请检查文件路径。")
    exit(1)
except Exception as e:
    print(f"读取文件时发生错误: {e}")
    exit(1)

word_list = jieba.lcut(text)
word_string = " ".join(word_list)

wordcloud = WordCloud(
    font_path=font_path,
    width=width,
    height=height,
    background_color=background_color
).generate(word_string)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

wordcloud.to_file(output_image)
print(f"词云图片已保存到 {output_image}")