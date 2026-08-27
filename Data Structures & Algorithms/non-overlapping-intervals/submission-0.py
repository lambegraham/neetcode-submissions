class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= prevEnd: #not overlapping
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end) #chooses the smaller
        return res