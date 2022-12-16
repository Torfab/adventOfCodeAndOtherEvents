from utilities import *
from copy import deepcopy

day=-1

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
  
def buildPath(node, path:dict, marked: list, nodeDict):
  marked.append(node["name"])
  path["steps"]=path["steps"]+node["distance"]
  if(path["steps"]>30):
    print("ooops", path)
    return
  path["value"]=path["value"]+nodeDict[node["name"]]["flowRate"]*(30-path["steps"])
  path["nodes"].append(node["name"])

  for neighbourNode in nodeDict[node["name"]]["neighbours"]:
    
    if(neighbourNode["name"] in marked):
      continue

    buildPath(neighbourNode, deepcopy(path), marked.copy(), nodeDict)

  print(path)
  return

def solve():

  rawNodeDict=dict()
  rows=getAocInput(day)
  realNodes=[]
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
  
  for node in nodeDict:
    print(nodeDict[node]["name"], nodeDict[node]["neighbours"])
  print()
  buildPath(dict(name='AA', distance=0), dict(nodes=[], value=0, steps=0), [], nodeDict)

solve()