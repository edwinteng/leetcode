class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_row,num_col = len(matrix),len(matrix[0])
        row_first_zero = False
        for i in range(num_row):
            for j in range(num_col):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i ==0:
                        row_first_zero = True
                    else:
                        matrix[i][0] = 0
        for i in range(1,num_row):
            for j in range(1,num_col):
                if matrix[i][0] ==0 or matrix[0][j] ==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(num_row):
                matrix[i][0]=0

        if row_first_zero:
            for j in range(num_col):
                matrix[0][j]=0
        