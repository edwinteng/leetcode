class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #bin(num2)[2:]:
        bit1 = num1.bit_count()
        bit2 = num2.bit_count()
        #if bit1 < bit2
        # add bit to num
        if bit1 < bit2:
            diff_bit = bit2-bit1
            #add right bit
            for i in range(diff_bit):
                num1 |= (num1+1)
        elif bit1 > bit2:
            diff_bit = bit1-bit2
            for i in range(diff_bit):
                num1 &= (num1-1)
            
        return num1