class Solution:
    def climbStairs(self, n: int) -> int:
        #n = number of steps
        #return = unique ways to climb to top 
        #can climb 1 or 2 steps at a time
        #n = 3
        #[0] > [1] > [2] > [3] = 3
        #                > [4] = X
        #          > [3] = 2
        #    > [2] > [3] = 2
        #          > [4] = X
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

#time   = O(N) loop runs once for each step from 3->n
#space  = O(N) dp stores n + 1 values