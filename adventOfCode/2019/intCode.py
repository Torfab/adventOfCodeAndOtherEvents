
def parseIntCode(rows):
  return {i:int(x) for i,x in enumerate(rows[0].split(","))}

def leadString(num, length=5, padder="0"):
  num=str(num)
  lenNum=len(num)
  ris=padder*(length-lenNum)
  return ris+num

def paramValue(value, parMode, commands, relativeBase):
  if parMode==1:
    return value
  if parMode==0:
    return commands.get(value, 0)
  if parMode==2:
    return commands[value+relativeBase]

def checkInstruction(commands, cursor):
  instruction=commands[cursor]
  parMode=None
  if instruction>99:
    stringInstruction=leadString(instruction)
    params=stringInstruction[:-2]
    parMode=[]
    for element in params:
      parMode.append(int(element))
    instruction=instruction%100
  return [instruction, parMode]

def runSingleCommand(commands, cursor, outputs, theInput=None, relativeBase=0):
  instruction, parMode=checkInstruction(commands, cursor)
  offSet=0
  if parMode!=None and parMode[0]==2:
    offSet=relativeBase
  if instruction==1:
    if parMode==None:
      parMode=[0,0,0]
    commands[commands[cursor+3]+offSet]=paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)+paramValue(commands[cursor+2], parMode[-2], commands, relativeBase)
    return [cursor+4, relativeBase]
  elif instruction==2:
    if parMode==None:
      parMode=[0,0,0]
    commands[commands[cursor+3]+offSet]=paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)*paramValue(commands[cursor+2], parMode[-2], commands, relativeBase)
    return [cursor+4, relativeBase]
  elif instruction==3:
    if parMode[-1]==2:
      weirdOffset=relativeBase
    commands[commands[cursor+1]+weirdOffset]=theInput
    return [cursor+2, relativeBase]
  elif instruction==4:
    if parMode==None:
      parMode=[0,0]
    outputs.append(paramValue(commands[cursor+1], parMode[-1], commands, relativeBase))
    return [cursor+2, relativeBase]
  elif instruction==5:
    if parMode==None:
      parMode=[0,0,0]
    if(paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)!=0):
      return [paramValue(commands[cursor+2], parMode[-2], commands, relativeBase), relativeBase]
    else:
      return [cursor+3, relativeBase]
  elif instruction==6:
    if parMode==None:
      parMode=[0,0],0
    if(paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)==0):
      return [paramValue(commands[cursor+2], parMode[-2], commands, relativeBase), relativeBase]
    else:
      return [cursor+3, relativeBase]
  elif instruction==7:
    if parMode==None:
      parMode=[0,0,0]
    if(paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)<paramValue(commands[cursor+2], parMode[-2], commands, relativeBase)):
      commands[commands[cursor+3]+offSet]=1
    else:
      commands[commands[cursor+3]+offSet]=0
    return [cursor+4, relativeBase]
  elif instruction==8:
    if parMode==None:
      parMode=[0,0,0]
    if(paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)==paramValue(commands[cursor+2], parMode[-2], commands, relativeBase)):
      commands[commands[cursor+3]+offSet]=1
    else:
      commands[commands[cursor+3]+offSet]=0
    return [cursor+4, relativeBase]
  elif instruction==9:
    if parMode==None:
      parMode=[0, 0]
    relativeBase=relativeBase+paramValue(commands[cursor+1], parMode[-1], commands, relativeBase)
    return [cursor+2, relativeBase]
  else:
    print("operation not recognized", instruction)
  return [cursor+1, relativeBase]

def runCommands(commands, inputs=None, cursor=0, pauseMode=False, relativeBase=0):
  if isinstance(inputs, int):
    inputs=[inputs]
  outputs=[]
  inputCursor=0
  theInput=None
  
  while(commands[cursor]!=99):
    instruction, _=checkInstruction(commands, cursor)
    if instruction==3:
      theInput=inputs[inputCursor]
      inputCursor=inputCursor+1
    if instruction==4 and pauseMode:
      cursor, relativeBase=runSingleCommand(commands, cursor, outputs, theInput, relativeBase)
      if instruction==99:
        return [commands, outputs, cursor, True, relativeBase]
      return [commands, outputs, cursor, False, relativeBase]
    cursor, relativeBase=runSingleCommand(commands, cursor, outputs, theInput, relativeBase)
  return [commands, outputs, cursor, True, relativeBase]
