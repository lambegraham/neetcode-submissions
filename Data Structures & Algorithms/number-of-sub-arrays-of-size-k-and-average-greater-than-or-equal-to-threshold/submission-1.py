class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        curr = sum(arr[:k - 1]) #start the arr with first k-1 elements summed

        for r in range(k - 1, len(arr)): #skip first k-1 elements
            if r - l + 1 > k:
                curr -= arr[l]
                l+=1
            curr += arr[r]
            avg = curr / k
            if avg >= threshold:
                res += 1
        return res
