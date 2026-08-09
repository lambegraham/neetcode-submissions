class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        charCount = Counter(tasks) #char: freq
        maxHeap = [-count for count in charCount.values()] #
        heapq.heapify(maxHeap)

        q = deque() #FIFO #(remaining_freq, next_available_time)
        time = 0 
        while maxHeap or q:
            time += 1 #cycles of CPU
            if maxHeap:
                count = heapq.heappop(maxHeap) #(-freq)
                count += 1 #remove 1 frequency
                if count:
                    q.append((count, time + n)) #put back in Q with cooldown

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time