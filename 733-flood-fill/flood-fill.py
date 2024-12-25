class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        num_rol,num_col=len(image),len(image[0])
        origin_color = image[sr][sc]
        visited = set()
        q = deque([(sr,sc)])
        image[sr][sc]=color
        while q:
            cur_r,cur_c = q.popleft()
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nei_r,nei_c = cur_r+dr,cur_c+dc
                if 0<=nei_r<num_rol and 0<=nei_c<num_col and (nei_r,nei_c) not in visited and image[nei_r][nei_c] == origin_color:
                    visited.add((nei_r,nei_c))
                    image[nei_r][nei_c]=color
                    q.append((nei_r,nei_c))
        return image