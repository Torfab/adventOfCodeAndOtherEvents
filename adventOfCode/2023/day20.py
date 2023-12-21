from utility import *

def parseRows(rows):
  flipflops={}
  conjunctions={}

  for row in rows:
    rowSplitted=row.split(" -> ")

    if(rowSplitted[0][0]=="&"):
      conjunctions[rowSplitted[0][1:]] = {"output": rowSplitted[1].split(", "), "input": {}, "banana": 0}


    if(rowSplitted[0][0]=="%"):
      connections=rowSplitted[1].split(", ")
      flipflops[rowSplitted[0][1:]]={"active":0, "connections": connections}

    if(rowSplitted[0]=="broadcaster"):
      broadcaster=rowSplitted[1].split(", ")
  
  for k,v in conjunctions.items():
    for element in v["output"]:
      if(conjunctions.get(element)!=None):
        conjunctions[element]["input"][k]=0
      if(element=="rx"):
        lastNode={"sender": k}
  
  for k,v in flipflops.items():
    for element in v["connections"]:
      if(conjunctions.get(element)!=None):
        conjunctions[element]["input"][k]=0
      if(element=="rx"):
        lastNode={"sender": k}


  for element in broadcaster:
    if (conjunctions.get(element)!=None):
      conjunctions[element]["input"]["broadcaster"]=0


  return flipflops, conjunctions, broadcaster, lastNode





def sendPulse(queue:list, pulseCounter, flipflops, conjunctions, broadcaster, last):
  while(queue):

    sender, label, mode = queue.pop(0)
    if(label==last and mode==0):
      return True
    # print(sender, label, mode)
    pulseCounter[mode]=pulseCounter[mode]+1

    if(label=="broadcaster"):
      for element in broadcaster:
        queue.append((label,element,mode))
      continue

    if(flipflops.get(label)!=None):
      if(mode):
        continue
      flipflops[label]["active"]=(flipflops[label]["active"]+1)%2
      for element in flipflops[label]["connections"]:
        queue.append((label, element, flipflops[label]["active"]))
      continue

    if(conjunctions.get(label)!=None):
      if(conjunctions[label]["input"][sender]!=mode):
        conjunctions[label]["input"][sender]=mode
        if(mode):
          valueToChange=1
        else:
          valueToChange=-1
        conjunctions[label]["banana"]=conjunctions[label]["banana"]+valueToChange

      if(conjunctions[label]["banana"]==len(conjunctions[label]["input"])):
        for element in conjunctions[label]["output"]:
          queue.append((label, element, 0))
      else:
        for element in conjunctions[label]["output"]:
          queue.append((label, element, 1))

      conjunctions[label]["input"][sender]=mode
  return False

def solveA():
  rows=getOldAocInput(20)
  flipflops, conjunctions, broadcaster, _ = parseRows(rows)

  #0 BASSO #1 ALTO
  pulseCounter=[0,0]

  queue=[("button", "broadcaster", 0)]

  for _ in range(1000):
    sendPulse(queue, pulseCounter, flipflops, conjunctions, broadcaster, None)
    queue=[("button", "broadcaster", 0)]

  return pulseCounter[0]*pulseCounter[1]

def fullReset(flipflops, conjunctions):
  for k in flipflops.keys():
    flipflops[k]["active"]=0

  for k in conjunctions.keys():
    conjunctions[k]["banana"]= 0

    for kin in conjunctions[k]["input"].keys():
      conjunctions[k]["input"][kin]=0

def solveB():
  rows=getOldAocInput(20)
  flipflops, conjunctions, broadcaster, lastNode = parseRows(rows)

  #0 BASSO #1 ALTO
  pulseCounter=[0,0]

  queue=[("button", "broadcaster", 0)]
  results=[]
  
  for node in conjunctions[lastNode["sender"]]["input"].keys():
    count=0
    while(not sendPulse(queue, pulseCounter, flipflops, conjunctions, broadcaster, node)):
      count=count+1
      queue=[("button", "broadcaster", 0)]
    results.append(count)
    fullReset(flipflops, conjunctions)
    count=0
      

  return math.lcm(*results)



print(solveA())
print(solveB())