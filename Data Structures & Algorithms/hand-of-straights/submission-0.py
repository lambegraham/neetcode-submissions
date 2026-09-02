class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]: #if we have num remaining
                for i in range(num, num + groupSize): #from num to group
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True