# Linear Algebra & Statistics common scripts.
# Scripts primarily come from Jason Brownlee's "Linear Algebra for Machine Learning"

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
from numpy import var
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
row_var = var(M, ddof=1, axis=1) # Unbiased Sample Variance where ddof is degrees of freedom
row_var1 = var(M, axis=1) # Population Variance
row_std = std(M, ddof=1, axis=1) # Unbiased Sample Standard Deviation for rows
row_std1 = std(M,axis=1) # Population Standard Deviation for rows
print(row_var)
print(row_var1)
print(row_std)
print(row_std1)

#%%
# covariance matrix
from numpy import array
from numpy import cov
# define matrix of observations
X = array([
  [1, 5, 8],
  [3, 5, 11],
  [2, 4, 9],
  [3, 6, 10],
  [1, 5, 10]])
print(X)
print(X.T)
# calculate covariance matrix
Sigma = cov(X.T) # Need to transpose because cov() naturally calculates
                  # the covariance of the columns but your data came in as rowsxcolumns so you
                  # need your columns first.
print(Sigma)