from utility import *
import heapq

directions=[(0,-1),(1,0),(0,1), (-1,0)]

goalColumns={"A": 3, "B": 5, "C": 7, "D":9}
goalLetter={3: "A", 5: "B", 7: "C", 9:"D"}
costs={"A":1, "B":10, "C":100, "D":1000}

def parseRows(rows):
  grid={}
  initialState=set()
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      grid[(x, y)]=rows[y][x]
      if(rows[y][x]!=" " and rows[y][x]!="#" and rows[y][x]!="."):
        initialState.add((rows[y][x], (x,y)))
        grid[(x, y)]="."
  return grid, (0,initialState)

def stampaGrid(grid):
  maxX, maxY = maxGrid(grid)
  print()
  for y in range(maxY+1):
    for x in range(maxX+1):
      print(grid.get((x,y), " "), end="")
    print()

def mergeGridAndState(grid, state):
  newGrid=grid.copy()
  for element in state:
    newGrid[element[1]]=element[0]
  return newGrid

def goOut(vState, newGrid, marked):
  value=vState[0]
  state=vState[1]
  arraySets= []
  for element in state:
    key, x, y = element[0], element[1][0], element[1][1]
    if(y==1):
      continue
    if(y==3 and (newGrid[(x,2)]!="." or x==goalColumns[key])):
      continue
    if(y==2 and (key, (x, 3)) in state and x==goalColumns[key]):
      continue

    for newX in reversed(range(1, x)):
      if(newX in goalColumns.values()):
        continue
      if(newGrid[(newX, 1)]!="."):
        break
      newState=state.copy()
      newState.remove(element)
      newState.add((key, (newX, 1)))
      newValue=value+costs[key]*(abs(newX-x)+y-1)
      newStateTupled=tuple(newState)
      if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
        continue 
      marked[tuple(newState)]=newValue
      arraySets.append((newValue, newState))
    for newX in range(x+1, 12):
      if(newX in goalColumns.values()):
        continue
      if(newGrid[(newX, 1)]!="."):
        break
      newState=state.copy()
      newState.remove(element)
      newState.add((key, (newX, 1)))
      newValue=value+costs[key]*(abs(newX-x)+y-1)
      newStateTupled=tuple(newState)
      if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
        continue 
      marked[tuple(newState)]=newValue
      arraySets.append((newValue, newState))
  return arraySets

def goOut2(vState, newGrid, marked, bigN):
  value=vState[0]
  state=vState[1]
  arraySets= []
  for element in state:
    key, x, y = element[0], element[1][0], element[1][1]
    if(y==1):
      continue
    if(y==bigN):
      if(x==goalColumns[key]):
        continue
    else:
      isToMove=False
      for newY in range(y, bigN+1):
        if(newGrid[(x,newY)]!=goalLetter[x]):
          isToMove=True
          break      
      if(not isToMove):
        continue
    isToMove=True
    ## Tutti i più piccoli devono essere vuoti
    for newY in range(2, y):
      if(newGrid[(x, newY)]!="."):
        isToMove=False
        break
    if(not isToMove):
      continue

    #Almeno uno più grande deve essere sbagliato

    for newX in reversed(range(1, x)):
      if(newX in goalColumns.values()):
        continue
      if(newGrid[(newX, 1)]!="."):
        break
      newState=state.copy()
      newState.remove(element)
      newState.add((key, (newX, 1)))
      newValue=value+costs[key]*(abs(newX-x)+y-1)
      newStateTupled=tuple(newState)
      if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
        continue 
      marked[tuple(newState)]=newValue
      arraySets.append((newValue, newState))
    for newX in range(x+1, 12):
      if(newX in goalColumns.values()):
        continue
      if(newGrid[(newX, 1)]!="."):
        break
      newState=state.copy()
      newState.remove(element)
      newState.add((key, (newX, 1)))
      newValue=value+costs[key]*(abs(newX-x)+y-1)
      newStateTupled=tuple(newState)
      if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
        continue 
      marked[tuple(newState)]=newValue
      arraySets.append((newValue, newState))
  return arraySets

def buildEndState(num):
  state=set()
  for element in goalColumns.keys():
    for x in range(2,2+num):
      state.add((element, (goalColumns[element], x)))
  return state

def checkGoIn(vState, newGrid, marked, bigN):
  value=vState[0]
  state=vState[1]

  for element in state:
    key, x, y = element[0], element[1][0], element[1][1]
    if(y!=1):
      continue
    goalX=goalColumns[key]

    for theY in reversed(range(2, bigN+1)):
      if(newGrid[(goalX, theY)]=="."):
        valid=True
        for yCompleted in range(theY+1, bigN+1):
          if(newGrid[(goalX, yCompleted)]!=key):
            valid=False
            break
        if(not valid):
          continue
        for newX in range(min(x, goalColumns[key])+1, max(x, goalColumns[key])):
          if(newGrid[(newX, 1)]!="."):
            valid=False
            break
        if(not valid):
          continue

        newState=state.copy()
        newState.remove(element)
        newState.add((key, (goalX, theY)))
        newValue=value+costs[key]*(abs(goalX-x)+theY-1)
        newStateTupled=tuple(newState)
        if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
          continue 
        marked[tuple(newState)]=newValue
        return (newValue, newState)
  return None 

def compute(grid, initialState, endState, bigN):

  marked=dict()
  marked[tuple(initialState[1])]=initialState[0]
  border=[]
  heapq.heappush(border, initialState)
  idx=0
  while(len(border)>0):
    currentState=heapq.heappop(border)

    idx=idx+1
    if(currentState[1]==endState):
      return currentState[0]
    
    if(marked.get(tuple(currentState[1]))<currentState[0]):
      continue

    newGrid=mergeGridAndState(grid, currentState[1])

    # if(idx%200000==0):
    #   print(idx, currentState[0])
    #   stampaGrid(newGrid)

    couldIn=checkGoIn(currentState, newGrid, marked, bigN)
    
    if(couldIn!=None):
      heapq.heappush(border, couldIn)
      continue

    arraySets=goOut2(currentState, newGrid, marked, bigN)
    for element in arraySets:
      heapq.heappush(border, element)

def solve(part):
  rows=getOldAocInput(23)
  grid, initialState=parseRows(rows)

  if(part=="a"):
    endState=buildEndState(2)
    return compute(grid, initialState, endState, 3)
  

  if(part=="b"):
    toChange=[]  
    newInitialState=initialState[1]
    for element in newInitialState:
      if(element[1][1]==3):
        toChange.append(element)
    for element in toChange:
      newInitialState.remove(element)
      newInitialState.add((element[0][0], (element[1][0], 5)))
    newInitialState.add(("D", (3,3)))
    newInitialState.add(("D", (3,4)))
    newInitialState.add(("C", (5,3)))
    newInitialState.add(("B", (5,4)))
    newInitialState.add(("B", (7,3)))
    newInitialState.add(("A", (7,4)))
    newInitialState.add(("A", (9,3)))
    newInitialState.add(("C", (9,4)))
    
    initialState=(0, newInitialState)
    endState=buildEndState(4)
    for y in range(4,6):
      for x in goalColumns.values():
        grid[(x, y)]="."

    return compute(grid, initialState, endState, 5)

print(solve("a"))
print(solve("b"))