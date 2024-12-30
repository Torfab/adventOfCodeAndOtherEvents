def runSingleCommand(commands, cursor):
  if commands[cursor]==1:
    commands[commands[cursor+3]]=commands[commands[cursor+1]]+commands[commands[cursor+2]]
    return cursor+4
  elif commands[cursor]==2:
    commands[commands[cursor+3]]=commands[commands[cursor+1]]*commands[commands[cursor+2]]
    return cursor+4
  return cursor+1

def runCommands(commands):
  cursor=0
  while(commands[cursor]!=99):
    cursor=runSingleCommand(commands, cursor)
  return commands
