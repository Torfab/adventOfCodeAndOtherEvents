from utility import *
from intCode import *

def parseRows(rows):
  return [int(x) for x in rows[0].split(",")]

def solve(part):
  rows=getOldAocInput(5)
  commands=parseRows(rows)
  if part=="a":
    result=runCommands(commands, 1)
    outputs=result[1]
    return outputs[-1]
  if part=="b":
    result=runCommands(commands, 5)
    outputs=result[1]
    return outputs[-1]

print(solve("a"))
print(solve("b"))

# print(evaluateTime(timeElapse))
