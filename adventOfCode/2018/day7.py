from utility import *
from collections import deque
import bisect
def parseRows(rows):
  myGraph={}

  for row in rows:
    rowSplitted=row.split(" ")

    myGraph[rowSplitted[1]]=myGraph.get(rowSplitted[1], {})
    myGraph[rowSplitted[1]]["before"]=myGraph[rowSplitted[1]].get("before", [])+[rowSplitted[7]]

    myGraph[rowSplitted[7]]=myGraph.get(rowSplitted[7], {})
    myGraph[rowSplitted[7]]["after"]=myGraph[rowSplitted[7]].get("after", [])+[rowSplitted[1]]


  return myGraph

def letterToNum(letter):
  return ord(letter)-4

def solve(part):
  rows=getOldAocInput(7)
  myGraph=parseRows(rows)
  lenMyGraph=len(myGraph)

  alreadyFinished=set()
  result=""
  if part==1:
    while(len(result)<lenMyGraph):
      findElements=[k for k,v in myGraph.items() if alreadyFinished.issuperset(v.get("after", [])) and k not in alreadyFinished]
      findElements.sort()
      firstElement=findElements[0]
      alreadyFinished.add(firstElement)
      result=result+firstElement
    return result

  freeWorkers=5
  
  findElements=[k for k,v in myGraph.items() if alreadyFinished.issuperset(v.get("after", []))]
  findElements.sort()
  thingsInQueue=deque([[letterToNum(letter), letter] for letter in findElements])
  alreadyStarted=set(findElements)
  alreadyFinished=set()

  freeWorkers=freeWorkers-len(thingsInQueue)
  currentTime=0


  while(thingsInQueue):
    timeToFinish, letter=thingsInQueue.popleft()
    freeWorkers=freeWorkers+1
    currentTime=currentTime+timeToFinish
    result=result+letter
    alreadyFinished.add(letter)

    for element in thingsInQueue:
      element[0]=element[0]-timeToFinish

    findElements=[k for k,v in myGraph.items() if alreadyFinished.issuperset(v.get("after", [])) and k not in alreadyFinished and k not in alreadyStarted]
    findElements.sort()

    for element in findElements:
      if(freeWorkers>0):
        bisect.insort(thingsInQueue, [letterToNum(element), element])
        alreadyStarted.add(element)
        freeWorkers=freeWorkers-1
      else:
        break

  return currentTime


print(solve(2))