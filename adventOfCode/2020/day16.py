from utility import *

def parseRows(rows):
  state=0
  ticketDict={}
  nearbyTickets=[]
  for row in rows:
    if(state==0):
      if(row==""):
        state=1
        continue
      rowSplitted=row.split(": ")
      key=rowSplitted[0]
      rowSplitted=rowSplitted[1].split()
      value=[]
      value.append(tuple([int(x) for x in rowSplitted[0].split("-")]))
      value.append(tuple([int(x) for x in rowSplitted[2].split("-")]))
      ticketDict[key]=value

    if(state==1):
      if(row==""):
        state=2
        continue
      if(row[0].isdigit()):
        myTicket=[int(x) for x in row.split(",")]
      if(row==""):
        state=2
    if(state==2 and row[0].isdigit()):
      nearbyTickets.append([int(x) for x in row.split(",")])
  return ticketDict, myTicket, nearbyTickets

def risA(nearbyTickets, valid):
  ris=0

  for ticket in nearbyTickets:
    for element in ticket:
      if element not in valid:
        ris=ris+element
  return ris

def isValid(ticket, valid):
  for element in ticket:
    if element not in valid:
      return element
  return 0

def dumpInvalid(nearbyTickets, valid):
  validTickets=[]
  for ticket in nearbyTickets:
    if(isValid(ticket, valid)==0):
      validTickets.append(ticket)
  return validTickets

def makeSetFieldValid(ranges):
  mySet=set()
  for i in range(ranges[0][0], ranges[0][1]+1):
    mySet.add(i)
  for i in range(ranges[1][0], ranges[1][1]+1):
    mySet.add(i)
  return mySet

def solve(part):
  rows=getOldAocInput(6)
  ticketDict, myTicket, nearbyTickets=parseRows(rows)
  ranges=[]
  for value in ticketDict.values():
    ranges=ranges+value
  ranges=mergeRanges(ranges)
  valid=set()
  for singleRange in ranges:
    for i in range(singleRange[0], singleRange[1]+1):
      valid.add(i)

  if part=="a":
    return risA(nearbyTickets, valid)
  
  nearbyTickets=dumpInvalid(nearbyTickets, valid)
  ticketDictToDestroy={k:makeSetFieldValid(v) for k,v in ticketDict.items()}

  found={}
  notFound=list(range(len(nearbyTickets[0])))

  separatedFieldsTickets=[]
  for _ in notFound:
    separatedFieldsTickets.append([])
  for ticket in nearbyTickets:
    for i in range(len(ticket)):
      separatedFieldsTickets[i].append(ticket[i])

  elementIdx=0
  departureFieldsIdx=[]
  while(len(departureFieldsIdx)!=6):
    elementIdx=(elementIdx+1)%len(notFound)
    column=notFound[elementIdx]
    notValid=set()
    for fieldValue in separatedFieldsTickets[column]:
      for k,fieldRange in ticketDictToDestroy.items():
        if fieldValue not in fieldRange:
          notValid.add(k)
    if(len(ticketDictToDestroy)-len(notValid)==1):
      columnName=set(ticketDictToDestroy.keys()).difference(notValid).pop()
      ticketDictToDestroy.pop(columnName)
      found[column]=columnName
      notFound.pop(elementIdx)
      departureFieldsIdx=[k for k, v in found.items() if "departure" in v]

  ris=1
  for idx in departureFieldsIdx:
    ris=ris*myTicket[idx]
  return ris



print(solve("a"))
print(solve("b"))


