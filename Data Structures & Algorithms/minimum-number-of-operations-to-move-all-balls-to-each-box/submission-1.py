class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        res = [0] * n

        for pos in range(n):
            for i in range(n):
                if boxes[i] == '1':
                    res[pos] += abs(pos - i)
        return res
