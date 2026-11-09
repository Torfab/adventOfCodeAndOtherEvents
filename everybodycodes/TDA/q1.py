from utility import *

def parseRows(rows):
  newRows=[]
  for row in rows:
    newRows.append([int(x) for x in row.split(",")])
  return  newRows

def calculateJump1(row):
  visited=set()
  cursor=0
  for element in row:
    diff=cursor-element
    if diff<=0 or diff in visited:
      cursor=cursor+element
    else:
      cursor=diff
    visited.add(cursor)
  return cursor

def calculateJump2(row):
  visited=set()
  cursor=0
  for element in row:
    diff=cursor-element
    if diff<=0 or diff in visited:
      cursor=cursor+element
      while(cursor in visited):
        cursor=cursor+1
    else:
      cursor=diff
    visited.add(cursor)
  return cursor

def isItValid(ranges, start, end):
  # print("sto valutando la correttezza di", start, end)
  for element in ranges:
    if(start>=element[1]):
      continue
    if(end<=element[0]):
      continue
    if start>=element[0] and end<=element[1]:
      continue
    if start<=element[0] and end>=element[1]:
      continue
    if start>element[0] and end>element[1]:
      # print("rottura destra", start, end, element)
      return False
    if start<element[0] and end<element[1]:
      # print("rottura sinistra", start, end, element)
      return False
  return True

def calculateJump3(row):
  visited=set()
  cursor=0
  sectionOccupiedUnder=[]
  sectionOccupiedOver=[]
  sections=[sectionOccupiedUnder,sectionOccupiedOver]
  index=0
  maxPointReached=0
  for en, element in enumerate(row):
    fastBreak=False
    diff=cursor-element
    start=cursor
    if diff<=0 or diff in visited or not isItValid(sections[index], diff, cursor):
      # print(diff<=0, diff in visited, not isItValid(sections[index], diff, cursor))
      cursor=cursor+element
      while(cursor in visited or not isItValid(sections[index], start, cursor)):
        cursor=cursor+1
        if cursor>maxPointReached+1:
          fastBreak=True
          break
      if (fastBreak):
        cursor=start
        continue
      sections[index].append((start, cursor))
      maxPointReached=max(maxPointReached, cursor)
    else:
      sections[index].append((diff, cursor))
      cursor=diff
    visited.add(cursor)
    index=(index+1)%2
  #   print("allo step", en, "ho trovato", cursor)
  # print()
  # print("valore trovato:", cursor)
  # print()
  return cursor

def solve(f):
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  result=0
  for row in rows:
    result=result+f(row)

  return result


print(solve(calculateJump3))