class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the i,j such that nums[i]+nums[j] = target

        diffs = {} #{num: index}

        for i in range(len(nums)):
            diff = target - nums[i] #4
            if diff in diffs: #we found what we needed
                return [diffs[diff], i]
            diffs[nums[i]] = i #4: 0