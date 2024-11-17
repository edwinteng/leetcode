from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        def get_neighbor(coord):
            delta_r = [1,-1,0,0]
            delta_c = [0,0,1,-1]
            r,c = coord
            res = list()
            for i in range(len(delta_r)):
                neighbor_r = r+delta_r[i]
                neighbor_c = c+delta_c[i]
                if 0<=neighbor_r<num_row and 0<=neighbor_c<num_col:
                    res.append((neighbor_r,neighbor_c))
            return res
        def bfs(start):
            queue = deque([start])
            while len(queue)>0:
                coord = queue.popleft()
                for neighbor in get_neighbor(coord):
                    r,c = neighbor
                    if grid[r][c] == '1':
                        queue.append(neighbor)
                        grid[r][c] = '0'
        num_island = 0
        for  i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == '1':
                    bfs((i,j))
                    num_island+=1
        return num_island


            