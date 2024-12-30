
class RandomizedSet:
    # O(1) for insert:  any data structure
    # hash for O(1)
    # random list   random.choice()
    def __init__(self):
        self.hash = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.hash[val]= len(self.lst)
            self.lst.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.hash:

            index,last_index = self.hash[val],len(self.lst)-1
            last_val = self.lst[-1]
            self.hash[last_val] = index
            self.lst[index],self.lst[last_index]=self.lst[last_index],self.lst[index]
            self.lst.pop()
            del self.hash[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.lst)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()