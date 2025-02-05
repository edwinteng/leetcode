class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        
        increase,decrease,ans = 0,0,0
        i=0
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                i+=1
            increase = 0
            decrease = 0
            while i < len(arr)-1 and  arr[i]<arr[i+1]:
                increase+=1
                i+=1
            while i < len(arr)-1 and arr[i]>arr[i+1]:
                decrease+=1
                i+=1
            if increase >0 and decrease > 0:
                ans = max(ans,increase+decrease+1)
        return ans

            
