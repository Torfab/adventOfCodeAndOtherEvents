from utility import *

setMultipleVisit=set()

def updateGraph(graph, arrayOfElement):
  if(graph.get(arrayOfElement[0])==None):
    graph[arrayOfElement[0]]=[]
  if(graph.get(arrayOfElement[1])==None):
    graph[arrayOfElement[1]]=[]
  graph[arrayOfElement[0]].append(arrayOfElement[1])
  graph[arrayOfElement[1]].append(arrayOfElement[0])
  if(64<ord(arrayOfElement[0][0])<91):
    setMultipleVisit.add(arrayOfElement[0])
  if(64<ord(arrayOfElement[1][0])<91):
    setMultipleVisit.add(arrayOfElement[1])
  
def findPaths(key: str, pathStack: list, end:str, graph:dict, done=[True]):
  result=0
  for  element in graph[key]:
    if(element==end):
      pathStack.append(end)
      result=result+1
      continue
    if(element=='start'):
      continue
    
    elementInPathStack=len([a for a in pathStack if a==element])

    if(done[0]):
      times=1
    else:
      times=2
    if (elementInPathStack>=times and element not in setMultipleVisit):
      continue
    else:
      newDone=done.copy()
      if(elementInPathStack==1 and element not in setMultipleVisit):
        newDone[0]=True
      newStack=pathStack.copy()
      newStack.append(element)
      result=result+findPaths(element, newStack, end, graph, newDone)
  return result
      
def solve(part):
  rows=getAocInput(12,2021)

  graphDict=dict()
  for element in rows:
    updateGraph(graphDict, element.split("-"))

  start='start'
  pathStack=['start']
  done=[part=='a']
  
  result=findPaths(start, pathStack, 'end', graphDict, done)

  return result

print(solve('a'))
print(solve('b'))