class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks): #[startTime, processTime]
            t.append(i) #append i onto processTime: [startTime, processTime, originalIndex]
        tasks.sort(key=lambda t: t[0]) #sort by startTime

        #now we have [startTime, processTime, originalIndex] sorted by starttime
        res = []
        minHeap = []
        i = 0
        time = tasks[0][0] #first startTime

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
            #while not exceeding tasks length & next task is available
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2])) #push processTime, originaIndex
                i += 1

                #2 cases now:
                #1: no tasks q'd, skip to next task
            if not minHeap:
                time = tasks[i][0]
                #2: have tasks q'd, process them
            else:
                procTime, index = heapq.heappop(minHeap) #pop off task
                time += procTime #process it
                res.append(index) #append the processing order (index) to result 
        return res
