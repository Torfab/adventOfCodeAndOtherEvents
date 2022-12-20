from utilities import *

day=20

def swapElementsInDict(mySequence: list, currentPosition1, currentPosition2):
  auxElement2=mySequence[currentPosition2]
  mySequence[currentPosition2]=mySequence[currentPosition1]
  mySequence[currentPosition1]=auxElement2
  return

def insertElementInList(mySequence: list, currentPosition1, currentPosition2):
  element=mySequence.pop(currentPosition1)
  if(currentPosition1<currentPosition2):
    mySequence.insert(currentPosition2, element)
  else:
    mySequence.insert(currentPosition2, element)
  return

def solve(decriptionKey, times):
  rows=getAocInput(day)
  sequence=[]
  for idx, element in enumerate(rows):
    sequence.append(dict(originalPosition=idx, value=int(element)*decriptionKey))

  idx=0
  # print(0, [a["value"] for a in sequence])
  for time in range(times):
    for step in range(len(sequence)):
      turnElement=next(a for a in sequence if a["originalPosition"]==step)
      idx1=sequence.index(turnElement)
      idx2=(idx1+turnElement["value"])%(len(sequence)-1)
      # print("sono allo step", step+1, "devo inserire", turnElement, "quindi allo stato attuale tra", idx1, idx2)
      insertElementInList(sequence,idx1,idx2)
      # print(step+1, [a["value"] for a in sequence])
  
  idx=sequence.index(next(a for a in sequence if a["value"]==0))
  result=sequence[(idx+1000)%len(sequence)]["value"]+sequence[(idx+2000)%len(sequence)]["value"]+sequence[(idx+3000)%len(sequence)]["value"]

  return result

print(solve(1,1))
print(solve(811589153,10))