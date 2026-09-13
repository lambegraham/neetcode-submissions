"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)

        for i in intervals:
            mp[i.start] += 1 #[1,3] = 1: +1
            mp[i.end] -= 1 #[1,3] = 3: -1

        res = 0
        curr = 0

        for m in sorted(mp.keys()):
            curr += mp[m] #add the value (-1/+1) to curr
            res = max(res, curr)
        return res