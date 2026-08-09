class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        ones = 0
        for num in nums:
            
            if num == 1:
                ones+=1
            if num != 1:
                ones = 0
            result = max(result,ones)
        return result