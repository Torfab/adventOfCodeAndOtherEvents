from utility import *

def parseRows(rows):
  row=rows[0]
  return [int(x) for x in row]

def doAPhase(elements, mainPattern):
  elementCursor=0
  newElements=[]
  while(elementCursor<len(elements)):
    repetition=elementCursor+1
    innerCursor=0
    blip=0
    counter=1
    if counter%repetition==0:
      blip=(blip+1)%len(mainPattern)
    ris=0
    while(innerCursor<len(elements)):
      ris=ris+elements[innerCursor]*mainPattern[blip]
      innerCursor=innerCursor+1
      counter=counter+1
      if counter%repetition==0:
        blip=(blip+1)%len(mainPattern)
    newElements.append(abs(ris)%10)
    elementCursor=elementCursor+1
  return newElements


def solve(part):
  rows=getOldAocInput(16)
  elements=parseRows(rows)
  if part=="a":
    mainPattern=[0,1,0,-1]
    for _ in range(100):
      elements=doAPhase(elements, mainPattern)
    return "".join([str(x) for x in elements[:8]])
  if part=="b":
    newElements=[]
    for _ in range(10000):
      newElements.extend(elements)
    offSet=int("".join([str(x) for x in elements[:7]]))
    newElements=newElements[offSet:]

    # The offset make it easy, becuase it's tailored to have only ALL 0 to the first number, and then all 1
    # We can litterally calculate last number and go backwards from there
    for _ in range(100):
      for i in range(len(newElements)-2,-1, -1):
        newElements[i]=(newElements[i]+newElements[i+1])%10


    return "".join([str(x) for x in newElements[:8]])


print(solve("a"))
print(solve("b"))
