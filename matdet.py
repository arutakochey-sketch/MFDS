def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    det = 0
    for col in range(n):
        minor = []
        for i in range(1,n):
            row = []
            for j in range(n):
                if j != col:
                    row.append(matrix[i][j])
            minor.append(row)
        det += (-1)**col*matrix[0][col]*determinant(minor)
    return det
n = int(input("Enter size of matrix: "))
matrix = []
for i in range(n):
    row = list(map(int,input(f"Enter row {i+1}: ").split()))
    matrix.append(row)
print("Matrix:",matrix)
print("Determinant:",determinant(matrix))