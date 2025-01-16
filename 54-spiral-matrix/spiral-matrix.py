class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num_row, num_col = len(matrix),len(matrix[0])
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        total = num_row*num_col
        count = 0
        i,j = 0,0
        dir_index = 0
        visited = set()
        ans = []
        while count<total:
            visited.add((i,j))
            ans.append(matrix[i][j])
            count+=1

            d_i,d_j = direction[dir_index]
            i_next,j_next = i+d_i, j+d_j
            if i_next<0 or i_next==num_row or j_next<0 or j_next==num_col or (i_next,j_next) in visited:
                dir_index+=1
                dir_index=dir_index%4
            d_i,d_j = direction[dir_index]
            i+=d_i
            j+=d_j

        return ans
