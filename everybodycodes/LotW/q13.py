from utility import *

def parseRows(rows):
  clocks=[]
  arms=[{} for _ in range(3)]
  
  for e,row in enumerate(rows):
    if(row):
      if row[0]=="C":
        continue
      if row[1]=="e":
        continue
    if row=="":
      clocks.append(arms)
      arms=[{} for _ in range(3)]
      continue
    rowSplitted=row.split(" ")
    nameKey=rowSplitted[0]
    if(nameKey!="direction"):
      values=[int(x) for x in rowSplitted[1].split(":")]
    else:
      values=[]
      for x in rowSplitted[1].split(":"):
        if x=="CW":
          values.append(1)
        else:
          values.append(-1)
    for i in range(3):
      arms[i][nameKey]=values[i]
  clocks.append(arms)
  return clocks

def normalize(arms):
  arms=arms.copy()
  theLCM=1
  for arm in arms:
    theLCM=lcm(theLCM, arm["hands"])
  theLCM=theLCM*2
  for arm in arms:
    arm["pulse"]=theLCM//arm["hands"]
    arm["current"]=arm["pulse"]*arm["current"]
    arm["hands"]=theLCM
    arm["justReached"]=True
  return arms

def checkCountMovements(myMovement, movements):
  result=0
  setMyMovement=set(myMovement[0])
  for m in movements:
    setM=set(m[0])
    # print(m)
    if m[0][0]==myMovement[0][0]:   # SE PARTONO INSIEME non possono toccarsi, anche se entrambi sono fermi non possono toccarsi
      continue
    if(m[1]==0 and m[0][0] in setMyMovement):  # SE QUELLO CONSERVATO è FERMO E QUELLO NUOVO CI PASSA, si aumenta di uno
      result=result+1
      continue
    if(myMovement[1]==0 and myMovement[0][0] in setM): # SE QUELLO NUOVO è FERMO E QUELLO CONSERVATO CI PASSA si aumenta di uno
      result=result+1
      continue
    if m[0][-1]==myMovement[0][-1] and m[1]==myMovement[1]: # SE ANDANDO NELLA STESSA DIREZIONE HO L'ULTIMO ELEMENTO IN COMUNE NIENTE
      continue
    if(setMyMovement.isdisjoint(setM)): # SE MANCO PASSANO GLI STESSI POSTI NIENTE
      continue
    if setMyMovement <= setM or setM <= setMyMovement: # SE UNO è COMPLETAMENTE SOTTOINSIEME DELL'ALTRO
      if(myMovement[1]!=m[1]):  # IN DIREZIONI DIVERSE AUMENTA DI UNO
        result=result+1
      else:
        # print("MA CHE DAVVERO?", myMovement, m )
        result=result+1 # IN DIREZIONI UGUALI AUMENTA DI DUE
        
    else:  # NEL CASO QUINDI CHE C'è UNA PARTE IN COMUNE E UNA NO
      if myMovement[1]!=m[1]: #AUMENTA SOLO SE DIREZIONI DIVERSE
        result=result+1
        # print("BECCATI", myMovement, m)
  return result

def compareClocks(clock1, clock2):
  c1 = clock1.copy()
  c2 = clock2.copy()
  c1.pop("move", None)
  c2.pop("move", None)
  return c1 == c2

def checkPosition(arms):
  position=[]
  result=0
  for arm in arms:
    for element in position:
      if element[0]!=arm["current"] or compareClocks(arm, element[2]):  # SE NON SONO NELLO STESSO PUNTO o SE SONO LO STESSO IDENTICO BRACCIO, inserisci ma non contare
        continue
      if arm["justReached"]: #QUESTO capita se sono nello stesso punto E NON sono lo stesso braccio
        # print("in teoria io mi sono mosso e lui chissene", arm, element)
        #se mi sono appena mosso a prescindere che l'element era fermo o era mosso aggiungo
        result=result+1
      else:
        if element[1]: #SE NON MI SONO APPENA MOSSO, MA il tizio che incontr si è appena mosso aggiungo 1
          # print("in teoria io sono fermo e lui si è mosso", arm, element)
          result=result+1
    position.append((arm["current"], arm["justReached"], arm))
    
  return result

def doMove(arms):
  movements=[]
  result=0
  for arm in arms:
    if(arm["move"]>0):
      startMovement=arm["current"]
      arm["current"]=(arm["current"]+arm["pulse"]*arm["direction"])%arm["hands"]
      # endMovement=arm["current"]
      direction=arm["direction"]
      arm["move"]=arm["move"]-1

      myMovement=(list((startMovement+i*direction)%arm["hands"] for i in range(arm["pulse"])), direction)
    else:
      myMovement=([arm["current"]], 0)
      arm["justReached"]=False
    result=result+checkCountMovements(myMovement, movements)
    movements.append(myMovement)

  # print("ah", movements)
  result=result+checkPosition(arms)
  return result

def doSnapShot(arms):
  return (arms[0]["current"], arms[1]["current"], arms[2]["current"])

def solveSingleClockOLD(arms):
  arms=normalize(arms)

  
  result=0

  step=0
  while any(arm["move"] != 0 for arm in arms):
    step=step+1
    count=doMove(arms)
    # print("siamo allo step", step, "finora ho contato movimenti:", count)
    # print()
    result=result+count
  return result

def solveSingleClock(arms):
  arms=normalize(arms)

  minMove=min(x["move"] for x in arms)
  print("minMove", minMove)
  print("tutte il resto fanno", [x["move"]-minMove for x in arms])

  
  currentState=tuple([x["current"] for x in arms])
  originalState=currentState


  alreadyJumped=False


  armsAt0=0

  step=0
  cycleStep=0
  result=0
  cycleResult=0
  while any(arm["move"] != 0 for arm in arms):
    if(armsAt0!=sum(1 for x in arms if x["move"]==0)):
      armsAt0=sum(1 for x in arms if x["move"]==0)
      alreadyJumped=False
      originalState=currentState
      cycleStep=0
      cycleResult=0
      minMove=min(x["move"] for x in arms if x["move"]>0)
    cycleStep=cycleStep+1

    step=step+1
    count=doMove(arms)
    # print("WE", arms[0]["move"])
    result=result+count
    cycleResult=cycleResult+count

    currentState=tuple([x["current"] for x in arms])
    if(not alreadyJumped and currentState==originalState):
      howManyCyclesMore=(minMove//cycleStep)-1
      result=result+cycleResult*howManyCyclesMore
      for arm in arms:
        if(arm["move"]>0):
          arm["move"]=arm["move"]-howManyCyclesMore*cycleStep
      step=step+cycleStep*howManyCyclesMore
      alreadyJumped=True

    # print("siamo allo step", step, "finora ho contato movimenti:", count)
    # print()
  return result

def solve():
  rows=openFile("raw.txt")
  clocks=parseRows(rows)
  result=0
  for clock in clocks:
    # print(clock)
    clockSolved=solveSingleClock(clock)
    result=result+clockSolved
    print("URRA", clockSolved)
    
  return result

# evaluateTime(solve, repetitions=1)
print(solve())
