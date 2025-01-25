from utility import *
from intCode import *

# GIOCA

def solve():
  rows=getOldAocInput(23)
  commands=parseIntCode(rows)
  cursor=0
  relativeBase=0
  theInput=[]
  finish=False
  while(not finish):
    commands, output, cursor, finish, relativeBase=runCommands(commands, inputs=theInput, pauseMode=True, cursor=cursor, relativeBase=relativeBase, pauseOnNewLine=True)
    print(translateAsciiLine(output), end="")
    theInput=inputAsciiLine(input())
  return

print(solve())
# print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
