import random
first = second = third = 0
for _ in range(1, 10001):
    key = random.randint(0, 360)
    if key >= 108:
        third += 1
    else:
        if key >= 30:
            second += 1
        else:
            first += 1
print(F"the first is {first}, the second is {second},the third is {third}")
