class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        curr = 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                curr -= arr[l]
                l+=1
            curr += arr[r]
            if r - l + 1 == k:
                avg = curr / k
                if avg >= threshold:
                    res += 1
        return res
