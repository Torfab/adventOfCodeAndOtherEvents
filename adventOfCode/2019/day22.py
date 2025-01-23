from utilityz import *

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
  rows=getAocInput(22)
  if (part=="a"):
    deck=[i for i in range(10007)]

    for element in rows:
      deck=doAShuffle(element, deck)
    return deck.index(2019)
  
print(solve("a"))