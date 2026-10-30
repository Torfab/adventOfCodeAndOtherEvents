from utility import *

def parseRows(rows):
  questList=[]
  
  for row in rows:
    questDict={}
    rowSplitted=row.split()
    for element in rowSplitted:
      elementSplitted=element.split("=")
      questDict[elementSplitted[0]]=int(elementSplitted[1])
    questList.append(questDict)
  return questList


def buildQuestDict(questList):
  questDict={}
  for element in questList:
    if(not questDict.get(element["id"])):
      questDict[element["id"]]=[{"quest":element["quest"], "part":element["part"], "time": element["time"]}]
    else:
      questDict[element["id"]].append({"quest":element["quest"], "part":element["part"], "time": element["time"]})
    
  return questDict

def reduceQuestDict(questDict):
  newQuestDict=[]
  for id, element in questDict.items():
    time=0
    for part in element:
      time=time+part["time"]
    newQuestDict.append((id, time, len(element)))
  return newQuestDict

def solve1():
  rows=openFile("raw.txt")
  questList=parseRows(rows)
  questDict=buildQuestDict(questList)

  reducedQuestDict=reduceQuestDict(questDict)

  reducedQuestDict.sort(key=lambda u: u[1])

  result=0
  for i in range(len(reducedQuestDict)):
    result=result+(i+1)*reducedQuestDict[i][1]

  return result

def solve2():
  rows=openFile("raw.txt")
  questList=parseRows(rows)
  questDict=buildQuestDict(questList)

  reducedQuestDict=reduceQuestDict(questDict)

  reducedQuestDict.sort(key=lambda u: (-u[2], u[1]))

  result=0
  for i in range(len(reducedQuestDict)):
    result=result+(i+1)*reducedQuestDict[i][1]

  return result

def buildSetOfScores(questDict):
  setOfScores=set()
  for id, element in questDict.items():
    for unique in element:
      setOfScores.add((unique["quest"], unique["part"]))
  return setOfScores

def evaluateScore(toScore, questDict, questPoints):
  quest=toScore[0]
  part=toScore[1]
  times={}
  for id, element in questDict.items():
    for unique in element:
      if quest==unique["quest"] and unique["part"]<=part:
        times[id]=[times.get(id,[0, False])[0]+unique["time"], times.get(id,[0,False])[1]]
        if part==unique["part"]:
          times[id][1]=True
  
  times=[(x,y[0]) for x,y in times.items() if y[1]]
  times.sort(key=lambda x:x[1])

  score=50*part
  lastValue=-1
  lastScore=score
  for element in times:
    if(lastValue==element[1]):
      questPoints[element[0]]=questPoints.get(element[0],0)+lastScore
    else:
      if score<=0:
        return
      questPoints[element[0]]=questPoints.get(element[0],0)+score
      lastValue=element[1]
      lastScore=score
    score=score-1


def solve3():
  rows=openFile("raw.txt")
  questList=parseRows(rows)
  questDict=buildQuestDict(questList)
  setOfScores=buildSetOfScores(questDict)

  questPoints={x:0 for x in questDict.keys()}
  
  for toScore in setOfScores:
    evaluateScore(toScore, questDict, questPoints)

  questPoints=[y for x,y in questPoints.items()]
  questPoints.sort(reverse=True)


  result=0

  lastI=-1
  lastValue=-1
  for i in range(len(questPoints)):
    if lastValue==questPoints[i]:
      result=result+(lastI+1)*questPoints[i]
    else:
      result=result+(i+1)*questPoints[i]
      lastI=i
      lastValue=questPoints[i]
  return result
# print(solve2())
print(solve3())
