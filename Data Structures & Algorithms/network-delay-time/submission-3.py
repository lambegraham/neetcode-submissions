class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        #u v t = source target time
        for u,v,t in times:
            adj[u].append((v,t))
            #0: ((1,2))
        
        #init variables?
        totalTime = 0 #result - IF we can reach ALL nodes !!!!!!!
        visited = set() #what have we seen? - prevent duplicate work
        minHeap = [(0, k)] #read = O(1) avg, push/pop O(logN) - tTime, source

        while minHeap:
            w1, n1 = heapq.heappop(minHeap) #weight1, node1
            if n1 in visited: #if node visited, skip
                continue
            visited.add(n1) #visit the node!
            totalTime = w1 #total time! 
            for n2, w2 in adj[n1]: #adj = 0: ((v,t)) 
                if n2 not in visited: #check we didnt visit again
                    heapq.heappush(minHeap, (w1+w2, n2)) #(total_time, source)
        #if we HAVE visited all the nodes, visited == len(n)
        return totalTime if len(visited) == n else -1