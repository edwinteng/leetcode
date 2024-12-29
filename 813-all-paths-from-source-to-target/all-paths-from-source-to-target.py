class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        allpath = []
        q = deque([[0]])
        while q:
            path = q.popleft()
            node = path[-1]
            if path[-1] == len(graph)-1:
                allpath.append(path)
                continue
            for child in graph[node]:
                q.append(path+[child])
        return allpath

