from utility import *

##I'm sad, the part 3 is very very more efficient considering it a dijkstra path through scores


commandBehaviour={"L":(-1,0), "R":(1,0)}

def parseRows(rows):
  elements={}
  for row in rows:
    rowSplitted=row.split(" ")
    colors={}
    colors["R"]=rowSplitted[0].split(":")[1]
    colors["G"]=rowSplitted[1]
    colors["B"]=rowSplitted[2]
    colors["S"]=rowSplitted[3]
    elements[rowSplitted[0].split(":")[0]]=colors
  return elements

def evaluate(num):
  a=""
  for element in num:
    if element.isupper():
      a=a+"1"
    else:
      a=a+"0"
  return fromBinaryToInteger(a)

def solve1():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  result=0
  for mainK, element in rows.items():
    score={}
    maxScore=0
    maxScoreKey="n"
    for k,v in element.items():
      score[k]=evaluate(v)
      if(score[k]>maxScore):
        maxScore=score[k]
        maxScoreKey=k
    if maxScoreKey=="G":
      result=result+int(mainK)
  return result

def solve2():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  allScores={}
  for mainK, element in rows.items():
    temp=evaluate(element["S"])
    allScores[temp]=allScores.get(temp, [])+[(mainK, element)]
  minScore=10000000
  currentMainK=0
  for element in allScores[max(allScores.keys())]:
    score=0
    for v in element[1].values():
      score=score+evaluate(v)
    if score<minScore:
      minScore=score
      currentMainK=element[0]
  return currentMainK

def categorize(element):
  result=""
  score={}
  maxScore=0
  maxScoreKey="n"
  maxScoreQuantity=0
  for k,v in element.items():
    if k=="S":
      continue
    score[k]=evaluate(v)
    if(score[k]==maxScore):
      maxScoreQuantity=maxScoreQuantity+1
    if(score[k]>maxScore):
      maxScoreQuantity=0
      maxScore=score[k]
      maxScoreKey=k
  if maxScoreQuantity>0:
    return "nothing"
  else:
    result=result+maxScoreKey
  shineValue=evaluate(element["S"])
  if(shineValue<=30):
    return result+"matte"
  if(shineValue>=33):
    return result+"shiny"
  return "nothing"

def solve3():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  allCategory={}
  for mainK, element in rows.items():
    temp=categorize(element)
    allCategory[temp]=allCategory.get(temp, [])+[int(mainK)]
  allCategoryGroup={k:len(x) for k,x in allCategory.items()}
  del(allCategoryGroup["nothing"])
  res=max(allCategoryGroup, key=allCategoryGroup.get)
  result = sum(allCategory[res])
  return result


# print(solve1())
print(solve3())