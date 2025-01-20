from utility import *
from intCode import *

def solve(part):
  rows=getOldAocInput(19)
  commands=parseIntCode(rows)
  cursor=0
  relativeBase=0
  finish=False
  theInput=[]
  if part=="a":
    theInput=inputAsciiLine('''NOT C T
OR T J
NOT B T
OR T J
NOT A T
OR T J
AND D J
WALK''')
    while(not finish):
      commands, output, cursor, finish, relativeBase=runCommands(commands, inputs=theInput, pauseMode=True, cursor=cursor, relativeBase=relativeBase, pauseOnNewLine=True)
      if output[-1]>0x110000:
        return output[-1]
      # print(translateAsciiLine(output), end="")
      # input()

  if part=="b":
    theInput=inputAsciiLine('''NOT C T
OR T J
NOT B T
OR T J
NOT A T
OR T J
AND D J
NOT D T
OR E T
OR H T
AND T J
RUN''')
    while(not finish):
      commands, output, cursor, finish, relativeBase=runCommands(commands, inputs=theInput, pauseMode=True, cursor=cursor, relativeBase=relativeBase, pauseOnNewLine=True)
      if output and output[-1]>0x110000:
        return output[-1]
      # print(translateAsciiLine(output), end="")
      # input()

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)