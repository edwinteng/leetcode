class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[pre].append(course) 
            indegree[course]+=1
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        course_seq = []
        while q:
            cur_course = q.popleft()
            course_seq.append(cur_course)
            for next_course in adj[cur_course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        return course_seq if len(course_seq)==numCourses else []