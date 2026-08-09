class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Suffix max solution
        res = [0] * len(arr)
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return res