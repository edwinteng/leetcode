class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for char in s:
            if len(st) >0:
                topchar,freq = st[-1]
                if topchar == char:
                    st.pop()
                    if freq < k-1:
                        st.append((char,freq+1))
                else:
                    st.append((char,1))
            else:
                st.append((char,1))
        ans = []
        for char,freq in st:
            for _ in range(freq):
                ans.append(char)
        return ''.join(ans)