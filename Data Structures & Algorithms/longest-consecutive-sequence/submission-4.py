class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length) in numSet: # KEY LINE
                    length +=1
                result = max(length, result)
        return result
                