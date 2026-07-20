from array import *

neg_arr = array("i", [5,-6,8,2,5,-4,-9,1,-7])
arr = array("i", [5,6,8,2,5,4,9,1,7])

new_arr = []


#  Move Negative numbers to beginning
# for i in range(len(neg_arr)):
#     if neg_arr[i] < 0:
#         neg_arr.append(neg_arr[i])

# for i in range(len(neg_arr)):
#     if neg_arr[i] >= 0:
#         neg_arr.append(neg_arr[i])

# print(new_arr)




# Move even numbers before odd
for i in range(len(arr)):
    if arr[i]%2 == 0:
        new_arr.append(arr[i])

for i in range(len(arr)):
    if arr[i]%2 != 0:
        new_arr.append(arr[i])

print(new_arr)