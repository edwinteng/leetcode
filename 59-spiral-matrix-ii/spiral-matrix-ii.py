class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        i,j = 0,0

        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        dir_i = 0
        for index in range(n*n):
            #print('cur:'+str(i)+':'+str(j))
            ans[i][j] = index+1
            #print(ans)
            d_i,d_j = direction[dir_i]
            next_i,next_j = i+d_i, j+d_j
            #print(str(next_i)+':'+str(next_j))
        
            if next_i<0 or next_i==n or next_j < 0 or next_j==n or ans[next_i][next_j]!=0:
                dir_i+=1
                dir_i=dir_i%4
                #print(dir_i)

            d_i,d_j = direction[dir_i]
            #print(direction[dir_i])
            i=i+d_i
            j=j+d_j
            #print('end:'+str(i)+':'+str(j))
        return ans




