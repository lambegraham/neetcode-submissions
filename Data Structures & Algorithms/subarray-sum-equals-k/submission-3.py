class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0

        prefixSum = defaultdict(int) #counter {0: 1}
        prefixSum[0] = 1 #seen 0 once

        for n in nums:
            currSum += n #add it to running total
            diff = currSum - k #take diff of currSum - k

            res += prefixSum[diff] #diff = 0, add {0: 1} so 1 to the result
            prefixSum[currSum] += 1 #record we have seen currSum 1 more time
        return res
