class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:                   # if hand list isn't divisible by groupSize:
            return False                                # return false

        count = Counter(hand)                       # create hash for count of each num in hand list
        hand.sort()                                 # sort hand list

        for n in hand:                              # traverse each num in hand list:
            if count[n]:                                # if cur num has val > 0 in count hash:
                for i in range(n, n + groupSize):           # traverse nums from cur to end of possible group:
                    if not count[i]:                            # if cur sub num val <= 0 in count hash:
                        return False                                # return false
                    count[i] -= 1                               # decrem cur sub num in count hash
        return True                                 # return true