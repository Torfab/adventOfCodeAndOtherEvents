from utility import *

def parseRows(rows):
  names=rows[0].split(",")
  movements=rows[2].split(",")

  return names, movements



def solve1():
  rows=openFile("raw.txt")
  names, movements=parseRows(rows)

  currentIndex=0
  minCounter=0
  maxCounter=len(names)-1
  print(names)
  print(movements)
  for movement in movements:
    print(movement)
    steps=int(movement[1:])
    if(movement[0]=="R"):
      currentIndex=min(currentIndex+steps, maxCounter)
    if(movement[0]=="L"):
      currentIndex=max(currentIndex-steps, minCounter)

  return names[currentIndex]

def solve2():
  rows=openFile("raw.txt")
  names, movements=parseRows(rows)
  lenNames=len(names)
  currentIndex=0
  for movement in movements:
    steps=int(movement[1:])
    if(movement[0]=="R"):
      currentIndex=(currentIndex+steps)%lenNames
    if(movement[0]=="L"):
      currentIndex=(currentIndex-steps)%lenNames

  return names[currentIndex]

def solve3():
  rows=openFile("raw.txt")
  names, movements=parseRows(rows)
  lenNames=len(names)
  for movement in movements:
    steps=int(movement[1:])
    if(movement[0]=="R"):
      aux=names[0]
      names[0]=names[steps%lenNames]
      names[steps%lenNames]=aux
    if(movement[0]=="L"):
      aux=names[0]
      names[0]=names[-steps%lenNames]
      names[-steps%lenNames]=aux
      

  return names[0]

# print(solve1())
# print(solve2())
print(solve3())
