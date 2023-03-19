from utility import *

rows=openFile("input.txt")


mapRegisters={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}

i=0

lastComparison=False

def checkRegister(value):
  if (mapRegisters.get(value)!=None):
    return mapRegisters[value]
  else:
    return int(value)
# print(mapRegisters)
while(True):
  command=rows[i]
  splitted=command.split(" ")
  realCommand=splitted[0]
  if(realCommand=="ADD"):
    mapRegisters[splitted[1]]=mapRegisters[splitted[1]]+checkRegister(splitted[2])
  elif(realCommand=="MOD"):
    mapRegisters[splitted[1]]=mapRegisters[splitted[1]]%checkRegister(splitted[2])
  elif(realCommand=="DIV"):
    mapRegisters[splitted[1]]=mapRegisters[splitted[1]]//checkRegister(splitted[2])
  elif(realCommand=="MOV"):
    mapRegisters[splitted[1]]=checkRegister(splitted[2])
  elif(realCommand=="JMP"):
    i=i+checkRegister(splitted[1])
    continue
  elif(realCommand=="JIF"):
    if(lastComparison):
      i=i+checkRegister(splitted[1])
      continue
  elif(realCommand=="CEQ"):
    lastComparison=checkRegister(splitted[1])==checkRegister(splitted[2])
  elif(realCommand=="CGE"):
    lastComparison=checkRegister(splitted[1])>=checkRegister(splitted[2])
  elif(realCommand=="OUT"):
    print(checkRegister(splitted[1]))
  elif(realCommand=="END"):
    break
  i=i+1

