class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum = derived[0]
        for i in range(1,len(derived)):
            xor_sum ^= derived[i]
        return True if xor_sum == 0 else False