class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #indegree
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        finish = 0 #tracks finished courses

        for course, preq in prerequisites:
            indegree[preq] += 1 #add 1 for every preq
            adj[course].append(preq)

        #queue courses that have no preq's
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0: 
                q.append(n)
        
        #BFS
        while q:
            node = q.popleft() #take the course out
            finish += 1 #mark a course as finished

            #find nei's
            for nei in adj[node]:
                #check if indegree = 0, which means we can start the next
                indegree[nei] -= 1 #remove the dependency
                if indegree[nei] == 0: #course is now available
                    q.append(nei) #schedule it for processing
        return finish == numCourses
