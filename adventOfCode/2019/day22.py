from utilityz import *

# Shuffling a deck of cards with the shuffles of the problem is a linear operation
# So use a lot of shuffles are comprimable in a single particular shuffle
# I can know in O(1) where a card goes or what card is in particular position
# for more detailed guide check https://mislavzanic.com/blog/advent-of-code-2019-22 (up at 2025/01/24)


def linearFullShuffle(rows, deckSize):
  a=1
  b=0
  for row in rows:
    rowSplitted=row.split(" ")
    if row=="deal into new stack":
      a=a*-1
      b=deckSize-1-b
    elif rowSplitted[0]=="cut":
      num=int(rowSplitted[1])
      b=b-num
    elif rowSplitted[0]=="deal":
      num=int(rowSplitted[3])
      a=a*num
      b=b*num
  return a%deckSize, b%deckSize


def doAShuffle(element, deck):
  if element=="deal into new stack":
    return list(reversed(deck))
  
  elementSplitted=element.split(" ")
  if elementSplitted[0]=="cut":
    num=int(elementSplitted[1])
    return deck[num:]+deck[:num]
  if elementSplitted[0]=="deal":
    num=int(elementSplitted[3])
    idxArray=0
    idxNewArray=0
    lenDeck=len(deck)
    newDeck=list(deck)  
    while(idxArray<lenDeck):
      newDeck[idxNewArray]=deck[idxArray]
      idxArray=idxArray+1
      idxNewArray=(idxNewArray+num)%lenDeck
    return newDeck


def solve(part):
  rows=getOldAocInput(22)
  if (part=="a"):
    deck=[i for i in range(10007)]

    for element in rows:
      deck=doAShuffle(element, deck)
    return deck.index(2019)
  if part=="b":
    deckSize=119315717514047
    a, b=linearFullShuffle(rows, deckSize)
    a,b= pow(a, -1, deckSize), -1*pow(a, -1, deckSize)*b%deckSize
    pow1=pow(a, 101741582076661, deckSize)
    pow2=b*((pow1-1)*pow(a-1, 119315717514047-2, deckSize))%deckSize
    return (pow1*2020+pow2)%deckSize

print(solve("a"))
print(solve("b"))