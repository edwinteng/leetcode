class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def dfs(index,total,path):
            if total>target or index>len(candidates):
                return
            #while index-1>=0 and candidates[index]==candidates[index-1]:
            #    index+=1
            if total==target:
                ans.append(path)
                return
            #1 1 2 5 6 7
            #0 0 

            for i in range(index,len(candidates)):
                if i!=index and candidates[i]==candidates[i-1]:
                    continue
                dfs(i+1,total+candidates[i],path+[candidates[i]])
                    #continue
                #if index <len(candidates) and total<target:
                #dfs(i+1,total+candidates[i],path+[candidates[i]])
                #dfs(index+1,total,path)
        dfs(0,0,[])
        return ans
        