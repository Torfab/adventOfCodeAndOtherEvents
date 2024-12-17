from utilityz import *

register={0:0, 1:1, 2:2, 3:3, 4:0, 5:0, 6:0}

operations={0:"adv", 1:"bxl", 2:"bst", 3:"jnz", 4:"bxc", 5:"out", 6:"bdv", 7:"cdv"}
ris=""

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
        print("output:", comboValue%8)
        global ris
        ris=ris+str(comboValue%8)+","
        return instructionPointer+2
    if(operand=="bdv"):
        register[5]=register[4]//(2**comboValue)
        return instructionPointer+2
    if(operand=="cdv"):
        register[6]=register[4]//(2**comboValue)
        return instructionPointer+2
    
def solve(part):
  rows=getOldAocInput(16)
  program=parseRows(rows)
  instructionPointer=0
  while(instructionPointer<len(program)-1):
      operandNumber=program[instructionPointer]
      value=program[instructionPointer+1]
      instructionPointer=evaluate(operandNumber,value, instructionPointer)
  return ris[:-1]

print(solve("a"))

# print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)
