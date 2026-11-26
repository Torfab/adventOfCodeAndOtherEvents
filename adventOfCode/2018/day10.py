from utility import *

# Reinvented a sort of Hartley entropy

def extractRow(row):
  rowSplitted=row.split("<")

  firstsSubString=rowSplitted[1].split(">")[0]
  position=tuple([int(x) for x in firstsSubString.split(", ")])

  
  firstsSubString=rowSplitted[2].split(">")[0]
  velocity=tuple([int(x) for x in firstsSubString.split(", ")])
  #position=<-41165, -10203> velocity=< 4,  1>
  return position, velocity

def parseRows(rows):
  posVel=[]
  for row in rows:
    position, velocity=extractRow(row)
    posVel.append({"position": position, "velocity": velocity})
  return posVel

def boxArea(limits):
  return limits[0]*limits[1]

def limits(posVel):
  minX=float("inf")
  maxX=-minX
  minY=minX
  maxY=-minX
  for element in posVel:
    position=element["position"]
    if(position[0]<minX):
      minX=position[0]
    if(position[0]>maxX):
      maxX=position[0]
    if(position[1]<minY):
      minY=position[1]
    if(position[1]>maxY):
      maxY=position[1]
  return maxX-minX, maxY-minY

def doATurn(posVel):
  for i in range(len(posVel)):
    posVel[i]["position"]=(posVel[i]["position"][0]+posVel[i]["velocity"][0], posVel[i]["position"][1]+posVel[i]["velocity"][1])

def solve():
  rows=getOldAocInput(10)
  posVel=parseRows(rows)
  step=0
  bestArea=float("inf")
  while(True):
    doATurn(posVel)
    step=step+1
    
    area=hartley_Entropy([x["position"] for x in posVel])
    if (area<bestArea):
      bestArea=area
      bestPositions= [x["position"] for x in posVel]
      bestStep=step
      stepSinceBest=0
    if(area>bestArea):
      stepSinceBest=stepSinceBest+1

    if stepSinceBest==10:
      stampaGrid(bestPositions)
      return bestStep
    
    # old manually hardcoded
    # if(limits[1]<10):
    #   myKeys=set([x["position"] for x in posVel])
    #   stampaGrid(myKeys)
    #   return step  

print(solve())
