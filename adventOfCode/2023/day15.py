from utility import *


def myHash(text):
  subResult=0
  for char in text:
    subResult=subResult+ord(char)
    subResult=subResult*17
    subResult=subResult%256
  return subResult

def buildBox():
  box={}
  for i in range(256):
    box[i]={}
  return box



def solve(part):
  rows=getOldAocInput(15)
  rowsSplitted= rows[0].split(",")
  # print(rowsSplitted)
  result=0
  if (part=="a"):
    for element in rowsSplitted:
      result=result+myHash(element)
  else:
    box=buildBox()
  
    for element in rowsSplitted:
      if(element[-1]=="-"):
        element=element[:len(element)-1]
        boxIdx=myHash(element)
        box[boxIdx].pop(element,0)
      else:
        elementSplit=element.split("=")
        element=elementSplit[0]
        value=int(elementSplit[1])
        boxIdx=myHash(element)
        box[boxIdx][element]=value
    for k, v in box.items():
      queue=1
      for _, lensLenght in v.items():
        result=result+(k+1)*queue*lensLenght
        queue=queue+1
  return result



print(solve("a"))
print(solve("b"))