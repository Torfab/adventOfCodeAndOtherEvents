from utility import *


def solve1():
  rows=getOldAocInput(10)
  stack=[]
  x=1
  idx=0
  result=0
  while (idx<len(rows) or len(stack)>0):
    if(idx<len(rows)):
      splitted=rows[idx].split(" ")
      if(splitted[0]=="noop"):
        stack.append(dict(cycleToDo=1, value=0))
      if(splitted[0]=="addx"):
        stack.append(dict(cycleToDo=2, value=int(splitted[1])))
    
    stack[0]["cycleToDo"]=stack[0]["cycleToDo"]-1
    if(stack[0]["cycleToDo"]==0):
      x=x+stack[0]["value"]
      stack.pop(0)

    idx=idx+1

    if((idx+1)%40==20):
      result=result+x*(idx+1)
    
  return result

def solve2():
  rows=getOldAocInput(10)
  stack=[]
  x=1
  idx=0
  result=''
  while (idx<len(rows) or len(stack)>0):
    if(idx<len(rows)):
      splitted=rows[idx].split(" ")
      if(splitted[0]=="noop"):
        stack.append(dict(cycleToDo=1, value=0))
      if(splitted[0]=="addx"):
        stack.append(dict(cycleToDo=2, value=int(splitted[1])))

    cursor=(idx)%40
    if(cursor==0):
      result=result+'\n'
    if(cursor>=x-1 and cursor <=x+1):
      result=result+'#'
    else:
      result=result+'.'

    stack[0]["cycleToDo"]=stack[0]["cycleToDo"]-1
    if(stack[0]["cycleToDo"]==0):
      x=x+stack[0]["value"]
      stack.pop(0)

    idx=idx+1

  return result

print(solve2())