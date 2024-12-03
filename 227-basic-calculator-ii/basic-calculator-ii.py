class Solution:
    def calculate(self, s: str) -> int:
        st = []
        value = 0
        prev_sign = '+'

        for i,char in enumerate(s):
            if char.isnumeric():
                value=value*10+int(char)
            if i==len(s)-1 or char in '+-*/':
                if prev_sign == '+':
                    st.append(value)
                if prev_sign == '-':
                    st.append(-value)
                if prev_sign == '*':
                    pop_value = st.pop()
                    st.append(pop_value*value)
                if prev_sign == '/':
                    pop_value = st.pop()
                    st.append(int(pop_value/value))
                value = 0
                prev_sign = char
        print(st)
        return sum(st)
