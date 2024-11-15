from utilityz import *

def homeMadePermutations(elements, subPermutation, totalLength, result):
  if(totalLength==len(subPermutation)):
    result.append(subPermutation)
    return
  
  for element in elements:
    if elements[element]>0:
      elements[element]=elements[element]-1
      homeMadePermutations(elements, subPermutation+element, totalLength, result)
      elements[element]=elements[element]+1

def parseRows(rows):
  vehicles={}
  for row in rows:
    vehicle, actions=row.split(":")
    vehicles[vehicle]={"actions":actions.split(","), "currentAction":0, "currentSpeed":10, "currentSpace":0}
  return vehicles


def strife(action, terrain="="):
  if(terrain=="="):
    if(action=="+"):
      return 1
    if(action=="-"):
      return -1
    if(action=="="):
      return 0
  if terrain=="+":
    return 1
  if terrain=="-":
    return -1
  return 0


def solve(part):
  rows=openFile("raw.txt")
  vehicles=parseRows(rows)
  if part=="b":
    track=parseTrack(openFile("track.txt"))
    iterations=len(track)*10
  else:
    track=["="]
    iterations=10

  for i in range(iterations):
    for vehicle in vehicles.values():
      vehicle["currentSpeed"]=vehicle["currentSpeed"]+strife(vehicle["actions"][vehicle["currentAction"]],track[i%len(track)])
      vehicle["currentSpace"]=vehicle["currentSpace"]+vehicle["currentSpeed"]
      vehicle["currentAction"]=(vehicle["currentAction"]+1)%len(vehicle["actions"])

  vehicleSpaceList=sorted(vehicles.keys(), key=lambda k: vehicles[k]["currentSpace"], reverse=True)
  return "".join(vehicleSpaceList)

def parseTrack(rows):
  grid, _, _ = buildGrid(rows, " ")
  currentPoint=(1,0)
  currentDirection=(1,0)
  track=[]
  while currentPoint!=(0,0):
    track.append(grid[currentPoint])
    tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
    if(grid.get(tentativeCurrentPoint)==None):
      if(currentDirection==(1,0)):
        currentDirection=(0,1)
        tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
        if(grid.get(tentativeCurrentPoint)==None):
          currentDirection=(0,-1)
          tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
      elif(currentDirection==(0,1)):
        currentDirection=(-1,0)
        tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
        if(grid.get(tentativeCurrentPoint)==None):
          currentDirection=(1,0)
          tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
      elif(currentDirection==(-1,0)):
        currentDirection=(0,-1)
        tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
        if(grid.get(tentativeCurrentPoint)==None):
          currentDirection=(0,1)
          tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
      elif(currentDirection==(0, -1)):
        currentDirection=(1,0)
        tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
        if(grid.get(tentativeCurrentPoint)==None):
          currentDirection=(-1,0)
          tentativeCurrentPoint=sumTupleValueByValue(currentPoint,currentDirection)
    currentPoint=tentativeCurrentPoint
  track.append("=")
  
  return track

def solve2():
  rows=openFile("raw.txt")
  vehicles=parseRows(rows)
  track=parseTrack(openFile("track.txt"))

  for i in range(len(track)*10):
    for vehicle in vehicles.values():
      vehicle["currentSpeed"]=vehicle["currentSpeed"]+strife(vehicle["actions"][vehicle["currentAction"]], track[i%len(track)])
      vehicle["currentSpace"]=vehicle["currentSpace"]+vehicle["currentSpeed"]
      vehicle["currentAction"]=(vehicle["currentAction"]+1)%len(vehicle["actions"])

  vehicleSpaceList=sorted(vehicles.keys(), key=lambda k: vehicles[k]["currentSpace"], reverse=True)
  return "".join(vehicleSpaceList)
  
def solve3():
  rows=openFile("raw.txt")
  vehicles=parseRows(rows)
  track=parseTrack(openFile("track.txt"))

  #the subcycle is 11
  for i in range(len(track)*11):
    vehicle=vehicles["A"]
    vehicle["currentSpeed"]=vehicle["currentSpeed"]+strife(vehicle["actions"][vehicle["currentAction"]], track[i%len(track)])
    vehicle["currentSpace"]=vehicle["currentSpace"]+vehicle["currentSpeed"]
    vehicle["currentAction"]=(vehicle["currentAction"]+1)%len(vehicle["actions"])

  toBeat=vehicle["currentSpace"]
  elements={"+":5, "-":3, "=":3}

  permutations=[]
  homeMadePermutations(elements, "", 11, permutations)

  count=0
  for plan in permutations:
    speed=10
    space=0
    actions=list(plan)
    idxAction=0
    lenActions=len(actions)
    for i in range(len(track)*11):
      speed=speed+strife(actions[idxAction], track[i%len(track)])
      space=space+speed
      idxAction=(idxAction+1)%lenActions
    if space>toBeat:
      count=count+1
  return count


print(solve("a"))
print(solve("b"))
# print(solve3())


