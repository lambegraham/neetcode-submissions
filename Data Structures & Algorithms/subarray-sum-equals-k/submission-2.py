class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1 #have seen 0 

        for num in nums:
            curSum += num #add it to running sum
            diff = curSum - k #check the diff

            res += prefixSums[diff] #how many times have we seen diff? add to result
            prefixSums[curSum] += 1 #update we seen this
        return res