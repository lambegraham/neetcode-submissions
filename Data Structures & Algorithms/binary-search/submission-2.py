class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target: #target is in left half, discard right
                r = mid - 1
            elif nums[mid] < target: #target is in right half, discard left
                l = mid + 1
            elif nums[mid] == target:
                return mid
        return -1