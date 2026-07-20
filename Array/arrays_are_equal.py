from array import *

arr1 = array('i', [10, 20, 30, 40])
arr2 = array('i', [10, 20, 30, 40])

equal = True

# Lengths must be equal

if len(arr1) != len(arr2):
    equal = False
else:
# Compare every element
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            equal = False
            break
if equal:
    print("Arrays are Equal")
else:
    print("Arrays are Not Equal")