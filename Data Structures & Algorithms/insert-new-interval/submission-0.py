class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals = [[1,2],[3,4]..]
        #newInterval = [1,3]

        res = [] #[[X,Y],[...]]

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #end of new is before start of current
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: #start of new is after end of current
                res.append(intervals[i])
            else: #combine intervals since overlapping
                newInterval = [ min(intervals[i][0], newInterval[0]),
                                max(intervals[i][1], newInterval[1])]
        res.append(newInterval) #handles the case of appending new
        return res

