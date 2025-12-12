from utilityz import *
import functools

def parseRows(rows):
  graph={}
  for row in rows:
    rowSplitted=row.split(" ")
    graph[rowSplitted[0][:-1]]=rowSplitted[1:]
  return graph

graph={}

@functools.cache
def findRoute(element, toPass):
  count=0
  listToPass=list(toPass)
  reTuple=False
  for idx in range(len(listToPass)):
    if element==listToPass[idx][0]:
      reTuple=True
      listToPass[idx]=(element, 1)
  if reTuple:
    toPass=tuple(listToPass)

  for route in graph[element]:
    if route=="out":
      skip=False
      for mandatory in toPass:
        if mandatory[1]==0:
          skip=True
          break
      if(not skip):
        count=count+1
    else:
      count=count+findRoute(route, toPass)
  return count

def solve():
  rows=getOldAocInput(11)
  global graph
  graph=parseRows(rows)
  return findRoute("you", ())

def solve2():
  rows=getOldAocInput(11)
  global graph
  graph=parseRows(rows)
  return findRoute("svr", (("dac", 0), ("fft", 0)))

print(solve())
print(solve2())