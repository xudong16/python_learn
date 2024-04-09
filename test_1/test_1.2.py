lstA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lstB = [1, 2, 3, 4, 5, 6, 7]
mydict = {}
min_len = min(len(lstA), len(lstB))
for i in range(0, min_len):
    mydict[lstA[i]] = lstB[i]
print(mydict)
