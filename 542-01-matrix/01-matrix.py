class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q=deque()
        num_col = len(mat[0])
        num_row= len(mat)
        ans = [[-1]*num_col for _ in range(num_row)]
        for i in range(num_row):
            for j in range(num_col):
                if mat[i][j]==0:
                    ans[i][j]=0
                    q.append((i,j))
    
        while q:
            i,j = q.popleft()
            for d_i,d_j in [(1,0),(0,1),(-1,0),(0,-1)]:
                cur_i,cur_j = i+d_i,j+d_j
                
                if 0<=cur_i<num_row and 0<=cur_j<num_col and ans[cur_i][cur_j]==-1:
                   
                    ans[cur_i][cur_j]=ans[i][j]+1
                    q.append((cur_i,cur_j))
        return ans