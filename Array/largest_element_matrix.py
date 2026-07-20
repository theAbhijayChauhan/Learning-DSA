matrix = [
    [12, 45, 8],
    [30, 60, 15],
    [25, 10, 40]
]

largest = matrix[0][0]

for i in range(len(matrix)):
    
    for j in range(len(matrix[i])):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            
print("Largest =", largest)