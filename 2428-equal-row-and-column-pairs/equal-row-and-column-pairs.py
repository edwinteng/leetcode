class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trans = [list(col) for col in zip(*grid)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(trans)):
                if trans[j] == grid[i]:
                    count+=1
        return count
