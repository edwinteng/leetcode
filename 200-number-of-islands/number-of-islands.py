from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row,num_col = len(grid),len(grid[0])
        visited = set()
        
        def bfs(x,y):
            q = deque([(x,y)])
            visited.add((x,y))
            while q:
                cur_i,cur_j = q.popleft()
                for d_i,d_j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    i,j = cur_i+d_i,cur_j+d_j
                    if 0<=i < num_row and 0<=j<num_col and grid[i][j]=='1' and (i,j) not in visited:
                        q.append((i,j))
                        visited.add((i,j))
        num_island = 0
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j]=='1' and (i,j) not in visited:
                    bfs(i,j)
                    num_island+=1
        return num_island


            