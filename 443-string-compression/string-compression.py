class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        cur_len= 0
        fast,slow = 0,0
        while fast < len(chars):

            while fast < len(chars) and chars[slow] == chars[fast]:
                fast+=1
                
            length = fast-slow
            chars[cur_len] = chars[slow]
            cur_len+=1
            if length >1:
                #convert number to string
                int_str = str(length)
                for i in range(len(int_str)):
                    chars[cur_len+i] = int_str[i]
                cur_len+=len(int_str)
            slow = fast
        return cur_len