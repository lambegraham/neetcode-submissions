class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         res[i] *= nums[j]
        # return res

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res