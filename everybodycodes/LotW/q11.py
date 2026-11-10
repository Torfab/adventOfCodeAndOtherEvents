from utility import *

def parseRows(rows):
  numPortals=int(rows[0].split(" ")[1])
  teleports={}
  for row in rows[2:]:
    portals= [int(x) for x in row.split(" ")]
    portal1, portal2 = portals[0]-1, portals[1]-1
    teleports[portal1]=portal2
    teleports[portal2]=portal1
  return numPortals, teleports
    

def checkAllDistances(i, reachables):
  reached=set()
  reached.add(i)
  border=[i]
  step=-1
  graph={}
  newBorder=True
  while(newBorder):
    newBorder=[]
    step=step+1
    while(border):
      element=border.pop()
      graph[element]=step
      for m in reachables[element]:
        tentative=m
        if tentative not in reached:
          newBorder.append(tentative)
          reached.add(tentative)

    border=newBorder

  return sum(graph.values())
    

def findResultDistances(numPortals, reachables):
  resultTeleportDistance=0
  for i in range(numPortals):
    resultTeleportDistance=resultTeleportDistance+checkAllDistances(i, reachables)
  return resultTeleportDistance


def solve(part):
  rows=openFile("raw.txt")
  numPortals, teleports=parseRows(rows)
  reachables={}
  if(part==1):
    movements=[1,-1]
  else:
    movements=[1,2,3,-1,-2,-3]

  for i in range(numPortals):
    reachables[i]=[]
    for m in movements:
      reachables[i].append((i+m)%numPortals)

  resultSimpleDistances=findResultDistances(numPortals, reachables)

  for t1,t2 in teleports.items():
    reachables[t1].append(t2)
    reachables[t2].append(t1)

  resultTeleportDistance=findResultDistances(numPortals, reachables)

  if part==2:
    minimum=resultTeleportDistance
    alreadyChecked=set()
    for i in range(numPortals):
      for j in range(numPortals):
        if(j*100+i in alreadyChecked):
          continue
        if j not in reachables[i]:
          reachables[i].append(j)
          reachables[j].append(i)
          minimum=min(minimum, findResultDistances(numPortals, reachables) )
          reachables[i].remove(j)
          reachables[j].remove(i)
          alreadyChecked.add(i*100+j)
    resultTeleportDistance=minimum

  if part==3:

    minimum=float("inf")
    used=set()
    for i in range(numPortals):
      if i in used:
        break
      candidates=[]
      for c in range(8):
        value=i+c*numPortals//8
        candidates.append(value)
        used.add(value)
      
      possibiliSequenze=generaSequenze(candidates)
      
      for s in possibiliSequenze:
        for j in range(1,len(s),2):
          element=s[j]
          element2=s[j-1]
          reachables[element].append(element2)
          reachables[element2].append(element)
        tentative=findResultDistances(numPortals, reachables)
        if (tentative<minimum):
          minimum=tentative
        for j in range(1,len(s),2):
          element=s[j]
          element2=s[j-1]
          reachables[element].remove(element2)
          reachables[element2].remove(element)
    resultTeleportDistance=minimum

  return resultSimpleDistances-resultTeleportDistance

def generaSequenze(candidates):
  realCandidates=[]
  if(not candidates):
    return []
  start=candidates[0]
  for i in candidates[1:]:
    couple=[start, i]
    rimanenti=[x for x in candidates if x not in couple]
    coppieGenerate=generaSequenze(rimanenti)
    if(not coppieGenerate):
      realCandidates.append(couple)
    for element in coppieGenerate:
      realCandidates.append(couple+element)
  return realCandidates

# print(solve())
# print(solve(2))
evaluateTime(solve,2)
