class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Quick Select

        target = len(nums) - k #convert to index 

        def quickSelect(left, right):
            pivot = nums[right] #final element is pivot
            pivotIndex = left

            #move all vals <= pivot to left of pivot
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[pivotIndex], nums[i] = nums[i], nums[pivotIndex]
                    pivotIndex += 1
            #move pivot to between sections
            nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]

            if pivotIndex > target: 
                return quickSelect(left, pivotIndex-1)
            elif pivotIndex < target:
                return quickSelect(pivotIndex+1, right)
            else:
                return nums[pivotIndex]

        return quickSelect(0, len(nums)-1)