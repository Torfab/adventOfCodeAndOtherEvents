from utility import *

# not the most optimized especially part 3, but it does his work.

def parseRows(rows):
  return rows[0]

def evaluate1(order, sequence):
  step=0
  idxOrder=0
  lenSequence=len(sequence)
  i=0
  cycle=False
  while(i<lenSequence):
    if(order[idxOrder]==sequence[i]):
      i=i+1
      cycle=True
      continue
    cycle=False
    i=i+1
    step=step+1
    idxOrder=(idxOrder+1)%3
  if(cycle):
    step=step+1
  return step

def evaluate2(order, sequence):
  step=0
  idxOrder=0
  sequence=list(sequence*100)
  
  while(len(sequence)>0):
    if(order[idxOrder]==sequence[0]and len(sequence)%2==0):
      sequence.pop(len(sequence)//2)
    sequence.pop(0)
    step=step+1
    idxOrder=(idxOrder+1)%3
    print(len(sequence))
    
  return step

def evaluate3(order, sequence):
  step=0
  idxOrder=0
  sequence=list(sequence)
  sequence.reverse()
  sequence=sequence*100000

  
  while(sequence):
    if(order[idxOrder]==sequence[-1]and len(sequence)%2==0):
      sequence.pop(len(sequence)//2)
    sequence.pop()
    step=step+1
    idxOrder=(idxOrder+1)%3
    if (len(sequence)%10000)==0:

      print(len(sequence))
    
  return step

def evaluate4(order, sequence):
  step=0
  idxOrder=0
  sequence=[{"val":x, "pop":False} for x in sequence]
  sequence=[{"val":x["val"], "pop":x["pop"]} for _ in range(100000) for x in sequence]
  popped=0
  lenSequence=len(sequence)
  startPoint=lenSequence//2-1

  for element in sequence:
    if element["pop"]==True:
      continue
    element["pop"]=True
    step=step+1
    popped=popped+1
    if (element["val"]==order[idxOrder] and popped%2!=0):
      popped=popped+1
      sequence[startPoint+popped//2]["pop"]=True
    idxOrder=(idxOrder+1)%3

  return step

def solve(evaluate):
  rows=openFile("raw.txt")
  sequence=parseRows(rows)
  order=["R", "G", "B"]
  return evaluate(order, sequence)


print(solve(evaluate4))