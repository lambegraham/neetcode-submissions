class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        curr = 0
        minLength = float('inf')

        for r, num in enumerate(nums):
            curr += nums[r]
            while curr >= target:
                minLength = min(minLength, (r-l+1))
                curr -= nums[l]
                l += 1
        return minLength if minLength != float('inf') else 0