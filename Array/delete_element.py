from array import *

arr = array("i", [10,20,30,100,40,90,80])

position = 3
new_arr = array("i")

# for i in range(position):
#     new_arr.append(arr[i])

# for i in range(position+1, len(arr)):
#     new_arr.append(arr[i])
# new_arr.pop(position)

# print(new_arr)


for i in range(len(arr)):
    if position != i:
        new_arr.append(arr[i])
print(new_arr)