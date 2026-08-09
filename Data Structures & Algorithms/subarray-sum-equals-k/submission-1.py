class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1 #have seen 0 

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums[diff]
            prefixSums[curSum] += 1
        return res