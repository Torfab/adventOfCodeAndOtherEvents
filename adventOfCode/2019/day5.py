from utility import *
from intCode import *


def solve(part):
  rows=getOldAocInput(5)
  commands=parseIntCode(rows)
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
