class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Suffix max solution
        r = [0] * len(arr)
        rightMax = -1
        for i in range(len(arr)-1,-1,-1):
            r[i] = rightMax
            rightMax = max(rightMax,arr[i])
        return r