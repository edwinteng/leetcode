class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course]+=1
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        num_course = 0
        while q:
            course = q.popleft()
            num_course+=1
            for next_course in adj[course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        return num_course == numCourses