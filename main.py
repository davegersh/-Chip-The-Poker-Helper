# Welcome to the 'main' program for 'Chip', this is where you'll find pretty
# much the entire functionality of Chip!
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
hand = "AC 5H AD KH 2S"
def rankHand(hand): #returns [hand rank, card rank] (ex. [5, 13] is a flush with highest card being an Ace)
    #split the hand in a sorted number arr and an unsorted suit arr
    sortedArr = []
    handArr = hand.split(' ')



    for card in handArr:
        sortedArr.append([cardRank[card[0]], card[1]])

    sortedArr.sort()

    #for card in sortedArr:


    #rank the hand
    rank = [0, 0]

    #test for flush and straight flush
    #for i in range(3):
    #    if handArr.Count(handArr[i]) == 5:


    return

def pokerHand(hand):
    return

#hands are organized in group of 5-7 cards each with a number and a suit
#numbers can be from 2-A ranked numerally by 1-13 (1 being 2 and 13 being A)
#suits are not ranked and can be: S (spades), C (clubs), H (hearts), D (diamonds)
#ex. AC 5H AD KH 2S

print(rankHand(hand))
