from utility import *

def parseRows(rows):
  return [int(x) for x in rows]

def flyFlock(rounds, flock):

  moved=True
  count=0
  while(moved==True):
    moved=False
    for i in range(len(flock)-1):
      if(flock[i]>flock[i+1]):
        moved=True
        flock[i]=flock[i]-1
        flock[i+1]=flock[i+1]+1
    if(moved):
      count=count+1
    if(count==rounds):
      return flock

  moved=True
  while(moved==True):
    moved=False
    for i in range(len(flock)-1):
      if(flock[i]<flock[i+1]):
        moved=True
        flock[i]=flock[i]+1
        flock[i+1]=flock[i+1]-1
    if(moved):
      count=count+1
    if(count==rounds):
      return flock
    
def flyFlock2(flock):

  moved=True
  count=0
  while(moved==True):
    moved=False
    for i in range(len(flock)-1):
      if(flock[i]>flock[i+1]):
        moved=True
        flock[i]=flock[i]-1
        flock[i+1]=flock[i+1]+1
    if(moved):
      count=count+1

  moved=True
  while(moved==True):
    moved=False
    for i in range(len(flock)-1):
      if(flock[i]<flock[i+1]):
        moved=True
        flock[i]=flock[i]+1
        flock[i+1]=flock[i+1]-1
    if(moved):
      count=count+1
    if(moved==False):
      return count
    

def flyFlock3(flock):

  AIM=sum(flock)//len(flock)
  flockToReduce=list(filter(lambda x: x>AIM, flock))
  flockToReduce.insert(0, AIM)

  diffArr=[flockToReduce[idx+1]-flockToReduce[idx] for idx in range(len(flockToReduce)-1)]
  diffArr.reverse()

  result=0
  iteration=1
  for element in diffArr:
    result=result+element*iteration
    iteration=iteration+1
  return result


def solve():
  rows=openFile("raw.txt")
  flock=parseRows(rows)

  finalFlock=flyFlock(10, flock)
  mySum=0
  for i, val in enumerate(finalFlock):
    mySum=mySum+(i+1)*val

  return mySum

def solve2():
  rows=openFile("raw.txt")
  flock=parseRows(rows)

  return flyFlock2(flock)

def solve3():
  rows=openFile("raw.txt")
  flock=parseRows(rows)

  return flyFlock3(flock)


print(solve3())
