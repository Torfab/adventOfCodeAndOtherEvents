from utility import *

def parseRows(rows):
  rows=[" ".join(x.split()).split(" ") for x in rows]
  newArray=[]
  cursor=0
  for row in rows:    
    newArray.append([])
    for value in row:
      if value.replace('.', '',1).isdigit() or value[0]=="-":
        newArray[cursor].append(float(value))
    cursor=cursor+1
  newArray=[x[-3:] for x in newArray]
  return newArray[1:]

def solve():
  rows=openFile("raw.txt")
  rows=parseRows(rows)

  minDistance=float("inf")
  for i in range(len(rows)):
    for j in range(i+1, len(rows)):
      distance= (((rows[i][0]-rows[j][0])**2)+((rows[i][1]-rows[j][1])**2) +((rows[i][2]-rows[j][2])**2))**0.5
      minDistance=min(minDistance, distance)
  return minDistance
print(solve())