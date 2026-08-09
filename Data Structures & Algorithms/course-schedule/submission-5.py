class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = defaultdict(list)

        for courses, preqs in prerequisites:
            indegree[preqs]+=1
            adj[courses].append(preqs)

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        finished_courses = 0
        while q:
            node = q.popleft()
            finished_courses+=1

            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return finished_courses == numCourses
            