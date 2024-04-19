import random
random_list = [random.randint(1, 100) for _ in range(20)]
print("原始列表:", random_list)
random_list[:10] = sorted(random_list[:10])
random_list[10:] = sorted(random_list[10:], reverse=True)
print("处理后的列表:", random_list)
