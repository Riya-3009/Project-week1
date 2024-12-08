# Input the dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input the first matrix
print("Enter the elements of the first matrix:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input the second matrix
print("Enter the elements of the second matrix:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

#ADDITION
result = [[0 for _ in range(cols)] for _ in range(rows)]
# Add the two matrices
for i in range(rows):
    for j in range(cols):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
# Display the result
print("The resultant matrix after addition is:")
for row in result:
    print(" ".join(map(str, row)))


#TRANSPOSE
# Input the dimensions of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input the matrix
print("Enter the elements of the matrix:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Initialize the transpose matrix
transpose = [[0 for _ in range(rows)] for _ in range(cols)]

# Transpose the matrix
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

# Display the transpose
print("The transpose of the matrix is:")
for row in transpose:
    print(" ".join(map(str, row)))



#MULTIPLICATION
# Input dimensions of the first matrix
rows1 = int(input("Enter the number of rows in the first matrix: "))
cols1 = int(input("Enter the number of columns in the first matrix: "))

# Input dimensions of the second matrix
rows2 = int(input("Enter the number of rows in the second matrix: "))
cols2 = int(input("Enter the number of columns in the second matrix: "))

# Ensure the matrices can be multiplied
if cols1 != rows2:
    print("Matrix multiplication is not possible. The number of columns in the first matrix must equal the number of rows in the second matrix.")
else:
    # Input the first matrix
    print("Enter the elements of the first matrix:")
    matrix1 = []
    for i in range(rows1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    # Input the second matrix
    print("Enter the elements of the second matrix:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(int, input().split()))
        matrix2.append(row)

    # Initialize the result matrix
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):  # or rows2
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display the resultant matrix
    print("The resultant matrix after multiplication is:")
    for row in result:
        print(" ".join(map(str, row)))


