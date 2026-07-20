from array import *

arr = array("i", [10,52,14,36, 0,14,89,84,73])
# largest = arr[0]
# smallest = arr[0]
# for i in range(0,len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
#     if arr[i] < smallest:
#         smallest = arr[i]

# print("Largest element = ",largest)
# print("Smallest element = ",smallest)





# arr = array("i", [10,50,60,52,39,57,96,32,14])

# smallest = arr[0]
# second = arr[0]
# for i in range(1, len(arr)):
#     if arr[i] < smallest:
#         second = smallest
#         smallest = arr[i]
#     elif arr[i] < smallest and arr[i] != smallest:
#         second = arr[i]

# print("Second smallest - ", second)




# arr = array("i", [10,20,30,40,50])
# total = 0
# for i in range(0, len(arr)):
#     total += arr[i]
# print(total)





# arr = array("i", [10,52,14,36,14,89,84,73])
# sum = 0
# for i in range(0, len(arr)):
#     sum += arr[i]
# avg = sum/len(arr)
# print(avg)






# even = 0
# odd = 0
# for i in range(0, len(arr)):
#     if arr[i]%2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even numbers are : ", even)
# print("Odd numbers are : ", odd)






# Reverse an array
# for i in range(len(arr)-1, -1, -1):
#     print(arr[i], end=" ")






# Rotate left by oen position
# first = arr[0]
# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]
# arr[len(arr)-1] = first
# print(arr)

#  Rotate Right by one position
# last = arr[len(arr)-1]
# for i in range(len(arr)-1, 0, -1):
#     arr[i] = arr[i-1]
# arr[0] = last
# print(arr)







# sorted_array = True
# for i in range(len(arr)-1):
#     if arr[i] > arr[i + 1]:
#         sorted_array = False
#         break

# if sorted_array:
#     print("Array is sorted")
# else:
#     print("Array not sorted")








# largest = arr[0]
# index = 0
# for i in range(1, len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
#         index = i
# print("Index -", index)

# smallest = arr[0]
# index = 0
# for i in range(1, len(arr)):
#     if arr[i] < smallest:
#         smallest = arr[i]
#         index = i
# print("Index -", index)







# old = 10
# new = 99
# for i in range(len(arr)):
#     if arr[i] == old:
#         arr[i] = new
# print(arr)








for i in range(len(arr)):
    if arr[i] == 0:
        # arr.insert(len(arr), arr[i])
        arr.append(arr[i])
        arr.pop(i)
print(arr)