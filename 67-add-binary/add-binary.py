class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        ans = ''
        while i >=0 or j>=0 or carry:
            cur_sum = carry
            if i>=0:
                cur_sum+=int(a[i])
            if j>=0:
                cur_sum+=int(b[j])
            carry,digit = divmod(cur_sum,2)
            ans=str(digit)+ans
            i-=1
            j-=1
        return ans