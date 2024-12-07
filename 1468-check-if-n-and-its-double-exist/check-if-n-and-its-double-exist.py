class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d= {}
        for element in arr:
            if element*2 in d or element/2 in d:
                return True
            else:
                d[element]=1
        return False