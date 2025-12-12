from utilityz import *
import functools

def parseRows(rows):
  graph={}
  for row in rows:
    rowSplitted=row.split(" ")
    graph[rowSplitted[0][:-1]]=rowSplitted[1:]
  return graph



@functools.cache
def findRoute(element, toPass):
  count=0
  listToPass=list(toPass)
  for idx in range(len(listToPass)):
    if element==listToPass[idx][0]:
      listToPass[idx]=(element, 1)
      toPass=tuple(listToPass)

  for route in graph[element]:
    if route=="out":
      if(not any(mandatory[1]==0 for mandatory in toPass)):
        count=count+1
    else:
      count=count+findRoute(route, toPass)
  return count

#sadly i've to global initialize this or functool cache can't work (not immutable even if i use it only in read)
graph={}

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