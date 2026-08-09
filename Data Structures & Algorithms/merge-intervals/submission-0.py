class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        result = []
        current = intervals[0]

        for interval in intervals[1:]:
            #overlap
            start, end = 0, 1
            if interval[start] <= current[end]: 
                current[end] = max(current[end], interval[end])
            else:
                result.append(current)
                current = interval
        result.append(current)
        return result