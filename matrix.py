import numpy as np 

a = np.array([1,2,3])
print(a)
type(a)

B = np.array([[1,2,3],[4,5,6]])
print(B)

# array float
C = np.array([[1.1 , 2.5 , 3.5],[1,4,6.7]])
print(C)

# # Array of complex numbers(so phuc)
B = np.array([[1,2,3],[4,5,6]],dtype=complex)
print(B)

# print maxtrix 0 

zeros_matrix = np.zeros((3,3))
print(zeros_matrix)

#  matrix 1 
one_matrix = np.ones((1,3),dtype=np.int32)
print(one_matrix)

# arange tra ra do dai cua m * n matrix 1 chieu
E = np.arange(5)
print(f'E = {E}')
# reshape 
A1 = np.arange(10).reshape(2,5)
print(f'A1 = {A1}')

#  matrix operation
A2 = np.array([[1,0],[2,1]])
B2 = np.array([[2,4],[1,-3]])
D2 = np.array([[3,2],[0,1]])
# nhan 2 ma tran
c3 = np.dot(A2,B2)
d3 = D2.dot(B2)
# cong 2 matrix
c2 = A2 + B2
print(f"c3 = {c3}")
print(f"c2 = {c2}")
print(f"d3 = {d3}")

# matrix tranpose : .T or .transpose()
tranpose_matrixA1 = A1.T
print(tranpose_matrixA1)

# Access matrix elements
R = np.array([2,4,6,8,10])
print(R[0]) 
# 2
print(R[-1])
# 10
print(R[3])
# 8

R1 = np.array([[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

print(f'R1[0][0] = {R1[0][0]}') # 1
print(f'R1[1][2] = {R1[1][2]}') # 9
print(f'R1[-1][-1] = {R1[-1][-1]}') # 19

# row of matrix
print(f'R1[0] = {R1[0]}') # row 1 of matrix R1
print(f'R1[2] = {R1[2]}') # row 3 of matrix R1
print(f'R1[-1] = {R1[-1]}') # row 3 of matrix R1
# columns of matrix
print(f'R1[:,0] = {R1[:,0]}') # column 1 of matrix R1
print(f'R1[:,3] = {R1[:,3]}') # column 4 of matrix R1
print(f'R1[:,-1] = {R1[:,-1]}') # column 4 of matrix R1

#Slicing of a Matrix 
letter = np.array([1,3,5,7,9,7,11])
print(letter[2:5])
print(letter[:5])
print(letter[::-1])

A4 = np.array([ [1, 4, 5, 12, 14], 
                [-5, 8, 9, 0, 17],
                [-6, 7, 11, 19, 21]])

# 2 row and 4 column
print(A4[:2,:4])
# first row and all columns
print(A4[:1,])
# all row , 3 column
print(A4[:,2])
# all row , 3 colums end
print(A4[:,2:5])