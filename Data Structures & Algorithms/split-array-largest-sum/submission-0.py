class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def split(g): #g = guess
            #greedy algorithm
            total = 0
            split = 0

            for num in nums:
                #total += num #[2 4 10] k = 3 - 2 OK 4 NO, split
                if (total + num) > g:
                    split += 1
                    total = num
                else:
                    total += num
            if split > k:
                return False #this will make us increase our guess
            if split < k:
                return True

        l = max(nums) #choose 1
        r = sum(nums) #choose all

        while l<r:
            mid = (l + r) // 2
            if split(mid):
                r = mid 
            else:
                l = mid + 1
        return l