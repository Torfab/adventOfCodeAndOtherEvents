from utility import *

def parseRows(rows):
  return rows[0]

def solve():
  rows=openFile("raw.txt")
  ploton=parseRows(rows)

  Anum=0
  Bnum=0
  Cnum=0
  result=0
  for c in ploton:
    if c=="A":
      Anum=Anum+1
    elif c=="a":
      result=result+Anum
    elif c=="B":
      Bnum=Bnum+1
    elif c=="b":
      result=result+Bnum
    elif c=="C":
      Cnum=Cnum+1
    elif c=="c":
      result=result+Cnum

  return result

def calculateOccurrance(ploton, ATents, BTents, CTents, start, end, distance):
  result=0
  cursor=start
  while(cursor<end):
    count=0
    if ploton[cursor]=="a":
      for tent in ATents:
        if abs(cursor-tent)<=distance:
          count=count+1
    if ploton[cursor]=="b":
      for tent in BTents:
        if abs(cursor-tent)<=distance:
          count=count+1
    if ploton[cursor]=="c":
      for tent in CTents:
        if abs(cursor-tent)<=distance:
          count=count+1
    result=result+count
    cursor=cursor+1
  return result

def solve3():
  rows=openFile("raw.txt")
  ploton=parseRows(rows)

  littlePloton=ploton*3
  ATents=[]
  BTents=[]
  CTents=[]
  for i, c in enumerate(littlePloton):
    if c=="A":
      ATents.append(i)
    if c=="B":
      BTents.append(i)
    if c=="C":
      CTents.append(i)
      
  distance=1000
  result=998*calculateOccurrance(littlePloton, ATents, BTents, CTents, len(ploton), 2*len(ploton), distance)
  result=result+calculateOccurrance(littlePloton, ATents, BTents, CTents, 0, len(ploton), distance)
  result=result+calculateOccurrance(littlePloton, ATents, BTents, CTents, 2*len(ploton), 3*len(ploton), distance)
  
  return result

# print(solve())
# print(solve2())
print(solve3())
