from utility import *

def parseRows(rows):
  return int(rows[0]), int(rows[1])

def findLoopSize(num):
  subjectValue=7
  value=1
  i=0
  while(value!=num):
    i=i+1
    value=(value*subjectValue)%20201227
  return i

def solve():
  rows=getOldAocInput(25)
  cardPublicKey, doorPublicKey=parseRows(rows)

  cardLoopSize=findLoopSize(cardPublicKey)
  current=1
  for _ in range(cardLoopSize):
    current=(current*doorPublicKey)%20201227

  return current


print(solve())
