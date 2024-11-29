class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = [0]*len(digits)
        for i in range(len(digits)-1,-1,-1):
            total = digits[i]+carry
            carry,num = divmod(total,10)
            ans[i]=num
        if carry!=0:
            ans = [carry]+ans
        return ans