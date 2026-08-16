class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for courses, preqs in prerequisites:
            indegree[courses] += 1 #has a preq
            adj[preqs].append(courses) #complete this first
        
        q = deque()
        #courses with no preqs take now
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        #track finished courses
        finished = 0
        while q:
            node = q.popleft() #finish a course 
            finished += 1 #increment
            #check nei courses, can we finish them now? 
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0: #if we can finish
                    q.append(nei)

        return True if finished == numCourses else False
