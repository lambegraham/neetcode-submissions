"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        startIndex = 0
        endIndex = 0
        res = 0
        currentMeetings = 0

        while startIndex < len(intervals): #loop through all intervals
            if starts[startIndex] < ends[endIndex]:
                #we need a new room since a new start
                startIndex += 1
                currentMeetings += 1
            else: 
                #meeting ended
                endIndex +=1
                currentMeetings -= 1
            res = max(res, currentMeetings)
            #for every loop check max rooms
        return res
        #Time: O(nlogn)
        #Space: O(n)
