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
        visited = {}
        def dfs(cur_node):
            if cur_node in visited:
                return visited[cur_node]
            clone_node = Node(cur_node.val)
            visited[cur_node] = clone_node
            clone_node.neighbors = []
            for nei in cur_node.neighbors:
                clone_node.neighbors.append(dfs(nei))
            return clone_node
        return dfs(node) if node else None
            
