class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        finished_courses = 0
        output = []

        for course, preq in prerequisites:
            indegree[preq]+=1
            adj[course].append(preq)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            node = q.popleft()
            finished_courses+=1
            output.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        if numCourses != finished_courses:
            return []
        return output[::-1]