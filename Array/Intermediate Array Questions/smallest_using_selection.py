from array import*

arr = array("i", [45, 12, 8, 60, 30])

smallest = 0
for i in range(1, len(arr)):
    if arr[i] < arr[smallest]:
        smallest = i

print(arr[smallest])