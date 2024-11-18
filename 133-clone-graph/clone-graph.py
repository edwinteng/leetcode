"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def bfs(node):
            
            
            #clone_node.neighbors = vertex.neighbors
            
            clone[node.val] = Node(node.val,[])
            queue = deque([node])
            while len(queue):
                cur_node = queue.popleft()
                for nei in cur_node.neighbors:
                    if nei.val not in clone:
                        clone[nei.val] = Node(nei.val,[])
                        queue.append(nei)
                    
                    clone[cur_node.val].neighbors.append(clone[nei.val])
            return clone[node.val]
        return bfs(node) if node  else None 