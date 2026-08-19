class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) -1
        res = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target: #res left of mid, disc right
                r = mid - 1
            
            elif nums[mid] < target: #res in right, disc left
                l = mid + 1
            
            else:
                return mid
        return res