from utility import *

directions=[(1,0), (0,1), (-1,0), (0,-1)]

"""NOT PROUD OF THESE SPAGHETTI, BUT IS WHAT IT IS, I WILL BE BETTER NEXT TIME"""

def solve():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)
  stampaGrid(grid)
  walls=set([x for x,y in grid.items() if y=="#"])
  rightGhosts=[{"coords":x, "direction":0, "collisions":0} for x,y in grid.items() if y==">"]
  downGhosts=[{"coords":x, "direction":1, "collisions":0} for x,y in grid.items() if y=="v"]
  leftGhosts=[{"coords":x, "direction":2, "collisions":0} for x,y in grid.items() if y=="<"]
  upGhosts=[{"coords":x, "direction":3, "collisions":0} for x,y in grid.items() if y=="^"]
  ghosts=rightGhosts+downGhosts+leftGhosts+upGhosts
  collisions=0
  for i in range(10):
    
    coordsUsed={}
    for g, ghost in enumerate(ghosts):
      tentative=sumTupleValueByValue(ghost["coords"], directions[ghost["direction"]])
      if tentative in walls:
        ghost["direction"]=(ghost["direction"]+1)%4
        collisions=collisions+1
      else:
        ghost["coords"]=tentative
      
      coordsUsed[ghost["coords"]]=coordsUsed.get(ghost["coords"],0)+1
    coordsWithCollisions=[(x,y) for x,y in coordsUsed.items() if y>1]
    for coords in coordsWithCollisions:
      for ghost in ghosts:
        if coords[0]==ghost["coords"]:
          ghost["direction"]=(ghost["direction"]+2)%4
      collisions=collisions+coords[1]
  return collisions

def removeGhosts(toRemove, ghosts, steps):
  toRemove.sort()
  for element in reversed(toRemove):
    ghosts.pop(element)

def solve2():
  maxCollisions=10000
  
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)
  walls=set([x for x,y in grid.items() if y=="#"])
  rightGhosts=[{"coords":x, "direction":0, "collisions":0} for x,y in grid.items() if y==">"]
  downGhosts=[{"coords":x, "direction":1, "collisions":0} for x,y in grid.items() if y=="v"]
  leftGhosts=[{"coords":x, "direction":2, "collisions":0} for x,y in grid.items() if y=="<"]
  upGhosts=[{"coords":x, "direction":3, "collisions":0} for x,y in grid.items() if y=="^"]
  ghosts=rightGhosts+downGhosts+leftGhosts+upGhosts
  collisions=0
  step=0
  while(True):

    step=step+1
    toRemove=[]
    coordsUsed={}
    for g, ghost in enumerate(ghosts):
      tentative=sumTupleValueByValue(ghost["coords"], directions[ghost["direction"]])
      if tentative in walls:
        ghost["direction"]=(ghost["direction"]+1)%4
        ghost["collisions"]=ghost["collisions"]+1
        collisions=collisions+1
      else:
        ghost["coords"]=tentative
      if(ghost["collisions"]==maxCollisions):
        toRemove.append(g)
      else:
        coordsUsed[ghost["coords"]]=coordsUsed.get(ghost["coords"],0)+1

    removeGhosts(toRemove, ghosts, step)
    toRemove=[]
    coordsWithCollisions=[(x,y) for x,y in coordsUsed.items() if y>1]
    for coords in coordsWithCollisions:
      for g, ghost in enumerate(ghosts):
        if coords[0]==ghost["coords"]:
          ghost["direction"]=(ghost["direction"]+2)%4
          ghost["collisions"]=ghost["collisions"]+1
          if(ghost["collisions"]==maxCollisions):
            toRemove.append(g)
      collisions=collisions+coords[1]
    removeGhosts(toRemove, ghosts, step)
    if(not ghosts):
      return step
    
def saveStatus(ghosts):
  return tuple([x["coords"][0]+100*x["coords"][1]+10000*x["direction"] for x in ghosts])

def removeAGhost(walls, ghosts, step, maxCollisions=1000000000000):

  useSubCollisions=False

  statuses=[]
  statuses.append(saveStatus(ghosts))

  subCollisions={}

  justFinish=False

  realEnd=False

  statusOfCycle=False

  while(True):
    step=step+1
    toRemove=[]
    coordsUsed={}
    inRoundSubCollisions={}
    for g, ghost in enumerate(ghosts):
      tentative=sumTupleValueByValue(ghost["coords"], directions[ghost["direction"]])
      if tentative in walls:
        ghost["direction"]=(ghost["direction"]+1)%4
        ghost["collisions"]=ghost["collisions"]+1
        inRoundSubCollisions[g]=inRoundSubCollisions.get(g,0)+1
      else:
        ghost["coords"]=tentative
      if(ghost["collisions"]==maxCollisions):
        toRemove.append(g)
        realEnd=True
      else:
        coordsUsed[ghost["coords"]]=coordsUsed.get(ghost["coords"],0)+1

    removeGhosts(toRemove, ghosts, step)
    toRemove=[]
    coordsWithCollisions=[(x,y) for x,y in coordsUsed.items() if y>1]
    for coords in coordsWithCollisions:
      for g, ghost in enumerate(ghosts):
        if coords[0]==ghost["coords"]:
          ghost["direction"]=(ghost["direction"]+2)%4
          ghost["collisions"]=ghost["collisions"]+1
          if(ghost["collisions"]==maxCollisions):
            toRemove.append(g)
            realEnd=True
          inRoundSubCollisions[g]=inRoundSubCollisions.get(g,0)+1

    removeGhosts(toRemove, ghosts, step)

    if(realEnd):
      return ghosts, step
    if(not ghosts):
      return step

    if (not justFinish):
      
      newStatus=saveStatus(ghosts)
      if (newStatus in statuses):
        if statusOfCycle==newStatus:
          cycleSteps=len(statuses)
          howManyCycles=float("inf")
          for g, ghost in enumerate(ghosts):
            cycles=(maxCollisions-ghost["collisions"])//subCollisions.get(g, 1)
            if cycles<howManyCycles:
              howManyCycles=cycles

          toBeSureRealCycle=howManyCycles-1
          step=step+cycleSteps*toBeSureRealCycle
          for g, ghost in enumerate(ghosts):
            ghost["collisions"]=ghost["collisions"]+subCollisions.get(g,0)*(toBeSureRealCycle)
          justFinish=True
        if(useSubCollisions==False):
          useSubCollisions=True
          statuses=[]
          statuses.append(newStatus)
          subCollisions={}
          statusOfCycle=newStatus


          
      else:
        statuses.append(newStatus)
    subCollisions= {x: subCollisions.get(x, 0) + inRoundSubCollisions.get(x, 0) for x in subCollisions.keys() | inRoundSubCollisions.keys() }

def solve3():
  
  
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)
  walls=set([x for x,y in grid.items() if y=="#"])
  rightGhosts=[{"coords":x, "direction":0, "collisions":0} for x,y in grid.items() if y==">"]
  downGhosts=[{"coords":x, "direction":1, "collisions":0} for x,y in grid.items() if y=="v"]
  leftGhosts=[{"coords":x, "direction":2, "collisions":0} for x,y in grid.items() if y=="<"]
  upGhosts=[{"coords":x, "direction":3, "collisions":0} for x,y in grid.items() if y=="^"]
  ghosts=rightGhosts+downGhosts+leftGhosts+upGhosts
  step=0

  while(ghosts):
    ghosts, step=removeAGhost(walls, ghosts, step, 1000000000000)
  return step



# print(solve2())
print(solve3())
