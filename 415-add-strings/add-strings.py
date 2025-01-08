class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        str1 = num1[::-1]
        str2 = num2[::-1]

        i,j = 0,0
        carry, tmp = 0,0
        ans = ''
        while i < len(str1) or j < len(str2) or carry:
            tmp=carry
            if i < len(str1):
                tmp+=int(str1[i])
            if j < len(str2):
                tmp+=int(str2[j])
            carry,digit=divmod(tmp,10)
            ans= ans+str(digit)
            i+=1
            j+=1
        return ans[::-1]
