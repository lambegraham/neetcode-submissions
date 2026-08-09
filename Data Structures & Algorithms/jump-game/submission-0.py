class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        print(goal)

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal: #can we reach it? 
                goal = i 
        return goal == 0