import matplotlib.pyplot as plt
plt.rc("font", family='YouYuan')

countries = ['美国', '中国', '日本', '德国', '韩国', '法国', '英国', '澳大利亚', '加拿大', '意大利', '瑞士', '以色列',
             '荷兰', '巴西', '瑞典', '其他国家']
research_funds = [6075, 4680, 1264, 1189, 697, 638, 544, 309, 285, 280, 266, 237, 208, 197, 177, 2506]

total_funds = sum(research_funds)

percentages = [round((fund / total_funds) * 100, 2) for fund in research_funds]

fig, ax = plt.subplots()
ax.pie(research_funds, labels=countries, autopct='%1.1f%%', startangle=90)

ax.set_title('2021年全球国家科研经费占比')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
