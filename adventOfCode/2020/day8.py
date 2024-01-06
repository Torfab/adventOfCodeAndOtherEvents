from utility import *

def parseRows(rows):
  instructions=[]
  for row in rows:
    rowSplitted=row.split(" ")
    instructions.append((rowSplitted[0], int(rowSplitted[1])))
  return instructions

def evaluateAcc(instructions):
  marked=set()
  idx=0
  acc=0
  while(idx<len(instructions)):
    inst, value=instructions[idx]
    if(idx in marked):
      return idx, acc
    marked.add(idx)
    if(inst=="nop"):
      idx=idx+1
      continue
    if(inst=="acc"):
      idx=idx+1
      acc=acc+value
      continue
    if(inst=="jmp"):
      idx=idx+value
      continue
  return idx, acc

def solve(part):
  rows= getOldAocInput(8)
  instructions=parseRows(rows)
  if(part=="a"):
    return evaluateAcc(instructions)[1]
  resultIdx=0
  if(part=="b"):
    idx=0
    for idx in range(len(instructions)):
      if(instructions[idx][0]=="jmp"):
        instructions[idx]=("nop", instructions[idx][1])
        resultIdx, resultAcc=evaluateAcc(instructions)
        instructions[idx]=("jmp", instructions[idx][1])
      elif(instructions[idx][0]=="nop"):
        instructions[idx]=("jmp", instructions[idx][1])
        resultIdx, resultAcc=evaluateAcc(instructions)
        instructions[idx]=("nop", instructions[idx][1])
      if(resultIdx==len(instructions)):
        return resultAcc
      idx=idx+1

print(solve("a"))
print(solve("b"))
