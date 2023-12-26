from utility import *
import heapq

directions=[(0,-1),(1,0),(0,1), (-1,0)]

goalColumns={"A": 3, "B": 5, "C": 7, "D":9}
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
    else:
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

def buildEndState():
  state=set()
  for element in goalColumns.keys():
    state.add((element, (goalColumns[element], 2)))
    state.add((element, (goalColumns[element], 3)))
  return state

def checkGoIn(vState, newGrid, marked):
  value=vState[0]
  state=vState[1]

  for element in state:
    key, x, y = element[0], element[1][0], element[1][1]
    if(y!=1):
      continue
    goalX=goalColumns[key]
    if(newGrid[(goalX,3)]=="."):
      valid=True
      for newX in range(min(x, goalColumns[key])+1, max(x, goalColumns[key])-1):
        if(newGrid[(newX, 1)]!="."):
          valid=False
          break
      if(valid):
        newState=state.copy()
        newState.remove(element)
        newState.add((key, (goalX, 3)))
        newValue=value+costs[key]*(abs(goalX-x)+2)
        newStateTupled=tuple(newState)
        if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
          continue 
        marked[tuple(newState)]=newValue
        return (newValue, newState)
    if(newGrid[(goalX, 3)]==key and newGrid[(goalX, 2)]=="."):
      valid=True
      for newX in range(min(x, goalColumns[key])+1, max(x, goalColumns[key])-1):
        if(newGrid[(newX, 1)]!="."):
          valid=False
          break
      if(valid):
        newState=state.copy()
        newState.remove(element)
        newState.add((key, (goalX, 2)))
        newValue=value+costs[key]*(abs(goalX-x)+1)
        newStateTupled=tuple(newState)
        if(marked.get(newStateTupled)!=None and marked[newStateTupled]<newValue):
          continue 
        marked[tuple(newState)]=newValue

        return (newValue, newState)
  return None 

def solve(part):
  rows=getOldAocInput(23)
  grid, initialState=parseRows(rows)
  endState=buildEndState()
  marked=dict()

  marked[tuple(initialState[1])]=initialState[0]
  border=[]
  heapq.heappush(border, initialState)
  idx=0
  while(len(border)>0):
    currentState=heapq.heappop(border)
    if(currentState[1]==endState):
      print(idx+1, currentState[0])
      stampaGrid(mergeGridAndState(grid, currentState[1]))
      return currentState[0]
    
    if(marked.get(tuple(currentState[1]))<currentState[0]):
      continue


    # stampaGrid(mergeGridAndState(grid, currentState[1]))
    newGrid=mergeGridAndState(grid, currentState[1])

    idx=idx+1
    if(idx%10000==0):
      print(idx, currentState[0], currentState[1])
      stampaGrid(newGrid)

    couldIn=checkGoIn(currentState, newGrid, marked)
    if(couldIn!=None):
      heapq.heappush(border, couldIn)
      continue

    arraySets=goOut(currentState, newGrid, marked)
    for element in arraySets:
      heapq.heappush(border, element)

    # print(marked)
    # for state in arraySets:
    #   newGrid=mergeGridAndState(grid, state)
    #   stampaGrid(newGrid)


    # return grid

print(solve("a"))
# print(solve("b"))