from utility import *

day=18

directionVector=[(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def comprehension(rows):
  triplettes=[]
  for element in rows:
    splitted=element.split(",")
    triplettes.append((int(splitted[0]), int(splitted[1]), int(splitted[2])))
  return triplettes

def solve1():
  rows=getOldAocInput(day)
  triplettes=comprehension(rows)

  distance1=0
  for i in range(len(triplettes)):
    for j in range(i+1,len(triplettes)):
      if (distanceBetweenTwoTriplettes(triplettes[i], triplettes[j])==1):
        distance1=distance1+1

  return len(triplettes)*6-distance1*2

def candidatePositioninBoundaries(candidatePosition, boundaries):
  if(candidatePosition[0]<boundaries[0]):
    return False
  if(candidatePosition[0]>boundaries[1]):
    return False
  if(candidatePosition[1]<boundaries[2]):
    return False
  if(candidatePosition[1]>boundaries[3]):
    return False
  if(candidatePosition[2]<boundaries[4]):
    return False
  if(candidatePosition[2]>boundaries[5]):
    return False
  return True

def breadthFirstSearch(element, border: list, outsidePoints: list, triplettes, boundaries, realAirPockets, notAirPockets):
  marked=border.copy()
  breadth=0
  while(len(border)>0):
    for idx in reversed(range(len(border))):
      for direction in directionVector:
        candidatePosition=sumTriplettesValueByValue(border[idx], direction)
        if(candidatePosition in outsidePoints or candidatePosition in notAirPockets):
          return True
        if(candidatePosition in realAirPockets):
          return False
        if(candidatePosition not in triplettes and candidatePosition not in marked and candidatePositioninBoundaries(candidatePosition, boundaries)):
          marked.append(candidatePosition)
          border.append(candidatePosition)
      border.pop(idx)
    breadth=breadth+1
  return False

def buildBoundaries(triplettes):
  borders=[]
  borders.append(min(a[0] for a in triplettes))
  borders.append(max(a[0] for a in triplettes))
  borders.append(min(a[1] for a in triplettes))
  borders.append(max(a[1] for a in triplettes))
  borders.append(min(a[2] for a in triplettes))
  borders.append(max(a[2] for a in triplettes))
  boundaries=[]
  for i in range(6):
    if(i%2==0):
      boundaries.append(borders[i]-1)
    else:
      boundaries.append(borders[i]+1)

  return borders, boundaries

def buildOutsidePoints(boundaries):
  outsidePoints=[]
  for x in range(2):
    for y in range(2,4):
      for z in range(4,6):
        outsidePoints.append((boundaries[x],boundaries[y],boundaries[z]))
  return outsidePoints

def buildCandidateAirPockets(border: list, triplettes: list):
  candidatesAirPockets=[]
  for x in range(border[0]+1, border[1]):
    for y in range(border[2]+1, border[3]):
      for z in range(border[4]+1, border[5]):
        if((x,y,z)not in triplettes):
          candidatesAirPockets.append((x,y,z))
  return candidatesAirPockets

def solve2():
  rows=getOldAocInput(day)
  triplettes=comprehension(rows)
  # Analyzing input i saw there is no negative point, and 0,0,0 is not part of the figure
  # The idea is to find a path toward (0,0,0) if there is one cube is in the exterior part

  borders,boundaries=buildBoundaries(triplettes)

  outsidePoints=buildOutsidePoints(boundaries)

  candidateAirPockets=buildCandidateAirPockets(borders, triplettes)

  # print(candidateAirPockets)

  relAirPockets=[]
  notAirPockets=[]
  for element in candidateAirPockets:
    if(not breadthFirstSearch(element, [(element)], outsidePoints, triplettes, boundaries, relAirPockets, notAirPockets)):
      relAirPockets.append(element)
    else:
      notAirPockets.append(element)

  # print("aaa", len(relAirPockets)+len(notAirPockets)==len(candidateAirPockets))
  sidesCompromised=0
  # print(relAirPockets)
  # print("ln")
  # print(len(relAirPockets))
  # print(len(notAirPockets))
  for airPocket in relAirPockets:
    for triplette in triplettes:
      if(distanceBetweenTwoTriplettes(airPocket, triplette)==1):
        sidesCompromised=sidesCompromised+1
  # print(sidesCompromised)


  return solve1()-sidesCompromised


print(solve1())
print(solve2())
