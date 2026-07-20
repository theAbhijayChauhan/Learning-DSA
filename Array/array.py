from array import *     #Better to import like this so no need to write the function name everywhere !
# import array as arr

val = array('i', [1,2,3,4,5,6,7,8,9])

# for i in range(0,6):
#     print(val[i], end = " ")
    

# print("\n")
# val.reverse()
# for i in range(0, len(val)):
#     print(val[i], end = ", ")

# val.insert(1, 90)       # Add a new element

# val.append(100)         # Adds an element in last

# val[2] = 50             # Replaces the element
# print("\n")
# for i in range(0, len(val)):
#     print(val[i], end = ", ")
    

# copyArray = array(val.typecode, (x*2 for x in val))
# for i in range(0, len(copyArray)):
#     print(copyArray[i], end = " ")
    
# print()

# val.remove(3)       # Removes the element with element name parameter
# val.pop(3)          # Deletes the index of passed parameter
# val.pop()           # Deletes the last index only
# for i in range(0,len(val)):
#     print(val[i], end = " ")
    
# a = val[2 : -3]
# a = val[::-1]
# for i in range(0, len(a)):
#     print(a[i], end = " ")



# arr = array("i", [])
# n = int(input("Enter a number : "))

# for i in range(0, n):
#     arr.append(int(input(f"Enter the {i} number : ")))

# for j in arr:
#     print(j, end= " ")


arr = array("i", [1,2,3,4,5,6,7,8,9])
i = arr.index(6)
print(i)
