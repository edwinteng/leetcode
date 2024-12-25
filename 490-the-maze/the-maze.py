from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        num_row = len(maze)
        num_col = len(maze[0])
        q = deque([start])
        visited = set()
        visited.add((start[0],start[1]))
        while q:
            i,j = q.popleft()
            for d_i,d_j in [(1,0),(0,1),(-1,0),(0,-1)]:
                cur_i,cur_j = d_i+i,d_j+j
                while 0<=cur_i<num_row and 0<=cur_j<num_col and maze[cur_i][cur_j]!=1:
                    cur_i+=d_i
                    cur_j+=d_j
                cur_i-=d_i
                cur_j-=d_j
                if [cur_i,cur_j] == destination:
                    return True
                if (cur_i,cur_j) not in visited:
                    q.append((cur_i,cur_j))
                    visited.add((cur_i,cur_j))
        return False
            
