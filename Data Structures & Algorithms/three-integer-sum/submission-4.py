class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort() #THIS IS THE KEY

        for i, a in enumerate(nums):
            #check if first num is pos, if so break
            #all nums after cannot form 3sum since sorted
            if a > 0:
                break
            #2 pointer
            l = i + 1
            r = len(nums) - 1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #more 0
                    r-=1 #make right smaller
                elif threeSum < 0: #less 0
                    l+=1 #make left bigger
                else:
                    res.add((a, nums[l], nums[r])) #append result
                    l+=1 #make l bigger
                    r-=1 #make r smaller 
        return list(res)