## Sum of each Row
# from numpy import *

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    total = 0
    for j in range(len(matrix[i])):
        total += matrix[i][j]
            
    print("Row", i + 1, "Sum =", total)
    
for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][j]

    print("Column", j + 1, "Sum =", total)