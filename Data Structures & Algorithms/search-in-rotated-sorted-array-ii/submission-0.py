class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2 #middle point
            if nums[mid] == target:
                return True
            #LEFT SIDE
            if nums[left] < nums[mid]: #left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 #search left
                else:
                    left = mid + 1 #search right
            #RIGHT SIDE
            elif nums[left] > nums[mid]: #right half is sorted
                if nums[mid] <= target < nums[right]:
                    left = mid + 1 #search right
                else:
                    right = mid -1 #search left
            #SKIP DUPLICATES
            elif nums[left] == nums[mid]: #duplicate found
                left += 1 #skip duplicate
        return False