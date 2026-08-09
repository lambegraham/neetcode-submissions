class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for course, preq in prerequisites:
            indegree[preq] +=1
            adj[course].append(preq)

        q = deque()
        #add all our courses with no preq's to q
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        #track our finished courses
        finished_courses = 0
        while q:
            node = q.popleft()
            finished_courses+=1
            #find nei, reduce indegrees
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return finished_courses == numCourses
            