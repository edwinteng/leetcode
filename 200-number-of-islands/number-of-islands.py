from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row,num_col = len(grid),len(grid[0])
        visited = set()
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))
            while q:
                cur_i,cur_j = q.popleft()
                for d_i,d_j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    next_i,next_j = cur_i+d_i,cur_j+d_j
                    if 0<=next_i < num_row and 0<=next_j<num_col and grid[next_i][next_j]=='1' and (next_i,next_j) not in visited:
                        q.append((next_i,next_j))
                        visited.add((next_i,next_j))
        num_island=0
        for i in range(num_row):
            for j in range(num_col):
                if (i,j) not in visited and grid[i][j]=='1':
                    bfs(i,j)
                    num_island+=1
        return num_island

        


            