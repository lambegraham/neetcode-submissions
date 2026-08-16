class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # indexes, nums[q] decreasing
        res = []

        for i, num in enumerate(nums):
            #check for smaller values, can never be maximum
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            #remove left index if it is out of window
            if q[0] <= i - k:
                q.popleft()
            #left is always the max of window
            if i >= k - 1:
                res.append(nums[q[0]]) #append on the left since it is max
        return res