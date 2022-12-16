from utilities import *
from copy import deepcopy

def buildNodeInNodeDict(node, realNodes, rawNodes):
  steps=0
  border=set([rawNodes[node]["name"]])
  marked=[rawNodes[node]["name"]]
  realNeighbours=[]
  while(len(border)>0 and steps<30):
    steps=steps+1
    newBorderSet=set()
    for borderNode in border:
      for neighbour in rawNodes[borderNode]["neighbours"]:
        if (neighbour in marked):
          continue
        if (neighbour in realNodes):
          realNeighbours.append(dict(name=neighbour, distance=steps+1))
        marked.append(neighbour)
        newBorderSet.add(neighbour)
      
    border=newBorderSet
  return dict(name=node, flowRate=rawNodes[node]["flowRate"], neighbours=realNeighbours)

def comprehensionRows(rows):
  realNodes=[]
  rawNodeDict=dict()
  for row in rows:
    splitted=row.replace("="," ").replace(",", "").replace(";", "").split(" ")
    for idx, element in enumerate(splitted):
      if(idx==1):
        rawNodeDict[element]=dict(name=element, neighbours=[])
        current=rawNodeDict[element]
      if(idx==5):
        intElement=int(element)
        current["flowRate"]=intElement
        if(intElement>0):
          realNodes.append(current["name"])
      if(idx>9):
        current["neighbours"].append(element)
  if('AA' not in realNodes):
    realNodes.append('AA')

  nodeDict=dict()
  for node in realNodes:
    nodeDict[node]=buildNodeInNodeDict(node, realNodes, rawNodeDict)
  return nodeDict

def buildPath(node, path:dict, marked: list, maxMinutes, nodeDict, allPossiblePaths):
  marked.append(node["name"])
  path["steps"]=path["steps"]+node["distance"]
  if(path["steps"]>maxMinutes):
    return path["value"]
  path["value"]=path["value"]+nodeDict[node["name"]]["flowRate"]*(maxMinutes-path["steps"])
  result=path["value"]
  allPossiblePaths.append(dict(path=path["nodes"], value=result))

  path["nodes"].append(node["name"])

  for neighbourNode in nodeDict[node["name"]]["neighbours"]:
    
    if(neighbourNode["name"] in marked):
      continue

    result=max(buildPath(neighbourNode, deepcopy(path), marked.copy(), maxMinutes, nodeDict, allPossiblePaths), result)
  
  return result

def solve1():
  rows=getAocInput(day)
  nodeDict=comprehensionRows(rows)
  allPossiblePaths=[]
  return buildPath(dict(name='AA', distance=0), dict(nodes=[], value=0, steps=0), [], 30, nodeDict, allPossiblePaths)

def solve2():
  rows=getAocInput(day)
  nodeDict=comprehensionRows(rows)
  allPossiblePaths=[]
  buildPath(dict(name='AA', distance=0), dict(nodes=[], value=0, steps=0), [], 26, nodeDict, allPossiblePaths)
  # return len(allPossiblePaths)
  result=0
  for i in range(len(allPossiblePaths)):
    for j in range(i+1, len(allPossiblePaths)):
      if(thingInCommonArray(allPossiblePaths[i]["path"][1:], allPossiblePaths[j]["path"][1:])):
        continue
      result=max(result, allPossiblePaths[i]["value"]+allPossiblePaths[j]["value"])
  return result

print(solve1())
print(solve2())