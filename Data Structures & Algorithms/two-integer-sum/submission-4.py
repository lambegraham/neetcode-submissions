class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #num: index
        #[3,4,5,6] t=7
        for i in range(len(nums)): #0 | 1
            diff = target - nums[i] #7-3=4 | 7-4=3
            if diff in seen: #if 4 in seen F | if 3 in seen Y 
                return [seen[diff], i]
            seen[nums[i]] = i #seen[3] = 0