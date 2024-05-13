import numpy as np

vector = np.array([-2, -1, 0])
vector2D = np.array([[1, 2, 3]]) # 3 Columns, 1 row

matrix = np.array([[4, 5, 6], [7, 8, 9]]) # 3 coumns two rows
matrix2 = np.array([[10, 11, 12], [13, 14, 15]])

# print(matrix * matrix) # Multiply value for value
# print(matrix ** matrix) # raise to the matrices value
# print(matrix < matrix2) # Boolean expressions
# print(matrix @ matrix.T) # Dot product (.T transposed, rows to columns)

idx = ([[1],[0, 2]]) # Pulls elements of an array (Second row, elements 0 & 1)
print(matrix)
print(matrix.shape)
print()
print(matrix.reshape(1, 6))
