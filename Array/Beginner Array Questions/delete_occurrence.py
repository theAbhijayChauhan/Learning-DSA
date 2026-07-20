from array import *

arr = array("i", [10,30,50,60,20,80,20,75,63])

target = 20

# for i in range(len(arr)):
#     if target == arr[i]:
#         arr.remove(target)
#         break
# print(arr)





i = 0
while i < len(arr):
    if arr[i] == target:
        arr.pop(i)  # Shifts elements left; don't change i
    else:
        i += 1  # Safe to move forward


# arr = array("i", [x for x in arr if x != target])         #Enhanced Loop
print(arr)