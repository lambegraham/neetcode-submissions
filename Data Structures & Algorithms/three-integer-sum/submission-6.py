class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set() #using a set we can skip duplicates since sorted already

        for i, num in enumerate(nums):
            if num > 0:
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                
                curr = num + nums[l] + nums[r]

                if curr < 0: #move l forward, increase sum since sorted smaller is on L
                    l += 1
                elif curr > 0: #move r back, decrease since ^^
                    r -= 1
                else:
                    res.add((num,nums[l],nums[r]))
                    l += 1
                    r -= 1

        return list(res)
