from utilityz import *

cannonScore={"A":1, "B":2, "C":3}

def solve():
  rows=openFile("raw.txt")
  grid, _, maxY=buildGrid(rows)
  cannons={}
  targets=[]
  bigTargets=[]
  for k,v in grid.items():
    if v in ["A", "B", "C"]:
      cannons[k]=v
    if v=="T":
      targets.append(k)
    if v=="H":
      bigTargets.append(k)

  minX=min([x[0] for x in targets])
  if(len(bigTargets)>0):
    minX=min(minX, min([x[0] for x in bigTargets]))
  cannonX=list(cannons.keys())[0][0]

  rangeToConsider=minX-cannonX

  hittableGrid={}
  for cannon, label, in cannons.items():
    for power in range (rangeToConsider):
      current=cannon
      for _ in range(power):
        current=sumTupleValueByValue(current, (1,-1))
        hittableGrid[current]=(label, power)
      for _ in range(power):
        current=sumTupleValueByValue(current, (1,0))
        hittableGrid[current]=(label, power)
      while current[1]<maxY:
        current=sumTupleValueByValue(current, (1,1))
        hittableGrid[current]=(label, power)
  score=0
  for target in targets:
    score=score+cannonScore[hittableGrid[target][0]]*hittableGrid[target][1]
  for target in bigTargets:
    score=score+(cannonScore[hittableGrid[target][0]]*hittableGrid[target][1])*2

  return score

def parseRows(rows):
  meteors=[]
  for row in rows:
    x,y=row.split(" ")
    meteors.append((int(x),int(y)))
  return meteors

def solve2():
  rows=openFile("raw.txt")
  meteors=parseRows(rows)
  maxY=0
  rangeToConsider=2000
  cannons=[(0,0),(0,1),(0,2)]
  hittableGrid={}
  for i in range(len(cannons)):
    for newTime in range(10):
      print("inizio", newTime)
      for power in range (1,rangeToConsider):
        current=cannons[i]
        time=newTime
        for _ in range(power):
          current=sumTupleValueByValue(current, (1,1))
          time=time+1
          hittableGrid[(current[0],current[1], time)]=min(hittableGrid.get((current[0],current[1], time), 10000),(i+1)*power)
        for _ in range(power):
          current=sumTupleValueByValue(current, (1,0))
          time=time+1
          hittableGrid[(current[0],current[1], time)]=min(hittableGrid.get((current[0],current[1], time), 10000),(i+1)*power)
        while current[1]>=maxY:
          current=sumTupleValueByValue(current, (1,-1))
          time=time+1
          hittableGrid[(current[0],current[1], time)]=min(hittableGrid.get((current[0],current[1], time), 10000),(i+1)*power)
  
  score=0
  print("setup completo")
  for meteor in meteors:
    time=0
    while hittableGrid.get((meteor[0], meteor[1], time))==None:
      time=time+1
      meteor=sumTupleValueByValue(meteor, (-1,-1))
    score=score+hittableGrid[(meteor[0],meteor[1],time)]
    print(hittableGrid[(meteor[0],meteor[1],time)], meteor)


  return score


# print(solve())
print(solve2())