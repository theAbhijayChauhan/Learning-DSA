from array import *

arr =array("i", [10,20,1,95,20,73,20,30,20])

visited = []

for i in range(len(arr)):
    if arr[i] in visited:
        continue
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count +=1
    print(arr[i], "-->", count)
    # Mark the element as counted
    visited.append(arr[i])







# Method 2: Dictionary (EVEN BETTER for interviews)
def count_frequency_dict(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for key, val in freq.items():
        print(key, '-->', val)

# Method 3: Using Counter (Only if interviewer allows)
from collections import Counter
def count_frequency_counter(arr):
    return Counter(arr)





#   Most Frequency of an element

max_count = 0
element = 0

for i in range(len(arr)):
    if arr[i] in visited:
        continue
    count = 0
    
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
        
    if count > max_count:
        max_count = count
        element = arr[i]
    
    visited.append(arr[i])

print("Most Frequent Element =", element)
print("Frequency =", max_count)