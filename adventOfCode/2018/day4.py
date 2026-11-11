from utility import *


#useless scoring
def toScoreRow(row):
  rowSplitted=row.split(" ")
  dateSplitted=rowSplitted[0][1:].split("-")
  timeSplitted=rowSplitted[1][:-1].split(":")
  year=int(dateSplitted[0])
  month=int(dateSplitted[1])
  day=int(dateSplitted[2])
  hour=int(timeSplitted[0])
  minute=int(timeSplitted[1])

  score=minute+100*hour+10000*day+10000000*month+1000000000*year
  return score

#this was my old explicit sort but those are naturally lexicographically sorted so....
def toSortRowsExplicit(rows):
  newRows=[]
  newRows.append((toScoreRow(rows[0]), rows[0]))
  for row in rows[1:]:
    score=toScoreRow(row)
    for idx, element in enumerate(newRows):
      if score<element[0]:
        newRows.insert(idx, (score, row))
        break
    newRows.insert(idx, (score, row))
  return [x[1] for x in newRows]

def toSortRows(rows):
  rows=sorted(rows)
  return rows

def parseRows(rows):
  rows=toSortRows(rows)
  guards={}
  guard={}
  guardId=-1
  startTime=-1
  endTime=-1
  for row in rows:
    rowSplitted=row.split(" ")
    command=rowSplitted[2]
    if(command=="Guard"):
      guardId=int(rowSplitted[3][1:])
      guard=guards.get(guardId, {"shift": {}, "totalAsleep": 0})
      guards[guardId]=guard
    if command=="wakes":
      endTime=int(rowSplitted[1][:-1].split(":")[1])
      guard["totalAsleep"]=guard["totalAsleep"]+endTime-startTime
      for minute in range(startTime, endTime):
        guard["shift"][minute]=guard["shift"].get(minute,0)+1
      
    if command=="falls":
      startTime=int(rowSplitted[1][:-1].split(":")[1])
      
  return  guards

def solve(part):
  rows=getOldAocInput(4)
  guards=parseRows(rows)



  if part==1:

    maxAsleep=-1
    maxGuardId=-1
    for guardId, guard in guards.items():
      if(guard["totalAsleep"]>maxAsleep):
        maxAsleep=guard["totalAsleep"]
        maxGuardId=guardId
    
    culpritGuard=guards[maxGuardId]

    maxMinute=-1
    maxOccurrance=-1
    for minute, occurrance in culpritGuard["shift"].items():
      if (occurrance>=maxOccurrance):
        maxMinute=minute
        maxOccurrance=occurrance


  if part==2:
    maxMinute=-1
    maxOccurrance=-1
    maxGuardId=-1
    for guardId, guard in guards.items():
      for minute, occurrance in guard["shift"].items():
        if (occurrance>=maxOccurrance):
          maxMinute=minute
          maxOccurrance=occurrance
          maxGuardId=guardId
          print("found", minute, "with occurrance", occurrance, "of guard", guardId)


  return maxGuardId*maxMinute


# print(solve(1))
print(solve(2))