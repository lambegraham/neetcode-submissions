class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = 1
        right = 1
        res = [1] * len(nums)
        #l -> r
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res