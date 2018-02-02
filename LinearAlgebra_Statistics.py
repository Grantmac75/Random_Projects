# Linear Algebra & Statistics common scripts

#%%
# orthogonal matrix
from numpy import array
from numpy.linalg import inv
# define orthogonal matrix
Q = array([
[1, 0],
  [0, -1]])
print(Q)
# inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
# identity equivalence
I = Q.dot(Q.T)
print(I)

#%%
# matrix standard deviation
from numpy import array
from numpy import std
# define matrix
M = array([
  [1,2,3,4,5,6],
  [1,2,3,4,5,6]])
print(M)
# column standard deviations
col_std = std(M, ddof=1, axis=0)
print(col_std)
# row standard deviations
row_std = std(M, ddof=1, axis=1) # Unbiased Sample Standard Deviation for rows
row_std1 = std(M,axis=1) # Population Standard Deviation for rows
print(row_std)
print(row_std1)