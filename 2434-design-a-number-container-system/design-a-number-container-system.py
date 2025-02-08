from collections import defaultdict
from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.containerMap = {}
        self.numberIndices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.containerMap:
            old_number = self.containerMap[index]
            self.numberIndices[old_number].remove(index)
        self.containerMap[index] = number
        self.numberIndices[number].add(index)

    def find(self, number: int) -> int:
        s =  self.numberIndices[number]
        return s[0] if s else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)