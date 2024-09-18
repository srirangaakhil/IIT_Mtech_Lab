import numpy as np
import pandas as pd
# you can import your favorite libraries here, as long as they run on SL2 machines

# Task 1
## create an nXn INTEGER matrix and store it with checkerboard pattern (using 0's and 1's). Top left corner should be 0. No loops. Assume n > 0.
def checkerboard(n):
    if n%2 == 0:
        x = np.arange((n+1)*(n+1)).reshape((n+1), (n+1))
    else:
        x = np.arange(n*n).reshape(n, n)
    y = x%2
    return y[:n, :n]

# Task 2
def LeakyReLU(arr, leak):
    return np.array(list(map(lambda i: i if i>0 else leak * i, arr.flatten())), dtype=np.float64).reshape(arr.shape)


# Task 3.1
## write a function to normalise an array of shape (m, n) along its columns. By normalise, we mean that mean of each column should be 0 and variance of each column is 1.
def normalise(arr):
    # compute mean (along columns) and reshape it into a row vector
    # then subtract this from each row of arr (let's call it mean_normalised)
    # then compute the std. deviation of the mean_normalised and reshape it into a row vector.
    # divide each row of mean_normalised by std.dev. to get the result.
    # write your code here
    temp = arr
    N = np.shape(temp[0])
    M = np.shape(temp[1])
    mean = np.mean(temp,0)
    std = np.std(temp, 0)
    temp[:]=temp[:]-mean
    temp[:] = temp[:] / std
    return temp
    
# Task 3.2
## Write a function mean_filter to implement a mean filter of 1-d array of shape (n,) and kernel size 2k+1. Output should be a float array. 
def mean_filter(arr, k):
    # write your code here
    temp = arr
    temp=np.pad(temp,k, 'constant', constant_values = 0 )
    n=(2*k+1)
    temp=[np.sum(temp[i:i + (2*k+1)]) for i in range(0, len(temp)-(2*k), 1)]
    sum = np.zeros(len(temp))
    sum=np.true_divide(temp,n)
    return sum

# Task 4 
# write a function to get the positions of top_k values of an each row of a matrix of shape (m,n).
"""
Concretely, if A is the input matrix of shape (m,n), then return an integer matrix R, such that:
R_{ij} is the index of an element in ith row of A which has rank j when that row is sorted in decreasing order. 
For example, if the input array ‘arr’ is:
[[ 6  4  4  7]
 [ 7  8  1  0]
 [11 10  5 11]]
Then top_k(arr, 2) will be:
[[3 0]
 [1 0]
 [3 0]]
Explanation for first row:
when we sort 6,4,4,7 in decreasing order, we get:
7, 6, 4, 4. Top 2 elements are 7 and 6. And, their positions in arr are: 3 and 0 respectively. 
So, the first row of result is 3,0.

Note: for breaking ties, higher indices should come first.(See the last row of result).
"""
def top_k(mat, k):
    return np.flip(np.argsort(mat, axis=1),1)[:,:k]

# Task 5
# write a function which takes an array of shape (n,n) and returns either True or False, depending on whether the input was a magic square or not.
def is_magic_square(square):
    # write your code here
    temp = square
    row = np.sum(temp, 0)
    col = np.sum(temp, 1)
    diag = np.trace(temp)
    row = np.unique(row)
    col = np.unique(col)
    uniq = np.unique(temp)
    if col.size == 1 and row.size == 1 and diag.size==1 and row[0] == col[0] and col[0] == diag and temp.size==uniq.size:
        return True
    return False

# Task 6
#### separate file, not here! ####