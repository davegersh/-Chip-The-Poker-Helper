# Welcome to the 'main' program for 'Chip', this is where you'll find pretty
# much the main functionality of Chip!
cardRank = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}

handRank = {
    0 : "High Card / Nothing",
    1 : "One Pair",
    2 : "Two Pair",
    3 : "Three of a Kind",
    4 : "Straight",
    5 : "Flush",
    6 : "Full House",
    7 : "Four of a Kind",
    8 : "Straight Flush"
}

hand = "AS AC 7H 7D 6S"
def rankHand(hand): #returns [hand rank, card rank] (ex. [5, 13] is a flush with highest card being an Ace)
    rank = [0, 0]

    #find a flush before sorting (the only time suits matter)
    flushSuit = '' #stores the suit that forms the flush
    for char in "CHDS": #go through the suits
        if hand.count(char) >= 5:
            rank[0] = 5
            flushSuit = char
    print(flushSuit)

    sortedArr = [] #an array of simply the number values (suits don't matter after flush)
    for card in hand.split(' '):
        if flushSuit in card:
            sortedArr.append(cardRank[card[0]])

    sortedArr.sort()
    print(hand)
    print(sortedArr)

    #test for straightflush, then straight
    for i in range(len(sortedArr)-4):
        if sortedArr[i+4] - sortedArr[i] == 4:
            if rank[0] == 5:
                rank[0] = 8 #straightflush
            else:
                rank[0] = 4 #straight
            break;

    #test for four of a kind
    for i in range(len(sortedArr)-2):
        if sortedArr.count(sortedArr[i]) == 4:
            rank[0] = 7 #four of a kind
            break;

    #test for full house (and three of a kind)
    if (len(sortedArr) >= 5 and rank[0] < 7):
        for i in range(len(sortedArr)-2):
            if sortedArr.count(sortedArr[len(sortedArr)-i-1]) == 3:
                threeArray = [x for x in sortedArr if x != sortedArr[len(sortedArr)-i-1]]
                for a in range(len(threeArray)-1):
                    if threeArray.count(threeArray[len(threeArray)-a-1]) == 2:
                        rank[0] = 6 #full house
                        break
                    else:
                        rank[0] = 3 #three of a kind

    #test for one or two pair
    if rank[0] < 3:
        pairCardsCount = 0
        for i in range(len(sortedArr)):
            if sortedArr.count(sortedArr[i]) == 2:
                pairCardsCount += 1

        if pairCardsCount >= 4:
            rank[0] = 2
        elif pairCardsCount == 2:
            rank[0] = 1

    return handRank[rank[0]]

def pokerHand(hand):
    return

#hands are organized in group of 5-7 cards each with a number and a suit
#numbers can be from 2-A ranked numerally by 1-13 (1 being 2 and 13 being A)
#suits are not ranked and can be: S (spades), C (clubs), H (hearts), D (diamonds)
#ex. AC 5H AD KH 2S

print(rankHand(hand) + " succi succi")
