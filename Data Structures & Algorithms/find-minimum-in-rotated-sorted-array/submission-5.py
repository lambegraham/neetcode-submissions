class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        result = nums[0]

        while l<=r:
            if nums[l] < nums[r]: #already sorted
                result = min(result, nums[l])
                break

            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] <= nums[r]: #search left half
                r = mid - 1
            else:
                l = mid + 1
        return result
