class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0]) #sort by start times
        res = []
        current = intervals[0] #start with first interval

        for nextInterval in intervals[1:]:
            start, end = 0, 1 #easier to ref

            if nextInterval[start] <= current[end]: #overlap
                current[end] = max(current[end], nextInterval[end]) #merge them
            else:
                res.append(current) #add interval to result
                current = nextInterval #move to next interval
        res.append(current) #flush last interval
        return res