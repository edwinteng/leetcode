class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = Counter(arr)
        ans = arr[0]
        for key,val in d.items():
            if val>=len(arr)*0.25:
                ans = key
        return ans