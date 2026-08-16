class Solution:
    def reverse(self, x: int) -> int:
        min = -2 ** 31
        max = (2 ** 31) -1

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            last = x % 10
            res = res * 10 + last
            x //= 10
            if res > max or res < min:
                return 0
        return res * sign