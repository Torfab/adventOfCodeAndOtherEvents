from utility import *

register={0:0, 1:1, 2:2, 3:3, 4:0, 5:0, 6:0}

operations={0:"adv", 1:"bxl", 2:"bst", 3:"jnz", 4:"bxc", 5:"out", 6:"bdv", 7:"cdv"}
ris=""

cinque=["1","0","1"]
sei=["1","1","0"]

def parseRows(row):
  register[4]=int(row[0].split(":")[1])
  register[5]=int(row[1].split(":")[1])
  register[6]=int(row[2].split(":")[1])
  
  program=[int(x) for x in row[4].split(":")[1].split(",")]
  return program
  
def evaluate(operandNumber, literalValue, instructionPointer):
  operand=operations[operandNumber]
  comboValue=register[literalValue]
  if(operand=="adv"):
    register[4]=register[4]//(2**comboValue)
    return instructionPointer+2
  if(operand=="bxl"):
    register[5]=literalValue^register[5]
    return instructionPointer+2
  if(operand=="bst"):
    register[5]=comboValue%8
    return instructionPointer+2
  if(operand=="jnz"):
    if(register[4]==0):
      return instructionPointer+2
    return literalValue
  if(operand=="bxc"):
    register[5]=register[5]^register[6]
    return instructionPointer+2
  if(operand=="out"):
    global ris
    ris=ris+str(comboValue%8)+","
    return instructionPointer+2
  if(operand=="bdv"):
    register[5]=register[4]//(2**comboValue)
    return instructionPointer+2
  if(operand=="cdv"):
    register[6]=register[4]//(2**comboValue)
    return instructionPointer+2
  
def solve():
  rows=getOldAocInput(17)
  program=parseRows(rows)
  instructionPointer=0
  while(instructionPointer<len(program)-1):
    operandNumber=program[instructionPointer]
    value=program[instructionPointer+1]
    instructionPointer=evaluate(operandNumber,value, instructionPointer)
  return ris[:-1]

def myXor(result, secondOperando):
  firstOperando=[0,0,0]
  for i in range(-3, 0):
    if result[i]=='0':
      firstOperando[i]=secondOperando[i]
    else:
      if(secondOperando[i]=='0'):
        firstOperando[i]='1'
      else:
        firstOperando[i]='0'
  return firstOperando

def myPad(c):
  toPad=3-len(c)
  for _ in range(toPad):
    c.insert(0,'0')
  return c

def esplodoC(c):
  candidates=[]
  current=[]
  if "x" not in c:
    return [c]
  for i in range(len(c)):
    if c[i]!="x":
      current.append(c[i])
    else:
      candidates=candidates+esplodoC(current+['0']+(c[i+1:] or []))
      candidates=candidates+esplodoC(current+['1']+(c[i+1:] or []))
      break
  return candidates

def myShift(testA, b):
  shiftNumber=fromBinaryToInteger("".join(b))
  if(shiftNumber==0):
    return 0,[testA]
  return shiftNumber, esplodoC(testA[-shiftNumber-3:-shiftNumber])
  

def solveB():
  rows=getOldAocInput(17)
  program=parseRows(rows)
  testA=[["0","0","0","0","0","0","0"]]
  for element in reversed(program):
    candidati=[]
    binaryToFind=myPad([x for x in fromIntegerToBinary(element)])
    
    for testino in testA:

      for i in range(8):
        testTurno=testino+myPad([x for x in fromIntegerToBinary(i)])
        b=testTurno
        b=myXor(b, cinque)
        shiftNumber, c=myShift(testTurno, b) #espandi a tutti i possibili C
        for possibleC in c:
          possibleB=myXor(b,possibleC)
          possibleB=myXor(possibleB, sei)
          if(possibleB==binaryToFind):
            candidati.append((testTurno, shiftNumber, possibleC))
      #valuta la C meno costosa
    finalRes=[]
    for candidato in candidati:
      tentativeTest=candidato[0].copy()
      if candidato[1]!=0:
        tentativeTest[-candidato[1]-3]=candidato[2][0]
        tentativeTest[-candidato[1]-2]=candidato[2][1]
        tentativeTest[-candidato[1]-1]=candidato[2][2]
      tentativeRisultato=[x if x!="x" else "0" for x in tentativeTest]
      tentativeRisultato=int("".join(tentativeRisultato))
      finalRes.append((tentativeRisultato, tentativeTest))
    testA=[res[1] for res in finalRes]
  finalRes= sorted(finalRes, key=lambda x:x[0])
  return fromBinaryToInteger("".join([x if x!="x" else "0" for x in testA[0]]))

print(solve())
print(solveB())
