class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #rotated with duplicates
        #[6,7,7,8,9,1,3,4]
        #brute = search each number, find the number, return the number
        #o(n) time, o(1) space
        #more optimal way = binary search
        #binary needs monotonic 1>2>3 
        
        left = 0
        right = len(nums)-1 #search range 0 -> n -1
        
        while left <= right:
            mid = (left + right) // 2 
        #found case
            if nums[mid] == target: 
                return True

        #left side
            elif nums[left] < nums[mid]: #search our left side 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 #search left 
                else:
                    left = mid + 1 #search right
        #right side
            elif nums[left] > nums[mid]: #search right side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        #skip duplicates
            elif nums[left] == nums[mid]:
                left += 1
        return False
