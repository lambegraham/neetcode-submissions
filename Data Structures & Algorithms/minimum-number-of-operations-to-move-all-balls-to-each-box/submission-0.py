class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ballCount = {}
        for i in range(len(boxes)):
            ballCount[i] = int(boxes[i])

        res = []

        for targetBox in range(len(boxes)):
            moves = 0

            for boxIndex in ballCount:
                if ballCount[boxIndex] == 1:
                    moves += abs(boxIndex - targetBox)
            
            res.append(moves)
        return res