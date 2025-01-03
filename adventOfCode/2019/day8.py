from utility import *

def parseRows(rows, wide, tall):
  layers=[]
  sizeLayer=wide*tall
  i=0
  currentLayer=""
  row=rows[0]
  while(i<len(row)):
    currentLayer=currentLayer+row[i]
    i=i+1
    if i%sizeLayer==0:
      layers.append(currentLayer)
      currentLayer=""
  return layers


def solve(part):
  rows=getOldAocInput(8)
  layers=parseRows(rows, 25, 6)
  if part=="a":
    idxResult=0
    minResult=float("inf")
    for idx in range(len(layers)):
      zeros=layers[idx].count("0")
      if zeros<minResult:
        idxResult=idx
        minResult=zeros    
    return layers[idxResult].count("1")*layers[idxResult].count("2")
  if part=="b":
    finalLayer=""
    for i in range(25*6):
      currentIdx=0
      while(layers[currentIdx][i]=="2"):
        currentIdx=currentIdx+1
      finalLayer=finalLayer+layers[currentIdx][i]
    finalLayer=finalLayer.replace("1", "█")
    finalLayer=finalLayer.replace("0", " ")
    for y in range(6):
      for x in range(25):
        print(finalLayer[x+25*y], end="")
      print()



print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
