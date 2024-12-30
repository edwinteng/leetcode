class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            indegree[course]+=1
            adj[pre].append(course)
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        course_seq = []
        while q:
            course = q.popleft()
            course_seq.append(course)
            for next_course in adj[course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        return numCourses == len(course_seq)