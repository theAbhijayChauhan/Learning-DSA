from array import *

arr = array('i', [10, -5, 7, -2, 0, 8, -9])

pos = []
neg = []

for i in range(len(arr)):
    if arr[i] < 0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])

print(pos)
print(neg)