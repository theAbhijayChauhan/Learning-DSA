## Find the Pair with the Largest Sum

from array import *

# arr = array('i', [10, 25, 8, 45, 60])

# largest_sum = arr[0] + arr[1]

# first = arr[0]
# second = arr[1]

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] > largest_sum:
#             largest_sum = arr[i] + arr[j]
#             first = arr[i]
#             second = arr[j]

# print("Pair =", first,"&", second)
# print("Largest Sum =", largest_sum)





# # Sum All Pairs 
# arr = array('i', [10, 20, 30, 40, 50, 60])
# largest_sum = arr[0] + arr[1]

# first = arr[0]
# second = arr[1]

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         sum = arr[i] + arr[j]
#         print(arr[i],"+", arr[j],"=", sum)
        
        
        
        
        
        


# Count All Pairs Having a the same given Sum
arr = array('i', [10, 20, 30, 40, 50, 60])

target = 70

count = 0
# Compare every pair
for i in range(len(arr)):
    
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            count += 1
            print(arr[i], arr[j])
        
print("Total Pairs =", count)