from utilityz import *

register={0:0, 1:1, 2:2, 3:3, 4:0, 5:0, 6:0}


# This problem want you to look at the input, in my input i always used those following two numbers
# So i decided to save them in the convenient data structure i use to work with.
cinque=["1","0","1"]
sei=["1","1","0"]

def parseRows(row):
  register[4]=int(row[0].split(":")[1])
  register[5]=int(row[1].split(":")[1])
  register[6]=int(row[2].split(":")[1])
  
  program= [int(x) for x in row[4].split(":")[1].split(",")]
  return program
  
def evaluate(operand, literalValue, ris):
  comboValue=register[literalValue]
  if(operand==0):
    register[4]=register[4]//(2**comboValue)
  elif(operand==1):
    register[5]=literalValue^register[5]
  elif(operand==2):
    register[5]=comboValue%8
  elif(operand==3):
    if(register[4]!=0):
      return literalValue
  elif(operand==4):
    register[5]=register[5]^register[6]
  elif(operand==5):
    ris.append(str(comboValue%8))
  elif(operand==6):
    register[5]=register[4]//(2**comboValue)
  elif(operand==7):
    register[6]=register[4]//(2**comboValue)

  
def solve():
  rows=getOldAocInput(17)
  program=parseRows(rows)
  instructionPointer=0
  ris=[]
  while(instructionPointer<len(program)-1):
    operandNumber=program[instructionPointer]
    value=program[instructionPointer+1]
    evaluated=evaluate(operandNumber,value, ris)
    if evaluated!=None:
      instructionPointer=evaluated
    else:
      instructionPointer=instructionPointer+2
  return ",".join(ris) 

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

def myShift(testA, b):
  shiftNumber=fromBinaryToInteger("".join(b))
  if(shiftNumber==0):
    return 0,testA
  return shiftNumber, testA[-shiftNumber-3:-shiftNumber]
  

def solveB():
  rows=getOldAocInput(17)
  program=parseRows(rows)
  testA=[["0","0","0","0","0","0","0"]]
  for element in reversed(program):
    candidati=[]
    binaryToFind=myPad([x for x in fromIntegerToBinary(int(element))])
    
    for possibility in testA:

      for i in range(8):
        testTurno=possibility+myPad([x for x in fromIntegerToBinary(i)])
        b=testTurno
        b=myXor(b, cinque)
        shiftNumber, c=myShift(testTurno, b)
        possibleB=myXor(b,c)
        possibleB=myXor(possibleB, sei)
        if(possibleB==binaryToFind):
          candidati.append((testTurno, shiftNumber, c))
    finalRes=[]
    for candidato in candidati:
      tentativeTest=candidato[0].copy()
      shiftNumber=candidato[1]
      possibleC=candidato[2]
      if shiftNumber!=0:
        tentativeTest[-shiftNumber-3]=possibleC[0]
        tentativeTest[-shiftNumber-2]=possibleC[1]
        tentativeTest[-shiftNumber-1]=possibleC[2]
      tentativeRisultato=int("".join([x if x!="x" else "0" for x in tentativeTest]))
      finalRes.append((tentativeRisultato, tentativeTest))

    finalRes= sorted(finalRes, key=lambda x:x[0])
    testA=[res[1] for res in finalRes]
  return fromBinaryToInteger("".join([x if x!="x" else "0" for x in testA[0]]))

print(solve())
print(solveB())
