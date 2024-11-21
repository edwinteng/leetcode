class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        #self.size = 0

        self.head,self.tail = Node(0,0),Node(0,0)
        self.head.next = self.tail
        self.tail.prev= self.head

    def remove(self,node):
        pre,nxt = node.prev,node.next
        #print('remove '+str(node.key))
        pre.next = nxt
        nxt.prev = pre
    def add(self,node):
        pre,nxt = self.head,self.head.next
        pre.next = node
        nxt.prev = node
        node.prev = pre
        node.next = nxt
        #prev, nxt = self.tail.prev, self.tail
        #prev.next = nxt.prev = node
        #node.next, node.prev = nxt, prev
        #print('heads next'+str(self.head.next.key))
        #print('tail prev'+str(self.tail.prev.key))
        #print('add '+str(node.key))
    def get(self, key: int) -> int:
        if key in self.cache:
            #print('get '+str(key))
            node = self.cache[key]
            #remove node from queue
            self.remove(node)
            # add to the beginning
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:


        if key in self.cache:
            #remove node from queue
            #node = self.cache[key]
            self.remove(self.cache[key])
        #else:
        #    self.size+=1
        #print('put '+str(key))
        #update node
        self.cache[key] = Node(key,value)
        #add to the beginning
        self.add(self.cache[key])
        #if it is over capacity
        if len(self.cache)>self.capacity:
        # remove the last item
            node = self.tail.prev
            #print(self.tail.prev.key)
            self.remove(node)
            del self.cache[node.key]

            #self.size-=1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)