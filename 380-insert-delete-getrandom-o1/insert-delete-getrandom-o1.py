
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
            #Update Hash table
            # swap hash table value
            index = self.hash[val]
            val_swap = self.lst[-1]
            self.hash[val_swap]= index
            # delete the element in hash table
            del self.hash[val]
            # Update list
            # Swap the last element and the element in the list
            # pop the last element
            self.lst[index],self.lst[-1]=self.lst[-1],self.lst[index]
            self.lst.pop()
            return True


    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()