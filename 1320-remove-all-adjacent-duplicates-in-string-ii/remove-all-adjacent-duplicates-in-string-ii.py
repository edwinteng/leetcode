class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for char in s:
            if st and  char == st[-1][0]:
                c, freq = st.pop()
                if freq<k-1:
                    st.append((c,freq+1))
            else:
                st.append((char,1))
        ans = []
        for char,freq in st:
            for i in range(freq):
                ans.append(char)
        return ''.join(ans)
