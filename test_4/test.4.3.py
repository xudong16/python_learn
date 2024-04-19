import random

random_list = [random.randint(1, 1000) for _ in range(1000)]

odd_numbers_list = [num for num in random_list if num % 2 != 0]

print("只包含奇数的列表:", odd_numbers_list)
