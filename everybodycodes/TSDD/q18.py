from utility import *

def parseRows(rows):
  myTree={}

  theInput=[]
  for row in rows:
    rowSplitted=row.split(" ")
    if rowSplitted[0]=="":
      continue
    elif rowSplitted[0]=="Plant":
      state=int(rowSplitted[1])
      thickness=int(rowSplitted[-1][:-1])
      myTree[state]={"thickness": thickness}
    elif rowSplitted[0]=="-":
      if rowSplitted[1]=="free":
        continue
      else:
        plantNum=int(rowSplitted[4])
      myTree[state]["branches"]=myTree[state].get("branches", [])+[(plantNum, int(rowSplitted[-1]))]
    elif rowSplitted[0]=="1" or rowSplitted[0]=="0":
      theInput.append(tuple(int(x) for x in rowSplitted))

  return myTree, state, theInput

def calculateLightEmitted(myTree, state):
  light=myTree[state].get("light", None)
  if light!=None:
    return light
  else:
    light=0
    sumz=0
    for b in myTree[state]["branches"]:
      sumz=sumz+calculateLightEmitted(myTree, b[0])*b[1]
    if sumz>=myTree[state]["thickness"]:
      myTree[state]["light"]=sumz
      light=sumz
    return light


def solve():
  rows=openFile("raw.txt")
  status=(1,1,1,1,1,1,1,1,1)
  myTree, state, _=parseRows(rows)
  for i,v  in enumerate(status):
    myTree[i+1]["light"]=v
  lightEmitted=calculateLightEmitted(myTree, state)

  return lightEmitted

def solve2():
  rows=openFile("raw.txt")
  myTree, state, theInputs=parseRows(rows)
  sumz=0
  for status in theInputs:
    iterationTree={k: v.copy() for k, v in myTree.items()}
    for i,v  in enumerate(status):
      iterationTree[i+1]["light"]=v
    lightEmitted=calculateLightEmitted(iterationTree, state)
    sumz=sumz+lightEmitted

  return sumz

def findBestLight(myTree, state, lenInput):
  status={}
  for k, v in myTree.items():
    if k>lenInput:
      for b in v["branches"]:
        if b[0]<=lenInput:
          if b[1]<0:
            status[b[0]]=0
          else:
            status[b[0]]=1
  status=list(status.values())


  iterationTree={k: v.copy() for k, v in myTree.items()}

  for i,v  in enumerate(status):
    iterationTree[i+1]["light"]=v
  return calculateLightEmitted(iterationTree, state)


def solve3():
  rows=openFile("raw.txt")
  myTree, state, theInputs=parseRows(rows)
  lenInput=len(theInputs[0])
  bestLight=findBestLight(myTree, state, lenInput)
  results=[]
  for status in theInputs:
    iterationTree={k: v.copy() for k, v in myTree.items()}
    for i,v  in enumerate(status):
      iterationTree[i+1]["light"]=v
    lightEmitted=calculateLightEmitted(iterationTree, state)
    results.append(lightEmitted)

  sumz=0
  for element in results:
    if element==0:
      continue
    else:
      sumz=sumz+bestLight-element
  return sumz


print(solve3())
