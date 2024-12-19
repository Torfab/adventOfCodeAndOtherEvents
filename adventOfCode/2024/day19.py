from utilityz import *
import functools

def parseRow(rows):
  towelsAvailable=tuple(rows[0].split(", "))
  designsList=rows[2:]
  return towelsAvailable, designsList

@functools.cache
def checkDesign(design, towelsAvailable):
  if(design==""):
    return 1
  ris=0
  for towel in towelsAvailable:
    if design.startswith(towel):
      ris=ris + checkDesign(design[len(towel):], towelsAvailable)
  return ris

def solve(part):
  rows=getOldAocInput(19)
  towelsAvailable, designsList=parseRow(rows)
  
  ris=0
  if(part=="a"):
    for design in designsList:
      if(checkDesign(design, towelsAvailable)!=0):
        ris=ris+1
  elif(part=="b"):
    for design in designsList:
      ris=ris+checkDesign(design, towelsAvailable)
  return ris


print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)