from array import *

arr = array("i", [10,20,30,10,20,60,40,10,80,90])

# Occurence of an element
key = 10
count = 0
for i in range(len(arr)):
    if arr[i] == key:
        count += 1
        
print("Element occurred -",count)


for i in range(len(arr)):
    if arr[i] == key:
        print("First found at index-",i)
        break
    

    
for i in range(len(arr)-1,-1,-1):
    if arr[i] == key:
        print("Last found at index-",i)
        break