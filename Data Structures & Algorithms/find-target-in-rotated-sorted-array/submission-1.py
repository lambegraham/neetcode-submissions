class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: #left is sorted
                #target outside of the left side, search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: #target in range, search left
                    r = mid - 1
            
            else: #right side sorted
                #target is outside of right, search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: #target in range, search right
                    l = mid + 1
        return -1

                