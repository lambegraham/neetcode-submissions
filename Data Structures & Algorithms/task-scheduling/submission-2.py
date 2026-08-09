class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #count = (char: freq)
        maxHeap = []
        for char, freq in count.items():
            maxHeap.append(-freq) #store our most freq chars at maxHeap[0]
        heapq.heapify(maxHeap) #MAX heap

        q = deque() #FIFO = CPU
        time = 0

        while q or maxHeap: #need to check if cpu is finished processing
            time += 1 #1 CPU cycle

            if maxHeap:
                #-count NEGATIVE! -4 + 1 = 3 
                count = heapq.heappop(maxHeap) + 1 #process task once
                if count: #if we have remaining cycles of this task
                    q.append((count, time + n)) #n = cooldown time
            
            #check cooldowns
            if q and q[0][1] == time: #time has passed, run task
                heapq.heappush(maxHeap, q.popleft()[0]) #q((2,5)) = 2, _
        return time