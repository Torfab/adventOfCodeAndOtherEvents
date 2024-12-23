from utility import *

def parseRows(rows):
  graph={}

  for row in rows:
    rowSplitted=row.split("-")
    if graph.get(rowSplitted[0])==None:
      graph[rowSplitted[0]]=set()
    graph[rowSplitted[0]].add(rowSplitted[1])
    if graph.get(rowSplitted[1])==None:
      graph[rowSplitted[1]]=set()
    graph[rowSplitted[1]].add(rowSplitted[0])
  return graph

def solve():
  rows=getOldAocInput(23)
  graph=parseRows(rows)

  subkeys=[k for k in graph.keys() if k[0]=="t"]
  found=set()
  ris=0
  for key1 in subkeys:
    subset=graph[key1]
    for key2 in graph[key1]:
      for key3 in graph[key2]:
        if key3 in subset:
          littleList=[key1,key2,key3]
          littleList.sort()
          union=tuple(littleList)
          if(union in found):
            continue
          found.add(union)
          ris=ris+1

  return ris

def solveB():
  rows=getOldAocInput(23)
  graph=parseRows(rows)

  cricca=set()
  tentatives=set(graph.keys())
  excludes=set()

  maxCricca=[[]]

  bronKerbosh(cricca, tentatives, excludes, graph, maxCricca)
  result=list(maxCricca[0])
  result.sort()
  return ",".join(result)

print(solve())
print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))

