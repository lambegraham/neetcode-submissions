class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        openCount = 0
        closeCount = 0
        subset = []
        res = []

        def bt(oc, cc): #open count, close count
            #base
            if oc == n and cc == n:
                res.append("".join(subset))
                return 
            
            #fail case - not sure it is needed here

            if oc < n: #not enough opens
                subset.append("(") #choice
                bt(oc+1, cc) #run
                subset.pop() #undo

            if cc < oc: #need more closing
                subset.append(")")
                bt(oc, cc+1)
                subset.pop()

        bt(0,0)
        return res