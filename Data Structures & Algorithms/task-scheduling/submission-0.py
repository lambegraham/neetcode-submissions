class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        charCount = defaultdict(int) # char: freq
        for char in tasks:
            #A B C C D A B 
            charCount[char] += 1 # A : 2
        # count = Counter(tasks)
        maxHeap = [] #(-freq, char)
        for char, freq in charCount.items():
            heapq.heappush(maxHeap, (-freq, char)) #most common at maxHeap[0]
            
        q = deque() #FIFO #(remaining_freq, next_available_time)
        time = 0 
        while maxHeap or q:
            time += 1 #cycles of CPU
            if maxHeap:
                freq, char = heapq.heappop(maxHeap) #(-freq, char)
                freq+=1 #remove 1 frequency
                if freq:
                    q.append((freq, char, time + n)) #put back in Q with cooldown
            if q and q[0][2] == time:
                heapq.heappush(maxHeap, q.popleft()[:2])
        return time