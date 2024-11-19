class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [[1,'I'],[4,'IV'],[5,'V'],[9,'IX'],[10,'X'],[40,'XL'],[50,'L'],[90,'XC'],[100,'C'],[400,'CD'],[500,'D'],[900,'CM'],[1000,'M']]
        
        ans = ''
        for i in range(len(mapping)-1,-1,-1):
            carry,remainder = divmod(num,mapping[i][0])
            num = remainder
            for j in range(carry):
                ans = ans +mapping[i][1]
        return ans
