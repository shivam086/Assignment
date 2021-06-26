"""
1. A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class RobotGame:
    def unique_path(self, col, row):  # Function to get unique path
        matrix_table = [[0 for i in range(col)] for j in range(row)]
        print(matrix_table)
        # case 1: n = 1, only one way to traverse
        for j in range(col):
            matrix_table[0][j] = 1
        print(matrix_table)
        # case 2: col = 1, only one way to traverse
        for i in range(row):
            matrix_table[i][0] = 1
        print(matrix_table)
        for i in range(1, row):
            for j in range(1, col):
                matrix_table[i][j] = matrix_table[i-1][j] + matrix_table[i][j-1]
        print(matrix_table)
        return matrix_table[row-1][col-1]


m = int(input("Enter value of m (columns): "))  # To input columns no., m
n = int(input("Enter length of n (rows): "))  # To input rows no., n
obj = RobotGame()  # To create RobotGame instance
output_val = obj.unique_path(m, n)  # To call instance unique_path method
print("Unique path will be: ", output_val)  # To print output value


'''
EXPLANATION:
-----------
1. First, I take columns and rows value, m and n
2. As, we know, robot can only move right or down side at any point of time. So, 
  (a.) If m=1, there will be always only one unique path to get there. 
  (b.) Similarly, if n=1, there will be always only one unique path.
3. Now, for cases, if m>1 or n>1,
   In this case, we can compute unique path from adding the solutions of two previous results i.e. 
     (a.) The possible unique paths coming from the left.
     (b.) The possible unique paths coming from the top.

Essentially, matrix_table[n][m] = matrix_table[n-1][m] + matrix_table[n][m-1] for all n, m > 1.
4. Now, we will have updated matrix_table data. So, the result will be matrix_table[row-1][col-1]
'''