class OrderedStream:

    def __init__(self, n: int):
        self.size = n
        self.data = [None]*(self.size+1)
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.data[idKey] = value
        for i in range(self.cur,self.size+1):
            if self.data[i] is None:
                return ans
            else:
                ans.append(self.data[i])
                self.cur+=1
        return ans



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)