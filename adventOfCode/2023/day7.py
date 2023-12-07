from utility import *

valuesA={"A":14, "K":13, "Q":12, "J":11, "T": 10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
valuesB={"A":14, "K":13, "Q":12, "J":1, "T": 10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}


def toScore (element, part):
  score=0
  position=5
  if(part=="a"):
    values=valuesA
  if(part=="b"):
    values=valuesB
  for char in element:
    score=score+values[char]*(100**position)
    position=position-1
  return score

def solve(part):
  rows=getOldAocInput(7)

  fives=[]
  fours=[]
  full=[]
  threes=[]
  doublePairs=[]
  pairs=[]
  high=[]

  for element in rows:
    dictElement={}
    elementSplitted=element.split(" ")
    newElement=elementSplitted[0]
    for char in newElement:
      if(dictElement.get(char)==None):
        dictElement[char]=1
        continue
      dictElement[char]=dictElement[char]+1

    if(part=="b" and dictElement.get("J")!=None):
      if(dictElement["J"]==5):
        dictElement["A"]=0
      js=dictElement.pop("J")
      key=max(dictElement, key=dictElement.get)
      dictElement[key]=dictElement[key]+js

    fours4=[k for k,v in dictElement.items() if v==4]
    threes3=[k for k,v in dictElement.items() if v==3]
    twos2=[k for k,v in dictElement.items() if v==2]

    if(len(dictElement)==1):
      fives.append({"hand":newElement,  "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
      continue
    if(len(dictElement)==2):
      if(len(fours4)>0):
        fours.append({"hand":newElement,  "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
        continue
      if(len(threes3)>0):
        full.append({"hand":newElement,  "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
        continue
    if(len(dictElement)==3):
      if(len(threes3)>0):
        threes.append({"hand":newElement,  "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
        continue
      if(len(twos2)>0):
        doublePairs.append({"hand":newElement, "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
        continue
    if(len(dictElement)==4):
      pairs.append({"hand":newElement,  "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
      continue
    if(len(dictElement)==5):
      high.append({"hand":newElement,  "score": toScore(newElement, part), "bid": int(elementSplitted[1])})
    
  rank=1
  result=0
  fives= sorted(fives, key=lambda x: x["score"])
  fours= sorted(fours, key=lambda x: x["score"])
  full= sorted(full, key=lambda x: x["score"])
  threes= sorted(threes, key=lambda x: x["score"])
  doublePairs= sorted(doublePairs, key=lambda x: x["score"])
  pairs= sorted(pairs, key=lambda x: x["score"])
  high = sorted(high, key=lambda x: x["score"])


  for element in high:
    result=result+element["bid"]*rank
    rank=rank+1
  for element in pairs:
    result=result+element["bid"]*rank
    rank=rank+1
  for element in doublePairs:
    result=result+element["bid"]*rank
    rank=rank+1
  for element in threes:
    result=result+element["bid"]*rank
    rank=rank+1
  for element in full:
    result=result+element["bid"]*rank
    rank=rank+1
  for element in fours:
    result=result+element["bid"]*rank
    rank=rank+1
  for element in fives:
    result=result+element["bid"]*rank
    rank=rank+1
  return result

print(solve("a"))
print(solve("b"))