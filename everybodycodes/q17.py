from utilityz import *
import heapq

# Legacy, lo lascio per ricordo come lìho implementato a mano prima di scoprire l'esistenza di prim's
# def evaluateSizeConstellation(subConstellation):

#   elementToCheck=subConstellation.copy()
#   constellation=[elementToCheck.pop()]
#   totalDistance=0
  
#   while(len(elementToCheck)>0):
#     minDistance=float("inf")
#     for sourceStar in constellation:
#       for receiveStar in elementToCheck:
#         distance=distanceBetweenTwoTuples(sourceStar, receiveStar)
#         if(distance<minDistance):
#           minDistance=distance
#           foundStarIndex=elementToCheck.index(receiveStar)
#     constellation.append(elementToCheck.pop(foundStarIndex))
#     totalDistance=totalDistance+minDistance

#   return totalDistance+len(constellation)

def primsThingy(subConstellation):
  primsConstellationRapresentation={}
  for element in subConstellation:
    primsConstellationRapresentation[element]=[]
    for otherElement in subConstellation:
      if element==otherElement:
        continue
      else:
        primsConstellationRapresentation[element].append((otherElement, distanceBetweenTwoTuples(element, otherElement)))

  startNode=subConstellation[0]

  border= []
  visited=set()
  
  mst=[]
  totalDistances=0

  for neighbour, distance in primsConstellationRapresentation[startNode]:
    heapq.heappush(border, (distance, startNode, neighbour))

  visited.add(startNode)

  while border:
    distance, source, received=heapq.heappop(border)
    if received in visited:
      continue
    mst.append((source, received, distance))
    totalDistances=totalDistances+distance
    visited.add(received)

    for neighbour, distance in primsConstellationRapresentation[received]:
      if neighbour not in visited:
        heapq.heappush(border,(distance, received, neighbour))
  return totalDistances
  
def findSizeConstellation(subConstellation):
  return len(subConstellation)+ primsThingy(subConstellation)

def solve():
  grid, _, _ = buildGrid(openFile("raw.txt"))
  return findSizeConstellation(list(grid.keys()))

def customSort(subarray):
  return len(subarray)

def solve2():
  grid, _, _= buildGrid(openFile("raw.txt"))
  allStars=list(grid.keys())
  constellations=[]
  while(len(allStars)>0):
    sourceStar=allStars.pop(0)
    newConstellation=[sourceStar]
    i=0
    while(i<len(newConstellation)):
      sourceStar=newConstellation[i]
      destroyerStars=[]
      for receiveStar in allStars:
        if distanceBetweenTwoTuples(sourceStar, receiveStar)<6:
          newConstellation.append(receiveStar)
          destroyerStars.append(allStars.index(receiveStar))
      
      destroyerStars.sort(reverse=True)
      for idx in destroyerStars:
        allStars.pop(idx)
      
      i=i+1
    constellations.append(newConstellation)

  constellationSizes=[findSizeConstellation(x) for x in constellations]
  constellationSizes.sort(reverse=True)
  resultMult=1
  for subConstellation in constellationSizes[:3]:
    resultMult=resultMult*subConstellation
  return resultMult

print(solve2())