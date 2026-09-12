class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin = 1
        curMax = 1
        res = nums[0]

        for num in nums:
            tmp = curMax * num
            #set curMax to max of 3 options:
            # 1. num * curMax, 2. num, 3. num * curMin 
            curMax = max(num * curMax, num * curMin, num) #max
            #set curMin to min of same 3, but with TEMP!!
            curMin = min(tmp, num * curMin, num) #min

            res = max(res, curMax)
        return res