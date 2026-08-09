class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for num in nums:
            hm[num] = 1
        
        for i in range(0, len(nums)+1):
            if not hm[i]:
                return i