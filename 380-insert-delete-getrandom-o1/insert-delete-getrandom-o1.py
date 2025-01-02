
class RandomizedSet:
    # O(1) for insert:  any data structure
    # hash for O(1)
    # random list   random.choice()
    def __init__(self):
        self.hash = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val not in self.hash:
            self.hash[val] = len(self.lst)
            self.lst.append(val)
            return True
        else:

            return False

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        else:
            index = self.hash[val]
            val_last = self.lst[-1]
            self.hash[val_last] = index
            self.lst[index],self.lst[-1]=self.lst[-1],self.lst[index]

            del self.hash[val]
            self.lst.pop()
            return True


    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()