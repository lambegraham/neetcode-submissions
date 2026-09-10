class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = [] #using a set we can skip duplicates since sorted already

        for i, num in enumerate(nums):
            if num > 0: #no more ways to make 0
                break 
            if i > 0 and num == nums[i-1]: #num is same as before, skip
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                
                curr = num + nums[l] + nums[r]

                if curr < 0: #move l forward, increase sum since sorted smaller is on L
                    l += 1
                elif curr > 0: #move r back, decrease since ^^
                    r -= 1
                else:
                    res.append((num,nums[l],nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1 #skip duplicates
        return res
