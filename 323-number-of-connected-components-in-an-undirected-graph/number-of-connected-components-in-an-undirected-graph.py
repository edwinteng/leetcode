class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(n)]
        size = [1]*n

        def find(node):
            cur_node = node
            while cur_node != parent[cur_node]:
                parent[cur_node] = parent[parent[cur_node]]
                cur_node = parent[cur_node]
            return cur_node
        def union(node1,node2):
            node1_parent,node2_parent = find(node1),find(node2)
            if node1_parent==node2_parent:
                return 0

            if size[node1_parent]>size[node2_parent]:
                size[node1_parent]+=size[node2_parent]
                parent[node2_parent] = node1_parent
            else:
                size[node2_parent]+=size[node1_parent]
                parent[node1_parent] = node2_parent
            return 1        
        comp=n
        for node1,node2 in edges:
            comp-=union(node1,node2)
            #comp-=ans
        return comp