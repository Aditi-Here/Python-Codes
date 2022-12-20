"""
Problem:
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. The task is to find whether element X is present in the matrix or not.


Example 1:

Input:
N = 3, M = 3
mat[][] = 3 30 38
         44 52 54
         57 60 69
X = 62
Output:
0
Explanation:
62 is not present in the
matrix, so output is 0

Example 2:

Input:
N = 1, M = 6
mat[][] = 18 21 27 38 55 67
X = 55
Output:
1
Explanation:
55 is present in the
matrix at 5th cell.

Approach:
The simple idea is to remove a row or column in each comparison until an element is
found. Start searching from the top-right corner of the matrix.
There are three possible cases:-

The given number is greater than the current number: This will ensure that all the elements in the current row are smaller than the given number as the pointer is already at the right-most elements and the row is sorted. Thus, the entire row gets eliminated and continues the search for the next row. Here, elimination means that a row needs not to be searched.
The given number is smaller than the current number: This will ensure that all the elements in the current column are greater than the given number. Thus, the entire column gets eliminated and continues the search for the previous column, i.e. the column on the immediate left.
The given number is equal to the current number: This will end the search.
"""
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
X=5
def findElementMatrix(arr):
    n = len(arr)
    i = 0
    j = n - 1
    while (i<n,j>=0):


        if arr[i][j]==X:
            return 1
        if arr[i][j]>X:
            j-=1
            pass
        else:
            i+=1
    return 0
ac=findElementMatrix(arr)
print(ac)

# the more better approach in terms of complexity is explain in theory part.