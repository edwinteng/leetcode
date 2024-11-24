import random
class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            index = len(self.lst)
            self.hash[val] = index
            self.lst.append(val)
            #print('add:'+str(self.lst))
            return True
    def remove(self, val: int) -> bool:
        if val in self.hash:
            index = self.hash[val]
            #last_index = self.hash[self.lst[-1]]
            self.hash[self.lst[-1]]=index
            self.lst[index],self.lst[len(self.lst)-1]=self.lst[len(self.lst)-1],self.lst[index]
            self.lst.pop()
            del self.hash[val]
            #print('remove:'+str(self.lst))
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