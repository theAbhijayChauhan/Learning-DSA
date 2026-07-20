from array import *

arr = array("i", [10,20,30,40,50,60,70,80,90,95])

key = 60

low = 0
high = len(arr)-1
found =  False

while low <= high:
    mid = (high + low)//2
    
    if arr[mid] == key:
        print("Element found at index: ", mid)
        found = True
        break
    
    elif key < arr[mid]:
        high = mid -1
    else:
        low = mid +1
        
if found == False:
    print("Element not found")