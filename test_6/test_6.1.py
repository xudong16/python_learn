number = input("please input the origin people number:")
number = int(number)
value_k = input("please input the origin value_k:")
value_k = int(value_k)
numbers = list(range(1, int(number)+1))
while 1:
    if number >= value_k:
        key = numbers.pop(value_k-1)
        number -= 1
    else:
        key = numbers.pop(value_k % number - 1)
        number -= 1
    if number <= 0:
        break
print(f"the end is {key}")
