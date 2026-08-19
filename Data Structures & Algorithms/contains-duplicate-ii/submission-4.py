class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashSet = {}

        for i in range(len(nums)):
            if nums[i] in hashSet and abs(hashSet[nums[i]] - i) <= k:
                return True
            hashSet[nums[i]] = i
        return False