class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        res = []
        current = intervals[0] #1st interval

        for interval in intervals[1:]: #start from the 2nd
            start, end = 0, 1 #easier to write 0/1

            if interval[start] <= current[end]:
                current[end] = max(interval[end],current[end])
            
            else:
                res.append(current) #append current interval, no overlap
                current = interval
        res.append(current) #append current interval after loop (flush)
        return res