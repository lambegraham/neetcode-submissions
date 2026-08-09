class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val -> index

        for i, n in enumerate(nums): #index, num
            diff = target - n #diff we are looking for
            if diff in prevMap:
                return [prevMap[diff], i] #return num and index
            prevMap[n] = i #set num = index of num