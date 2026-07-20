from array import *

arr = array("i", [12,45,36,48,76,85,37,91,5])

key = 45
found = False
for i in range(len(arr)):
    if arr[i] == key:
        found = True
        print("Number found at index : ", i)
        break
if found == False:
    print("Element not found !")
