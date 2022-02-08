def isNStraightHand(hand, groupSize):
    flag = 0
    if len(hand) % groupSize != 0:
        return False

    else:
        hand.sort()

        for j in range(int(len(hand) / groupSize)):
            tmp = 0
            flag = 0
            for i in range(groupSize-1):
                if( (hand[flag] + 1) in hand):
                    tmp = hand.index(hand[flag]+1)-1
                    hand.pop(hand.index(hand[flag]))
                    flag = tmp
                else:
                    return False
            hand.pop(hand.index(hand[flag]))
        return True


hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(isNStraightHand(hand, groupSize))
