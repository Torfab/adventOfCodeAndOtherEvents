from utility import *

def parseRows(rows):
  return list(rows[0])

def findNextCursors(letter, cursor, lastCursor, row):
  while(row[lastCursor]!=letter and lastCursor!=cursor):
    lastCursor=lastCursor-1
  while(row[cursor]==letter) and lastCursor!=cursor:
    cursor=cursor+1
  return cursor, lastCursor

def fixLetter(letter, row):
  cursor=row.index(letter)
  step=0
  movedElements=0
  lastIndex=len(row)-1

  cursor, lastCursor=findNextCursors(letter, cursor, lastIndex, row)
  if(cursor==lastCursor):
    return 0, lastIndex, row, movedElements

  while(cursor!=lastCursor):
    # print(cursor, lastCursor)
    step=step+1
    movedElements=movedElements+lastCursor-cursor+1
    row=row[:cursor]+list(reversed(row[cursor:lastCursor+1]))+row[lastCursor+1:]
    cursor, lastCursor=findNextCursors(letter, cursor, lastCursor, row)

  return step, cursor, row, movedElements

def solve():
  rows=openFile("raw.txt")
  row=parseRows(rows)

  letter=row[0]
  lenRow=len(row)

  step=0
  
  while(True):
    innerStep, cursor, row, _=fixLetter(letter, row)
    step=step+innerStep
    if(cursor==lenRow-1):
      return step
    letter=row[cursor+1]

def fixLetterDirectly(innerRow):
  color=innerRow[0]

  colorGroup=[]
  gapGroup=[]
  gapElement=[]
  index=0
  lenInnerRow=len(innerRow)
  count=0
  while(index<lenInnerRow):
    if(innerRow[index]==color):
      count=count+1
      if(gapElement):
        gapGroup.append("".join(gapElement))
      gapElement=[]
    else:
      if count!=0:
        colorGroup.append(count)
        count=0
      gapElement.append(innerRow[index])
    index=index+1

  if count != 0:
    colorGroup.append(count)
  if gapElement:
    gapGroup.append("".join(gapElement))
  # print(colorGroup, gapGroup)
  

  colorGroup=colorGroup[1:]
  gapToHandle=len(colorGroup)

  lastPartSaved=""
  if(len(gapGroup)>gapToHandle):
    lastPartSaved=gapGroup[gapToHandle]

  gapGroup=gapGroup[:gapToHandle]


  currentFlipLength=sum(colorGroup) + sum (len(x) for x in gapGroup)
  # print(currentFlipLength)

  dispari=True
  flipElement=0
  rearranged=[]
  total=0
  for _ in colorGroup:
    total=total+currentFlipLength
    if dispari:
      elementChosen=gapGroup[flipElement][::-1]
      addedColor=colorGroup[-flipElement-1]
      dispari=False
    else:
      elementChosen=gapGroup[-flipElement-1]
      addedColor=colorGroup[flipElement]
      dispari=True
      flipElement=flipElement+1
    rearranged.append(elementChosen)

    currentFlipLength=currentFlipLength-len(elementChosen)-addedColor
  rearranged.reverse()

  rearranged.append(lastPartSaved)
  
  return "".join(rearranged), total
    




def solve2(repetition):
  rows=openFile("raw.txt")
  innerRow=parseRows(rows)
  innerRow=innerRow*repetition
  step=0
  while(innerRow):
    innerRow, innerLength=fixLetterDirectly(innerRow)
    print(innerLength, "copletataletterra")
    step=step+innerLength
  return step

print(solve2(100))
