from utility import *

def buildGraph(rows):
  graph={}
  for element in rows:

    innerList=element[7:].split(" ")
    innerDict={}
    for node in innerList:
      nodeName, nodeValue=node.split(":")
      innerDict[nodeName]=nodeValue
    graph[element[0:3]]=innerDict
  
  return graph

def solve():
  rows=openFile("input.txt")

  graph=buildGraph(rows)

  border=[(-600, "TYC")]
  visited={"TYC": -600}

  while(len(border)>0):
    element=min(border)
    border.remove(element)
    if(element[0]>visited.get(element[1])):
      continue

    for key, node in graph[element[1]].items():
      score=element[0]+600+int(node)
      if(visited.get(key)!=None and visited.get(key)<score):
          continue
      visited[key]=score
      border.append((score, key))
      
  return visited["EAR"]

print(solve())
