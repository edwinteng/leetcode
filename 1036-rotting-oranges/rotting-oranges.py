class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_row = len(grid)
        num_col = len(grid[0])
        mins = 0
        fresh = 0
        q = deque()
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        while q and fresh>0:
            for _ in range(len(q)):
                i,j = q.popleft()
                for d_i,d_j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    cur_i,cur_j = i+d_i,j+d_j
                    
                    if 0<=cur_i<num_row and 0<=cur_j<num_col and grid[cur_i][cur_j]==1:
                        print(str(mins)+':'+str(cur_i)+':'+str(cur_j))
                        grid[cur_i][cur_j]=2
                        q.append((cur_i,cur_j))
                        fresh-=1
            print(q)
            mins+=1
        return mins if fresh==0 else -1