class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        completed = 0

        for course, preq in prerequisites: #adj list
            indegrees[preq] += 1
            adj[course].append(preq)

        #=== BFS ===
        q = deque()
        #want to queue the courses with no preq's
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
        
        while q:
            node = q.popleft() #our completed course
            completed+=1 #add completed

            for nei in adj[node]: #find nei's
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return completed == numCourses






