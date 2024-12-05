from utilityz import *

def parseRows(rows):
  start=int(rows[0])
  buses=[int(x) for x in rows[1].split(",") if x.isdigit()]
  return start, buses

def parseRowsB(rows):
  buses=[]
  for bus in rows[1].split(","):
    if(bus=="x"):
      buses.append(-1)
    else:
      buses.append(int(bus))

  return buses

def solve():
  rows=getOldAocInput(13)
  start, buses=parseRows(rows)

  minBus=0
  minRis=float("inf")
  for idx in range(len(buses)):
    ris=buses[idx]-start%buses[idx]
    if ris<minRis:
      minRis=ris
      minBus=buses[idx]
  return minBus*minRis

def solveB():
  rows=getOldAocInput(13)
  buses=parseRowsB(rows)

  theMcm=buses[0]
  start=theMcm
  for i in range(1,len(buses)):

    if(buses[i]==-1):
      continue
    while((start)%buses[i]!=((buses[i]-i)%buses[i])):
      start=start+theMcm
    theMcm=mcm(theMcm,buses[i])

  return start
  
# print(solve())
print(solveB())
