class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1 #always max

        while l<=r:
            mid = (l + r) // 2
            if nums[mid] < target: #too small, try right side
                l = mid + 1
            elif nums[mid] > target: 
                r = mid - 1
            else:
                return mid
        return -1