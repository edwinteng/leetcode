class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_row,num_col = len(board),len(board[0])
        
        def dfs(i,j,index):
            #end condition 
            if index==len(word)-1 and board[i][j]==word[index] :
                return True
            if word[index]!=board[i][j]:
                return False
            temp = board[i][j]
            board[i][j]='0'
            for d_i,d_j in [(0,1),(1,0),(0,-1),(-1,0)]:
                cur_i,cur_j = d_i+i,d_j+j
                if 0<=cur_i <num_row and 0<=cur_j<num_col:
                    if  board[cur_i][cur_j]!='0' and dfs(cur_i,cur_j,index+1):
                        return True
            board[i][j]=temp
            return False
        for i in range(num_row):
            for j in range(num_col):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False