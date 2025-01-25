from utilityz import *
from intCode import *

# Technically not hard, Practically challenging.
# Challenge text was a bit foggy and articulated, there was a lot of trial and error.
# Intcode was not helping in debug what was happening.
# At first i thought i had to start a single intcode with first 50 address as input
# Secondly i thought, as always, he sent data with 10 at end
# Thirdly i couldn't understand how many -1 i had to send
# Fourthly i couldn't understand if when i received data it had priority against the sending of new data
# After i manage to find the way of the challenge on trial and error i could see that the text was very precise
# on all those. But you could see it only AFTER you failed and doublechecked your assumption
# Part B was a lot more easier because almost all the "what should i do?!? why it isn't working as expected" was done on part a
# But still i couldn't figure out what count as idle system, i had a lot of false positive where i was in idle before first nat value was done
# And first cycle of -1 in input wasn't the best aswel. In the end i manage to have a real nat value and it was done.

def updateComputer(computer, values):
  computer["commands"]=values[0]
  computer["output"]=values[1]
  computer["cursor"]=values[2]
  computer["finish"]=values[3]
  computer["relativeBase"]=values[4]

def solve(part):
  rows=getOldAocInput(23)
  commands=parseIntCode(rows)
  cursor=0
  relativeBase=0

  cluster=[]
  for element in range(50):
    values=runCommands(commands.copy(), inputs=[element], pauseMode=True, cursor=cursor, relativeBase=relativeBase, pauseOnInput=True)
    cluster.append({})
    updateComputer(cluster[element], values)
    cluster[element]["queue"]=[]
    cluster[element]["id"]=element
  
  lastSent=-1
  nat=-1
  cycle=0
  while(True):
    receivedNumber=0
    for i, element in enumerate(cluster):
      if(len(element["queue"])==0):
        values=runCommands(element["commands"], inputs=[-1], pauseMode=True, cursor=element["cursor"], relativeBase=element["relativeBase"], pauseOnInput=True)
        updateComputer(element, values)
        if len(values[1])>0:
          realOutput=[values[1][0]]
          for _ in range(2):
            values=runCommands(element["commands"], inputs=[], pauseMode=True, cursor=element["cursor"], relativeBase=element["relativeBase"], pauseOnInput=True)
            updateComputer(element, values)
            realOutput.append(values[1][0])
          # print("zsono il pc", i, "inserisco a", realOutput[0], "i valori", (realOutput[1], realOutput[2]))
          if(realOutput[0]==255):
            if(part=="a"):
              return realOutput[2]
            if(part=="b"):
              nat=(realOutput[1], realOutput[2])
          else:
          
            cluster[realOutput[0]]["queue"].append((realOutput[1], realOutput[2]))

      else:
        receivedNumber=receivedNumber+1
        received=element["queue"].pop(0)
        values=runCommands(element["commands"], inputs=[received[0]], pauseMode=True, cursor=element["cursor"], relativeBase=element["relativeBase"], pauseOnInput=True)
        updateComputer(element, values)
        while(len(values[1])!=0):
          realOutput=[values[1][0]]
          for _ in range(2):
            values=runCommands(element["commands"], inputs=[received[0]], pauseMode=True, cursor=element["cursor"], relativeBase=element["relativeBase"], pauseOnInput=True)
            updateComputer(element, values)
            realOutput.append(values[1][0])

          # print("sono il pc", i, "inserisco a", realOutput[0], "i valori", (realOutput[1], realOutput[2]))
          if(realOutput[0]==255):
            if(part=="a"):
              return realOutput[2]
            if(part=="b"):
              nat=(realOutput[1], realOutput[2])
          else:
            cluster[realOutput[0]]["queue"].append((realOutput[1], realOutput[2]))

          values=runCommands(element["commands"], inputs=[received[0]], pauseMode=True, cursor=element["cursor"], relativeBase=element["relativeBase"], pauseOnInput=True)
          updateComputer(element, values)
        values=runCommands(element["commands"], inputs=[received[1]], pauseMode=True, cursor=element["cursor"], relativeBase=element["relativeBase"], pauseOnInput=True)
        updateComputer(element, values)

    if(receivedNumber==0 and nat!=-1):
      if (lastSent==nat):
        return nat[1]
      else:
        lastSent=nat
        cluster[0]["queue"].append(nat)
    cycle=cycle+1



print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
