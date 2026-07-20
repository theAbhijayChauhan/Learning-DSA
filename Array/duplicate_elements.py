from array import *

arr = array("i", [10,20,30,40,50,40,10,60])

visited = []

# for i in range(len(arr)):
#     if arr[i] in visited:
#         continue
#     count = 0
    
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
    
#     if count > 1:
#         print("Duplicate Values :",arr[i])
    
#     visited.append(arr[i])
    
    
    
    
    
    
#   Remove Duplicate values
new_arr = array("i")
for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
print(new_arr)


duplicate = False

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        
        if arr[i] == arr[j]:
            duplicate = True
            break
    
    if duplicate == False:
        break

if duplicate:
    print("Duplicates Found")
else:
    print("No Duplicates")