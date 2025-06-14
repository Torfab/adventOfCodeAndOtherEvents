from utility import *

def parseRows(rows):
  collectionOfTermites={}
  for row in rows:
    source, becoming= row.split(":")
    becoming= becoming.split(",")
    collectionOfTermites[source]=becoming
  return collectionOfTermites

def updateTermites(currentState, collectionOfTermites):
  newCurrentState={x:0 for x in collectionOfTermites.keys()}

  for sourceTermite, numberTermites in currentState.items():
    for newborn in collectionOfTermites[sourceTermite]:
      newCurrentState[newborn]=newCurrentState[newborn]+numberTermites
  return newCurrentState


def solve(times, startingElement):
  rows=openFile("raw.txt")
  collectionOfTermites=parseRows(rows)
  current={startingElement:1}
  for _ in range(times):
    current=updateTermites(current, collectionOfTermites)
  return sum(current.values())


def solve2():
  rows=openFile("raw.txt")
  collectionOfTermites=parseRows(rows)
  results={}
  for element in collectionOfTermites.keys():

    current={element:1}
    for _ in range(20):
      current=updateTermites(current, collectionOfTermites)
    results[element]=sum(current.values())
  return max(results.values())-min(results.values())


# print(solve(4, "A"))
# print(solve(10, "Z"))
print(solve2())