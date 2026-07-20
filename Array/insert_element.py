from array import *

arr = array("i", [10,20,30,40,50,60,70,80,90])

position = 5
value = 55

#  Copy the new array
new_arr = array("i")

#  Copy all the elements before the position
for i in range(position):
    new_arr.append(arr[i])

#  Add the element
new_arr.append(value)

#   Copy the remaining elements
for i in range(position, len(arr)):
    new_arr.append(arr[i])

print(new_arr)