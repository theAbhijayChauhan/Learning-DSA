matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[i])):
        # Add corresponding elements
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Print the resultant matrix
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ")
print()






# Print Primary Diagonal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Primary diagonal has same row and column index
for i in range(len(matrix)):
    print(matrix[i][i], end=" ")
print()
    
    
    


# Print Secondary Diagonal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix)
# Secondary diagonal has row + column = n - 1
for i in range(n):
    print(matrix[i][n - i - 1], end=" ")