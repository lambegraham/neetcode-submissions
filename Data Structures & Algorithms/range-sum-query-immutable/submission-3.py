class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left <= right:
            preRight = self.prefix[right]
            preL = self.prefix[left - 1] if left > 0 else 0 #0 index!
            return (preRight - preL)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)