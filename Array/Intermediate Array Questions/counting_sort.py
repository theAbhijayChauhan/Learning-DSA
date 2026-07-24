arr = [4, 2, 2, 8, 3, 3, 1]

maximum = arr[0]

# Find the largest element
for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
count = [0] * (maximum + 1)    

# Count Occurences
for i in range(len(arr)):
    count[arr[i]] += 1
index = 0

# Build the sorted Array
for i in range(len(count)):
    while count[i] > 0:
        arr[index] = i
        index += 1
        count[i] =- 1

print(arr)