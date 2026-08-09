class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l + r) // 2
            if nums[mid] > target: #mid is too big, discard right
                r = mid - 1
            if nums[mid] < target: #mid is too small, discard left
                l = mid + 1
            if nums[mid] == target:
                return mid
        return -1
                