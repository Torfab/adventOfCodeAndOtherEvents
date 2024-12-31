def leadString(num, length=4, padder="0"):
  num=str(num)
  lenNum=len(num)
  ris=padder*(length-lenNum)
  return ris+num

def paramValue(value, parMode, commands):
  if parMode==1:
    return value
  if parMode==0:
    return commands[value]

def runSingleCommand(commands, cursor, outputs, input=None,):
  instruction=commands[cursor]
  parMode=None
  if instruction>99:
    stringInstruction=leadString(instruction)
    params=stringInstruction[:-2]
    parMode=[]
    for element in reversed(params):
      parMode.append(int(element))
    instruction=instruction%100
    # parMode
  if instruction==1:
    if parMode==None:
      parMode=[0,0]
    commands[commands[cursor+3]]=paramValue(commands[cursor+1], parMode[0], commands)+paramValue(commands[cursor+2], parMode[1], commands)
    return cursor+4
  elif instruction==2:
    if parMode==None:
      parMode=[0,0]
    commands[commands[cursor+3]]=paramValue(commands[cursor+1], parMode[0], commands)*paramValue(commands[cursor+2], parMode[1], commands)
    return cursor+4
  elif instruction==3:
    commands[commands[cursor+1]]=int(input)
    return cursor+2
  elif instruction==4:
    # if(commands[cursor+2]==99):
    #   print("Final ", end="")
    if parMode==None:
      parMode=[0]
    # print("Output", paramValue(commands[cursor+1], parMode[0], commands))
    outputs.append(paramValue(commands[cursor+1], parMode[0], commands))
    return cursor+2
  elif instruction==5:
    if parMode==None:
      parMode=[0,0]
    if(paramValue(commands[cursor+1], parMode[0], commands)!=0):
      return paramValue(commands[cursor+2], parMode[1], commands)
    else:
      return cursor+3
  elif instruction==6:
    if parMode==None:
      parMode=[0,0]
    if(paramValue(commands[cursor+1], parMode[0], commands)==0):
      return paramValue(commands[cursor+2], parMode[1], commands)
    else:
      return cursor+3
  elif instruction==7:
    if parMode==None:
      parMode=[0,0,0]
    if(paramValue(commands[cursor+1], parMode[0], commands)<paramValue(commands[cursor+2], parMode[1], commands)):
      commands[commands[cursor+3]]=1
    else:
      commands[commands[cursor+3]]=0
    return cursor+4
  elif instruction==8:
    if parMode==None:
      parMode=[0,0,0]
    if(paramValue(commands[cursor+1], parMode[0], commands)==paramValue(commands[cursor+2], parMode[1], commands)):
      commands[commands[cursor+3]]=1
    else:
      commands[commands[cursor+3]]=0
    return cursor+4
  
    
    

  else:
    print("operation not recognized")
  return cursor+1

def runCommands(commands, input=None):
  cursor=0
  outputs=[]
  while(commands[cursor]!=99):
    cursor=runSingleCommand(commands, cursor, outputs, input)
  return commands, outputs
