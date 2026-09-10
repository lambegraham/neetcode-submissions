class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        for n in range(len(nums)):
            preL = prefix[n-1] if n > 0 else 0
            preR = prefix[-1] - prefix[n]

            if preL == preR:
                return n
        return -1