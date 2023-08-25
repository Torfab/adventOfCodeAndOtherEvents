from utility import *


def parseRows(rows):
  firstLine=rows[0]
  polymerDict=dict()
  for element in rows[2:]:
    polymerDict[element[:2]]=[element[0]+element[6], element[6]+element[1]]

  lineDict=dict()
  for i in range(len(firstLine)-1):
    if(lineDict.get(firstLine[i]+firstLine[i+1])==None):
      lineDict[firstLine[i]+firstLine[i+1]]=1
    else:
      lineDict[firstLine[i]+firstLine[i+1]]=lineDict[firstLine[i]+firstLine[i+1]]+1

    
  return lineDict, polymerDict


def solve(iterations):
  rows=getOldAocInput(14)
  # rows=getOldAocInput(-1)

  lineDict, polymerDict=parseRows(rows)
  
  for _ in range(iterations):
    newLineDict=dict()
    for key in lineDict:
      
      for newElement in polymerDict[key]:
        if(newLineDict.get(newElement)==None):
          newLineDict[newElement]=lineDict[key]
        else:
          newLineDict[newElement]=newLineDict[newElement]+lineDict[key]
    lineDict=newLineDict

  solutionDict={rows[0][0]:1}
  for element in lineDict:
    if(solutionDict.get(element[1])==None):
      solutionDict[element[1]]=lineDict[element]
    else:
      solutionDict[element[1]]=solutionDict[element[1]]+lineDict[element]
  return max(solutionDict.values())-min(solutionDict.values())

print(solve(10))
print(solve(40))