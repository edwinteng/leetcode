class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n ==0:
            return True
        visited = set()
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(cur,prev):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in adj[cur]:
                if nei != prev:
                    if not dfs(nei,cur):
                        return False
            return True
        return dfs(0,-1) and len(visited)==n

            