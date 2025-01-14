class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for i in range(len(spells)):
            left = 0
            right = len(potions)
            while left < right:
                mid= left+ (right-left)//2
                if potions[mid]*spells[i] < success:
                    left=mid+1
                else:
                    right = mid
            ans.append(len(potions)-left)
        return ans